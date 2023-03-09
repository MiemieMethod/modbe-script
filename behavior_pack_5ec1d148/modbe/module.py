# -*- coding: utf-8 -*-


import mod.server.extraServerApi as extraServerApi
import mod.client.extraClientApi as extraClientApi
import common.gameConfig as GameConfig
from mod_log import logger

from modbe.enum import *

__all__ = ["Level", "ModBE", "Callback", "Actor", "Player", "Block", "Pos", "Tag", "EndTag", "ByteTag", "ShortTag", "IntTag", "LongTag", "FloatTag", "DoubleTag", "ByteArrayTag", "StringTag", "ListTag", "CompoundTag", "IntArrayTag"]


# Modules #

class Level(object):

    @staticmethod
    def getLevelId():
        if ModBE.isServer():
            return extraServerApi.GetLevelId()
        if ModBE.isClient():
            return extraClientApi.GetLevelId()


class ModBE(object):

    @staticmethod
    def isServer():
        # type: () -> bool
        return GameConfig.IsServer()

    @staticmethod
    def isClient():
        # type: () -> bool
        return GameConfig.IsClient()

    @staticmethod
    def preventDefault():
        if ModBE.isServer():
            server = extraServerApi.GetSystem("ModBE", "Server")
            server._cancelEvent = True
        if ModBE.isClient():
            client = extraClientApi.GetSystem("ModBE", "Client")
            client._cancelEvent = True

    @staticmethod
    def log(logType, logLevel, logArea, message, *args):
        # type: (int, int, str, str, Any) -> None
        level = LogLevel.toString(logLevel)
        if logType == LogType.debug:
            logger.debug("[" + level + "][" + logArea + "] " + message, *args)
        elif logType == LogType.info:
            logger.info("[" + level + "][" + logArea + "] " + message, *args)
        elif logType == LogType.error:
            logger.error("[" + level + "][" + logArea + "] " + message, *args)


if ModBE.isServer():
    _factory = extraServerApi.GetEngineCompFactory()
if ModBE.isClient():
    _factory = extraClientApi.GetEngineCompFactory()


class Callback(object):
    _serverCallbacks = {
        "entityAdd": "AddEntityServerEvent",  # (entity, entityType, pos, dimension, isBaby, itemName, auxValue) # type: (Actor, str, Pos, int, bool, str, int) -> None
        "itemUse": "ServerItemUseEvent",  # (entity, oldName, oldAux) # type: (Actor, str, int) -> None
        "itemTryUse": "ServerItemTryUseEvent"
        # (entity, oldName, oldAux, itemStack) # type: (Actor, str, int, ItemStack) -> None
    }
    _serverRegistered = {}
    _clientCallbacks = {
        "itemUse": "ClientItemUseEvent",
        # (entity, oldName, oldAux, itemStack) # type: (Actor, str, int, ItemStack) -> None
        "itemTryUse": "ClientItemTryUseEvent"
        # (entity, oldName, oldAux, itemStack) # type: (Actor, str, int, ItemStack) -> None
    }
    _clientRegistered = {}

    @staticmethod
    def register(name, hook, priority=0):
        # type: (str, Callable[[], Any], int) -> None
        if ModBE.isServer():
            if name in Callback._serverCallbacks:
                if name in Callback._serverRegistered:
                    Callback._serverRegistered[name].append(hook)
                else:
                    Callback._serverRegistered[name] = [hook]
                ModBE.log(LogType.debug, LogLevel.verbose, "ModBE", "Server Callback: '%s' registered.", name)
        if ModBE.isClient():
            if name in Callback._clientCallbacks:
                if name in Callback._clientRegistered:
                    Callback._clientRegistered[name].append(hook)
                else:
                    Callback._clientRegistered[name] = [hook]
                ModBE.log(LogType.debug, LogLevel.verbose, "ModBE", "Client Callback: '%s' registered.", name)

    @staticmethod
    def invoke(name, *args):
        # type: (str, Any) -> None
        ModBE.log(LogType.debug, LogLevel.verbose, "ModBE", "Callback: '%s'.", name)
        if name in Callback._serverRegistered:
            ModBE.log(LogType.debug, LogLevel.verbose, "ModBE", "Callback funcs: '%s'.",
                      Callback._serverRegistered[name])
            for hook in Callback._serverRegistered[name]:
                hook(*args)

    @staticmethod
    def _getCallbackNameByEngineEvent(name):
        callbacks = {}
        if ModBE.isServer():
            callbacks = Callback._serverCallbacks
        if ModBE.isClient():
            callbacks = Callback._clientCallbacks
        for key in callbacks:
            if callbacks[key] == name:
                return key


class Actor(object):
    if ModBE.isServer():
        _game = _factory.CreateGame(Level.getLevelId())
    if ModBE.isClient():
        _game = _factory.CreateGame(Level.getLevelId())

    def __new__(cls, uniqueID):
        _identifier = "minecraft:unknown"
        if ModBE.isServer():
            _identifier = _factory.CreateEngineType(uniqueID).GetEngineTypeStr()
        if ModBE.isClient():
            _identifier = _factory.CreateEngineType(uniqueID).GetEngineTypeStr()
        if _identifier == "minecraft:player":
            ModBE.log(LogType.debug, LogLevel.verbose, "ModBE", "Player: '%s' newed.", uniqueID)
            return object.__new__(Player, uniqueID)
        else:
            ModBE.log(LogType.debug, LogLevel.verbose, "ModBE", "Actor: '%s' newed.", uniqueID)
            return object.__new__(cls, uniqueID)

    def __init__(self, uniqueID):
        self._uniqueID = uniqueID or "0"
        if ModBE.isServer():
            self._type = _factory.CreateEngineType(self._uniqueID)
            self._dimension = _factory.CreateDimension(self._uniqueID)
            self._item = _factory.CreateItem(self._uniqueID)
        if ModBE.isClient():
            self._type = _factory.CreateEngineType(self._uniqueID)
        ModBE.log(LogType.debug, LogLevel.verbose, "ModBE", "Actor: '%s' initialized.", uniqueID)

    def getUniqueID(self):
        if not self.isAlive():
            ModBE.log(LogType.error, LogLevel.error, "ModBE", "Actor.getUniqueID: Actor is not alive.")
        return self._uniqueID

    def getEntityTypeId(self):
        if self.isAlive():
            return self._type.GetEngineType()
        else:
            ModBE.log(LogType.error, LogLevel.error, "ModBE", "Actor.getEntityTypeId: Actor is not alive.")
        return EntityType.Undefined

    def getActorIdentifier(self):
        if self.isAlive():
            return self._type.GetEngineTypeStr()
        else:
            ModBE.log(LogType.error, LogLevel.error, "ModBE", "Actor.getActorIdentifier: Actor is not alive.")
        return "minecraft:unknown"

    def isPlayer(self):
        return False

    def isAlive(self):
        game = None
        if self._game:
            return self._game.IsEntityAlive(self._uniqueID)
        else:
            ModBE.log(LogType.error, LogLevel.error, "ModBE", "Actor.isAlive: Cannot get Level.")
            return False

    def despawn(self):
        """
        仅服务端
        """
        if self.isAlive():
            if ModBE.isServer():
                server = extraServerApi.GetSystem("ModBE", "Server")
                server.DestroyEntity(self._uniqueID)
            else:
                ModBE.log(LogType.error, LogLevel.error, "ModBE",
                          "Actor.despawn: Client not supported for this method.")
        else:
            ModBE.log(LogType.error, LogLevel.error, "ModBE", "Actor.despawn: Actor is not alive.")

    def kill(self):
        """
        仅服务端
        """
        if self.isAlive():
            if ModBE.isServer():
                self._game.KillEntity(self._uniqueID)
            else:
                ModBE.log(LogType.error, LogLevel.error, "ModBE", "Actor.kill: Client not supported for this method.")
        else:
            ModBE.log(LogType.error, LogLevel.error, "ModBE", "Actor.kill: Actor is not alive.")

    def getDimensionId(self):
        """
        仅服务端
        """
        if self.isAlive():
            if ModBE.isServer():
                return self._dimension.GetEntityDimensionId()
            else:
                ModBE.log(LogType.error, LogLevel.error, "ModBE",
                          "Actor.getDimensionId: Client not supported for this method.")
        else:
            ModBE.log(LogType.error, LogLevel.error, "ModBE", "Actor.getDimensionId: Actor is not alive.")
        return 0

    def getCarriedItem(self):
        """
        仅服务端
        """
        if self.isAlive():
            if ModBE.isServer():
                item_dict = self._item.GetEntityItem(ItemPosType.CARRIED, 0, True)
                # item =
            else:
                ModBE.log(LogType.error, LogLevel.error, "ModBE",
                          "Actor.getCarriedItem: Client not supported for this method.")
        else:
            ModBE.log(LogType.error, LogLevel.error, "ModBE", "Actor.getCarriedItem: Actor is not alive.")


class Player(Actor):

    def __init__(self, uniqueID):
        Actor.__init__(self, uniqueID)
        ModBE.log(LogType.debug, LogLevel.verbose, "ModBE", "Player: '%s' initialized.", uniqueID)

    def isPlayer(self):
        return True


class Block(object):
    if ModBE.isServer():
        _info = _factory.CreateBlockInfo(Level.getLevelId())
        _blockState = _factory.CreateBlockState(Level.getLevelId())
    if ModBE.isClient():
        _info = _factory.CreateBlockInfo(Level.getLevelId())

    def __init__(self, blockDict):
        self._fullName = blockDict["name"]
        self._data = "aux" in blockDict and blockDict["aux"] or 0
        if ModBE.isServer():
            self._factory = extraServerApi.GetEngineCompFactory()
            self._info = self._factory.CreateBlockInfo(Level.getLevelId())
            self._blockState = self._factory.CreateBlockState(Level.getLevelId())
        if ModBE.isClient():
            self._factory = extraClientApi.GetEngineCompFactory()
            self._info = self._factory.CreateBlockInfo(Level.getLevelId())
        self._serializationId = Block.getStatesFromAux(self._fullName, self._data)

    @staticmethod
    def getStatesFromAux(name, aux):
        return Block._blockState.GetBlockStatesFromAuxValue(name, aux)

    @staticmethod
    def getAuxFromStates(name, states):
        return Block._blockState.GetBlockStatesFromAuxValue(name, states)

    def _getBlockBasicDict(self):
        """
        仅服务端
        """
        if ModBE.isServer():
            return self._info.GetBlockBasicInfo(self._fullName)
        else:
            ModBE.log(LogType.error, LogLevel.error, "ModBE",
                      "Block._getBlockBasicDict: Client not supported for this method.")

    def getBlockIdentifier(self):
        # type: () -> str
        return self._fullName

    def getData(self):
        # type: () -> int
        return self._data

    def getRenderLayer(self):
        # type: () -> int
        return self._getBlockBasicDict()["renderLayer"]

    def getDestroySpeed(self):
        # type: () -> float
        return self._getBlockBasicDict()["destroyTime"]

    def getSolid(self):
        # type: () -> bool
        return self._getBlockBasicDict()["solid"]

    def getExplosionResistance(self):
        # type: () -> float
        return self._getBlockBasicDict()["explosionResistance"]

    def getLightEmission(self):
        # type: () -> int
        return self._getBlockBasicDict()["blockLightEmission"]

    def getLight(self):
        # type: () -> int
        return self._getBlockBasicDict()["blockLightAbsorption"]

    def getMapColor(self):
        # type: () -> str
        return self._getBlockBasicDict()["mapColor"]

    def getCreativeCategory(self):
        # type: () -> int
        return self._getBlockBasicDict()["creativeCategory"]

    def getStates(self):
        return self._serializationId


# Interfaces #

class Pos(object):

    def __init__(self, x, y, z):
        self.x = x or 0
        self.y = y or 0
        self.z = z or 0

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getZ(self):
        return self.z

    def clone(self):
        return Pos(self.x, self.y, self.z)


class Tag(object):

    def __new__(cls, typeId, value=None):
        return object.__new__(Tag._typeIdToClass(typeId), value)

    def __init__(self, typeId):
        self._type = typeId
        if not self._data:
            self._data = None

    def get(self, *args):
        return self._data

    def put(self, data):
        self._data = data
        return self

    def getId(self):
        return self._type

    def clone(self):
        return Tag(self._type)

    @staticmethod
    def _typeIdToClass(typeId):
        classes = [
            EndTag,
            ByteTag,
            ShortTag,
            IntTag,
            LongTag,
            FloatTag,
            DoubleTag,
            ByteArrayTag,
            StringTag,
            ListTag,
            CompoundTag,
            IntArrayTag
        ]
        return classes[typeId]


class EndTag(Tag):

    def __new__(cls):
        return object.__new__(cls)

    def __init__(self):
        Tag.__init__(TagType.End)

    def clone(self):
        return EndTag()


class ByteTag(Tag):

    def __new__(cls, data=0):
        return object.__new__(cls, data)

    def __init__(self, data=0):
        Tag.__init__(TagType.Byte)
        self._data = data

    def clone(self):
        return ByteTag(self._data)


class ShortTag(Tag):

    def __new__(cls, data=0):
        return object.__new__(cls, data)

    def __init__(self, data=0):
        Tag.__init__(TagType.Short)
        self._data = data

    def clone(self):
        return ShortTag(self._data)


class IntTag(Tag):

    def __new__(cls, data=0):
        return object.__new__(cls, data)

    def __init__(self, data=0):
        Tag.__init__(TagType.Int)
        self._data = data

    def clone(self):
        return IntTag(self._data)


class LongTag(Tag):

    def __new__(cls, data=0):
        return object.__new__(cls, data)

    def __init__(self, data=0):
        Tag.__init__(TagType.Int64)
        self._data = data

    def clone(self):
        return LongTag(self._data)


class FloatTag(Tag):

    def __new__(cls, data=0.0):
        return object.__new__(cls, data)

    def __init__(self, data=0.0):
        Tag.__init__(TagType.Float)
        self._data = data

    def clone(self):
        return FloatTag(self._data)


class DoubleTag(Tag):

    def __new__(cls, data=0.0):
        return object.__new__(cls, data)

    def __init__(self, data=0.0):
        Tag.__init__(TagType.Double)
        self._data = data

    def clone(self):
        return DoubleTag(self._data)


class ByteArrayTag(Tag):

    def __new__(cls, data=[]):
        return object.__new__(cls, data)

    def __init__(self, data=[]):
        Tag.__init__(TagType.ByteArray)
        self._data = data

    def clone(self):
        return ByteArrayTag(self._data)


class StringTag(Tag):

    def __new__(cls, data=""):
        return object.__new__(cls, data)

    def __init__(self, data=""):
        Tag.__init__(TagType.String)
        self._data = data

    def clone(self):
        return StringTag(self._data)


class ListTag(Tag):

    def __new__(cls, tagList=[]):
        return object.__new__(cls, tagList)

    def __init__(self, tagList=[]):
        Tag.__init__(TagType.List)
        self._list = tagList
        self._listType = self.size() > 0 and self.get(0).getId() or TagType.End

    def size(self):
        return len(self._list)

    def get(self, index):
        return self._list[index]

    def add(self, tag):
        # type: (Tag) -> ListTag
        self._list.append(tag)
        if self.size() == 1:
            self._listType = self.get(0).getId()
        return self

    def put(self, data):
        self._list = data
        self._listType = self.size() > 0 and self.get(0).getId() or TagType.End
        return self

    def clone(self):
        return ListTag(self._data)


class CompoundTag(Tag):

    def __new__(cls, data={}):
        return object.__new__(cls, data)

    def __init__(self, tagDict={}):
        Tag.__init__(TagType.Compound)
        self._tags = tagDict

    def remove(self, name):
        # type: (str) -> bool
        if self.contains(name):
            del self._tags[name]
            return True
        return False

    def contains(self, name, typeId=TagType.End):
        # type: (str, int) -> bool
        if typeId <= TagType.End or typeId > TagType.IntArray:
            return name in self._tags
        else:
            return name in self._tags and self._tags[name].getId() == typeId

    def get(self, name):
        # type: (str) -> Tag | None
        if self.contains(name):
            return self._tags[name]
        return None

    def getBoolean(self, name):
        # type: (str) -> ByteTag | None
        if self.contains(name, TagType.Byte):
            return self._tags[name]
        return None

    def getByte(self, name):
        # type: (str) -> ByteTag | None
        if self.contains(name, TagType.Byte):
            return self._tags[name]
        return None

    def getShort(self, name):
        # type: (str) -> ShortTag | None
        if self.contains(name, TagType.Short):
            return self._tags[name]
        return None

    def getInt(self, name):
        # type: (str) -> IntTag | None
        if self.contains(name, TagType.Int):
            return self._tags[name]
        return None

    def getLong(self, name):
        # type: (str) -> LongTag | None
        if self.contains(name, TagType.Int64):
            return self._tags[name]
        return None

    def getFloat(self, name):
        # type: (str) -> FloatTag | None
        if self.contains(name, TagType.Float):
            return self._tags[name]
        return None

    def getDouble(self, name):
        # type: (str) -> DoubleTag | None
        if self.contains(name, TagType.Double):
            return self._tags[name]
        return None

    def getByteArray(self, name):
        # type: (str) -> ByteArrayTag | None
        if self.contains(name, TagType.ByteArray):
            return self._tags[name]
        return None

    def getString(self, name):
        # type: (str) -> StringTag | None
        if self.contains(name, TagType.String):
            return self._tags[name]
        return None

    def getList(self, name):
        # type: (str) -> ListTag | None
        if self.contains(name, TagType.List):
            return self._tags[name]
        return None

    def getCompound(self, name):
        # type: (str) -> CompoundTag | None
        if self.contains(name, TagType.Compound):
            return self._tags[name]
        return None

    def getIntArray(self, name):
        # type: (str) -> IntArrayTag | None
        if self.contains(name, TagType.IntArray):
            return self._tags[name]
        return None

    def put(self, name, tag):
        # type: (str, Tag) -> CompoundTag
        self._tags[name] = tag
        return self

    def putBoolean(self, name, value):
        # type: (str, bool) -> CompoundTag
        self._tags[name] = ByteTag(value)
        return self

    def putByte(self, name, value):
        # type: (str, int) -> CompoundTag
        self._tags[name] = ByteTag(value)
        return self

    def putShort(self, name, value):
        # type: (str, int) -> CompoundTag
        self._tags[name] = ShortTag(value)
        return self

    def putInt(self, name, value):
        # type: (str, int) -> CompoundTag
        self._tags[name] = IntTag(value)
        return self

    def putLong(self, name, value):
        # type: (str, int) -> CompoundTag
        self._tags[name] = LongTag(value)
        return self

    def putFloat(self, name, value):
        # type: (str, float) -> CompoundTag
        self._tags[name] = FloatTag(value)
        return self

    def putDouble(self, name, value):
        # type: (str, float) -> CompoundTag
        self._tags[name] = DoubleTag(value)
        return self

    def putByteArray(self, name, value):
        # type: (str, list[int]) -> CompoundTag
        self._tags[name] = ByteArrayTag(value)
        return self

    def putString(self, name, value):
        # type: (str, str) -> CompoundTag
        self._tags[name] = StringTag(value)
        return self

    def putList(self, name, value):
        # type: (str, ListTag) -> CompoundTag
        self._tags[name] = ListTag(value)
        return self

    def putCompound(self, name, value):
        # type: (str, CompoundTag) -> CompoundTag
        self._tags[name] = CompoundTag(value)
        return self

    def putIntArray(self, name, value):
        # type: (str, list[int]) -> CompoundTag
        self._tags[name] = IntArrayTag(value)
        return self

    def clear(self):
        self._tags.clear()

    def clone(self):
        return CompoundTag(self._tags)


class IntArrayTag(Tag):

    def __new__(cls, data=[]):
        return object.__new__(cls, data)

    def __init__(self, data=[]):
        Tag.__init__(TagType.IntArray)
        self._data = data

    def clone(self):
        return IntArrayTag(self._data)
