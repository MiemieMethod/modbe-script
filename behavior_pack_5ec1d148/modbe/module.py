# -*- coding: utf-8 -*-

import mod.server.extraServerApi as extraServerApi
import mod.client.extraClientApi as extraClientApi
import common.gameConfig as GameConfig
from mod_log import logger

from modbe.enum import *

__all__ = ["Level", "ModBE", "Callback", "Dimension", "LevelChunk", "Actor", "Player", "Block", "Item", "ItemStack", "Pos", "BlockPos", "ChunkPos", "Tag", "EndTag", "ByteTag", "ShortTag", "IntTag", "LongTag", "FloatTag", "DoubleTag", "ByteArrayTag", "StringTag", "ListTag", "CompoundTag", "IntArrayTag"]


# Modules #

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
    _game = _factory.CreateGame(extraServerApi.GetLevelId())
if ModBE.isClient():
    _factory = extraClientApi.GetEngineCompFactory()
    _game = _factory.CreateGame(extraClientApi.GetLevelId())


class Level(object):

    @staticmethod
    def getLevelId():
        if ModBE.isServer():
            return extraServerApi.GetLevelId()
        if ModBE.isClient():
            return extraClientApi.GetLevelId()

    @staticmethod
    def getLocalDimension():
        """
        仅客户端
        """
        if ModBE.isClient():
            return Dimension(_game.GetCurrentDimension())
        else:
            ModBE.log(LogType.error, LogLevel.error, "ModBE",
                      "Level.getLocalDimension: Server not supported for this method.")


class Callback(object):
    _serverCallbacks = {
        "entityAdd": "AddEntityServerEvent",
        # (entity, entityType, pos, dimension, isBaby, itemName, auxValue) # type: (Actor, str, Pos, int, bool, str, int) -> None
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


class Dimension(object):
    if ModBE.isServer():
        _blockInfo = _factory.CreateBlockInfo(Level.getLevelId())
    if ModBE.isClient():
        _blockInfo = _factory.CreateBlockInfo(Level.getLevelId())

    def __init__(self, typeId):
        self._id = typeId

    def __eq__(self, other):
        if not isinstance(other, Dimension):
            return NotImplemented
        return self.getId() == other.getId()

    def __ne__(self, other):
        if not isinstance(other, Dimension):
            return NotImplemented
        return self.getId() != other.getId()

    def getId(self):
        return self._id

    def getBlock(self, blockPos):
        # type: (BlockPos) -> Block
        blockPos = blockPos.toBlockPos()
        if ModBE.isServer():
            block = self._blockInfo.GetBlockNew(blockPos.toTuple(), self.getId())
            return block is not None and Block.fromDict(block) or block
        if ModBE.isClient():
            if Level.getLocalDimension() == self:
                block = self._blockInfo.GetBlock(blockPos.toTuple())
                return block is not None and Block(block[0], block[1]) or block
            ModBE.log(LogType.error, LogLevel.error, "ModBE",
                      "Dimension.getBlock: Local player is not currently in this Dimension: %s.", self.getId())
        return None

    def getLiquidBlock(self, blockPos):
        # type: (BlockPos) -> Block
        """
        仅服务端
        """
        blockPos = blockPos.toBlockPos()
        if ModBE.isServer():
            block = self._blockInfo.GetLiquidBlock(blockPos.toTuple(), self.getId())
            return block is not None and Block.fromDict(block) or block
        if ModBE.isClient():
            ModBE.log(LogType.error, LogLevel.error, "ModBE",
                      "Dimension.getLiquidBlock: Client not supported for this method.")
        return None

    def getExtraBlock(self, blockPos):
        # type: (BlockPos) -> Block
        """
        仅服务端
        """
        blockPos = blockPos.toBlockPos()
        if ModBE.isServer():
            block = self.getBlock(blockPos)
            liquid = self.getLiquidBlock(blockPos)
            if liquid.getBlockIdentifier() != block.getBlockIdentifier():
                return liquid
        if ModBE.isClient():
            ModBE.log(LogType.error, LogLevel.error, "ModBE",
                      "Dimension.getLiquidBlock: Client not supported for this method.")
        return None

    def getChunk(self, pos):
        # type: (ChunkPos) -> LevelChunk
        return LevelChunk(self, pos)


class LevelChunk(object):

    def __init__(self, dim, pos):
        # type: (Dimension, ChunkPos) -> None
        self._dimension = dim
        self._pos = pos

    def __eq__(self, other):
        if not isinstance(other, LevelChunk):
            return NotImplemented
        return self.getDimension() == other.getDimension() and self.getPosition() == other.getPosition()

    def __ne__(self, other):
        if not isinstance(other, LevelChunk):
            return NotImplemented
        return self.getDimension() != other.getDimension() or self.getPosition() != other.getPosition()

    def getDimension(self):
        return self._dimension

    def getPosition(self):
        return self._pos

    def getBlock(self, relativePos):
        # type: (BlockPos) -> Block
        relativePos = relativePos.toBlockPos()
        return self.getDimension().getBlock(self.getPosition().toBlockPos(relativePos))

    def getLiquidBlock(self, relativePos):
        # type: (BlockPos) -> Block
        """
        仅服务端
        """
        relativePos = relativePos.toBlockPos()
        if ModBE.isServer():
            return self.getDimension().getLiquidBlock(self.getPosition().toBlockPos(relativePos))
        if ModBE.isClient():
            ModBE.log(LogType.error, LogLevel.error, "ModBE",
                      "LevelChunk.getLiquidBlock: Client not supported for this method.")
        return None

    def getExtraBlock(self, relativePos):
        # type: (BlockPos) -> Block
        """
        仅服务端
        """
        relativePos = relativePos.toBlockPos()
        if ModBE.isServer():
            return self.getDimension().getExtraBlock(self.getPosition().toBlockPos(relativePos))
        if ModBE.isClient():
            ModBE.log(LogType.error, LogLevel.error, "ModBE",
                      "LevelChunk.getExtraBlock: Client not supported for this method.")
        return None


class Actor(object):
    if ModBE.isServer():
        pass
    if ModBE.isClient():
        pass

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
        self._uniqueID = uniqueID or "-1"
        if ModBE.isServer():
            self._type = _factory.CreateEngineType(self._uniqueID)
            self._dimension = _factory.CreateDimension(self._uniqueID)
            self._item = _factory.CreateItem(self._uniqueID)
            self._pos = _factory.CreatePos(self._uniqueID)
        if ModBE.isClient():
            self._type = _factory.CreateEngineType(self._uniqueID)
            self._pos = _factory.CreatePos(self._uniqueID)
        ModBE.log(LogType.debug, LogLevel.verbose, "ModBE", "Actor: '%s' initialized.", uniqueID)

    def __eq__(self, other):
        if isinstance(other, Actor):
            return self.getUniqueID() == other.getUniqueID()
        elif isinstance(other, int):
            return int(self.getUniqueID()) == other
        elif isinstance(other, str):
            return self.getUniqueID() == other
        else:
            return NotImplemented

    def __ne__(self, other):
        if not isinstance(other, Actor) or not isinstance(other, int) or not isinstance(other, str):
            return NotImplemented
        return not self.__eq__(other)

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
        return _game.IsEntityAlive(self._uniqueID)

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
                _game.KillEntity(self._uniqueID)
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

    def getDimension(self):
        """
        仅服务端
        """
        if self.isAlive():
            if ModBE.isServer():
                return Dimension(self._dimension.GetEntityDimensionId())
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
                return ItemStack.fromDict(item_dict)
            else:
                ModBE.log(LogType.error, LogLevel.error, "ModBE",
                          "Actor.getCarriedItem: Client not supported for this method.")
        else:
            ModBE.log(LogType.error, LogLevel.error, "ModBE", "Actor.getCarriedItem: Actor is not alive.")

    def getPos(self):
        if self.isAlive():
            return Pos.fromTuple(self._pos.GetPos())
        else:
            ModBE.log(LogType.error, LogLevel.error, "ModBE", "Actor.getPos: Actor is not alive.")

    def getFeetPos(self):
        if self.isAlive():
            return Pos.fromTuple(self._pos.GetFootPos())
        else:
            ModBE.log(LogType.error, LogLevel.error, "ModBE", "Actor.getFeetPos: Actor is not alive.")


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

    def __init__(self, fullName, aux=0):
        self._fullName = fullName
        self._data = aux
        if ModBE.isServer():
            self._states = Block.getStatesFromAux(self._fullName, self._data)
            self._serializationId = CompoundTag().putString("name", self._fullName).putCompound(
                "states", CompoundTag.fromDict(self._states))
        if ModBE.isClient():
            pass

    def __eq__(self, other):
        if not isinstance(other, Block):
            return NotImplemented
        return self.getBlockIdentifier() == other.getBlockIdentifier() and self.getData() == other.getData()

    def __ne__(self, other):
        if not isinstance(other, Block):
            return NotImplemented
        return self.getBlockIdentifier() != other.getBlockIdentifier() or self.getData() != other.getData()

    @staticmethod
    def fromDict(blockDict):
        return Block(blockDict["name"], "aux" in blockDict and blockDict["aux"] or 0)

    @staticmethod
    def getStatesFromAux(name, aux):
        """
        仅服务端
        """
        if ModBE.isServer():
            return Block._blockState.GetBlockStatesFromAuxValue(name, aux)
        else:
            ModBE.log(LogType.error, LogLevel.error, "ModBE",
                      "Block.getStatesFromAux: Client not supported for this method.")

    @staticmethod
    def getAuxFromStates(name, states):
        """
        仅服务端
        """
        if ModBE.isServer():
            return Block._blockState.GetBlockStatesFromAuxValue(name, states)
        else:
            ModBE.log(LogType.error, LogLevel.error, "ModBE",
                      "Block.getAuxFromStates: Client not supported for this method.")

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
        """
        仅服务端
        """
        if ModBE.isServer():
            return self._getBlockBasicDict()["renderLayer"]
        else:
            ModBE.log(LogType.error, LogLevel.error, "ModBE",
                      "Block.getRenderLayer: Client not supported for this method.")

    def getDestroySpeed(self):
        # type: () -> float
        """
        仅服务端
        """
        if ModBE.isServer():
            return self._getBlockBasicDict()["destroyTime"]
        else:
            ModBE.log(LogType.error, LogLevel.error, "ModBE",
                      "Block.getDestroySpeed: Client not supported for this method.")

    def getSolid(self):
        # type: () -> bool
        """
        仅服务端
        """
        if ModBE.isServer():
            return self._getBlockBasicDict()["solid"]
        else:
            ModBE.log(LogType.error, LogLevel.error, "ModBE", "Block.getSolid: Client not supported for this method.")

    def getExplosionResistance(self):
        # type: () -> float
        """
        仅服务端
        """
        if ModBE.isServer():
            return self._getBlockBasicDict()["explosionResistance"]
        else:
            ModBE.log(LogType.error, LogLevel.error, "ModBE",
                      "Block.getExplosionResistance: Client not supported for this method.")

    def getLightEmission(self):
        # type: () -> int
        """
        仅服务端
        """
        if ModBE.isServer():
            return self._getBlockBasicDict()["blockLightEmission"]
        else:
            ModBE.log(LogType.error, LogLevel.error, "ModBE",
                      "Block.getLightEmission: Client not supported for this method.")

    def getLight(self):
        # type: () -> int
        """
        仅服务端
        """
        if ModBE.isServer():
            return self._getBlockBasicDict()["blockLightAbsorption"]
        else:
            ModBE.log(LogType.error, LogLevel.error, "ModBE", "Block.getLight: Client not supported for this method.")

    def getMapColor(self):
        # type: () -> str
        """
        仅服务端
        """
        if ModBE.isServer():
            return self._getBlockBasicDict()["mapColor"]
        else:
            ModBE.log(LogType.error, LogLevel.error, "ModBE",
                      "Block.getMapColor: Client not supported for this method.")

    def getCreativeCategory(self):
        # type: () -> int
        """
        仅服务端
        """
        if ModBE.isServer():
            return self._getBlockBasicDict()["creativeCategory"]
        else:
            ModBE.log(LogType.error, LogLevel.error, "ModBE",
                      "Block.getCreativeCategory: Client not supported for this method.")

    def getStates(self):
        """
        仅服务端
        """
        if ModBE.isServer():
            return self._states
        else:
            ModBE.log(LogType.error, LogLevel.error, "ModBE",
                      "Block.getStates: Client not supported for this method.")

    def hasState(self, stateType):
        """
        仅服务端
        """
        if ModBE.isServer():
            if stateType in self._states:
                return True
            return False
        else:
            ModBE.log(LogType.error, LogLevel.error, "ModBE",
                      "Block.hasState: Client not supported for this method.")

    def getState(self, stateType):
        """
        仅服务端
        """
        if ModBE.isServer():
            if self.hasState(stateType):
                return self._states[stateType]
            else:
                ModBE.log(LogType.error, LogLevel.error, "ModBE",
                          "Block.getState: Cannot find state '%s' in current Block.", stateType)
            return None
        else:
            ModBE.log(LogType.error, LogLevel.error, "ModBE",
                      "Block.getState: Client not supported for this method.")


class Item(object):
    categoryFromString = {
        "all": CreativeCategory.All,
        "construction": CreativeCategory.Construction,
        "nature": CreativeCategory.Nature,
        "equipment": CreativeCategory.Equipment,
        "items": CreativeCategory.Items,
        "commands": CreativeCategory.Commands,
        "none": CreativeCategory.Count,
        "custom": CreativeCategory.Custom
    }
    if ModBE.isServer():
        _item = _factory.CreateItem(Level.getLevelId())
        _blockInfo = _factory.CreateBlockInfo(Level.getLevelId())
    if ModBE.isClient():
        _item = _factory.CreateItem(Level.getLevelId())

    def __init__(self, fullName):
        self._fullName = fullName
        if ModBE.isServer():
            pass
        if ModBE.isClient():
            pass

    def __eq__(self, other):
        if isinstance(other, Item):
            return self.getItemIdentifier() == other.getItemIdentifier()
        elif isinstance(other, str):
            return self.getItemIdentifier() == other
        else:
            return NotImplemented

    def __ne__(self, other):
        if not isinstance(other, Actor) or not isinstance(other, str):
            return NotImplemented
        return not self.__eq__(other)

    def _getItemBasicDict(self):
        return self._item.GetItemBasicInfo(self._fullName)

    def _getBlockBasicDict(self):
        """
        仅服务端
        """
        if ModBE.isServer():
            return self._blockInfo.GetBlockBasicInfo(self._fullName)
        else:
            ModBE.log(LogType.error, LogLevel.error, "ModBE",
                      "Item._getBlockBasicDict: Client not supported for this method.")

    def isBlock(self):
        """
        仅服务端
        """
        if ModBE.isServer():
            return self._getBlockBasicDict() is not None
        else:
            ModBE.log(LogType.error, LogLevel.error, "ModBE", "Item.isBlock: Client not supported for this method.")

    def getItemIdentifier(self):
        return self._fullName

    def getAttackDamage(self):
        return self._getItemBasicDict()["weaponDamage"]

    def getMaxDamage(self):
        return self._getItemBasicDict()["maxDurability"]

    def getCreativeCategory(self):
        return self.categoryFromString[self._getItemBasicDict()["itemCategory"]]

    def getTierLevel(self):
        return self._getItemBasicDict()["itemTierLevel"]

    def getArmorValue(self):
        return self._getItemBasicDict()["armorDefense"]


class ItemStack(object):
    TAG_ENCHANTS = "ench"
    if ModBE.isServer():
        _itemComp = _factory.CreateItem(Level.getLevelId())
    if ModBE.isClient():
        _itemComp = _factory.CreateItem(Level.getLevelId())

    def __init__(self, fullName, count=1, aux=0, _userData=None):
        self._item = Item(fullName)
        self._aux = aux
        self._count = count
        self._userData = CompoundTag.fromObject(_userData)
        if ModBE.isServer():
            self._block = self._item.isBlock() and Block(fullName, aux) or None
        if ModBE.isClient():
            pass

    def __eq__(self, other):
        if not isinstance(other, ItemStack):
            return NotImplemented
        return self.getItem() == other.getItem() and self.get() == other.get() and self.getAuxValue() == other.getAuxValue() and self.getUserData() == other.getUserData()

    def __ne__(self, other):
        if not isinstance(other, ItemStack):
            return NotImplemented
        return self.getItem() != other.getItem() or self.get() != other.get() or self.getAuxValue() != other.getAuxValue() or self.getUserData() != other.getUserData()

    @staticmethod
    def fromDict(itemDict):
        identifier = itemDict["newItemName"]
        aux = itemDict["newAuxValue"]
        count = itemDict["count"]
        _userData = "userData" in itemDict and itemDict["userData"] or None
        return ItemStack(identifier, count, aux, _userData)

    def _getItemBasicDict(self):
        return self._itemComp.GetItemBasicInfo(self.getItemIdentifier(), self.getAuxValue(), self.isEnchanted())

    def getItem(self):
        return self._item

    def isBlock(self):
        """
        仅服务端
        """
        if ModBE.isServer():
            return self.getItem().isBlock()
        else:
            ModBE.log(LogType.error, LogLevel.error, "ModBE",
                      "ItemStack.isBlock: Client not supported for this method.")

    def getBlock(self):
        if hasattr(self, "_block"):
            return self._block
        return None

    def get(self):
        return self._count

    def set(self, inCount):
        if inCount <= self.getMaxStackSize():
            self._count = inCount >= 0 and inCount or 0
        else:
            ModBE.log(LogType.error, LogLevel.error, "ModBE",
                      "ItemStack.set: inCount > maxStackSize.")

    def add(self, addCount):
        self.set(self.get() + addCount)

    def remove(self, removeCount):
        self.set(self.get() - removeCount)

    def increase(self):
        self.add(1)

    def decrease(self):
        self.remove(1)

    def getUserData(self):
        return self._userData

    def getItemIdentifier(self):
        return self.getItem().getItemIdentifier()

    def getAuxValue(self):
        return self._aux

    def isEnchanted(self):
        return self.getUserData().contains(self.TAG_ENCHANTS)

    def getIdAux(self):
        return self._getItemBasicDict()["id_aux"]

    def getAttackDamage(self):
        return self._getItemBasicDict()["weaponDamage"]

    def getMaxDamage(self):
        return self._getItemBasicDict()["maxDurability"]

    def getCreativeCategory(self):
        return Item.categoryFromString[self._getItemBasicDict()["itemCategory"]]

    def getTierLevel(self):
        return self._getItemBasicDict()["itemTierLevel"]

    def getArmorValue(self):
        return self._getItemBasicDict()["armorDefense"]

    def getMaxStackSize(self):
        return self._getItemBasicDict()["maxStackSize"]

    def getDamageValue(self):
        return self.getUserData().getInt("Damage")

    def isFullStack(self):
        return self.get() >= self.getMaxStackSize()

    def isEmptyStack(self):
        return self.get() <= 0


# Interfaces #


class Pos(object):

    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        if not isinstance(other, Pos):
            return NotImplemented
        return Pos(self.getX() + other.getX(), self.getY() + other.getY(), self.getZ() + other.getZ())

    def __sub__(self, other):
        if not isinstance(other, Pos):
            return NotImplemented
        return Pos(self.getX() - other.getX(), self.getY() - other.getY(), self.getZ() - other.getZ())

    def __mul__(self, other):
        if not isinstance(other, Pos):
            return NotImplemented
        return self.getX() * other.getX() + self.getY() * other.getY() + self.getZ() * other.getZ()

    def __eq__(self, other):
        if not isinstance(other, Pos):
            return NotImplemented
        return self.getX() == other.getX() and self.getY() == other.getY() and self.getZ() == other.getZ()

    def __ne__(self, other):
        if not isinstance(other, Pos):
            return NotImplemented
        return self.getX() != other.getX() or self.getY() != other.getY() or self.getZ() != other.getZ()

    @staticmethod
    def fromTuple(_tuple):
        return Pos(_tuple[0], _tuple[1], _tuple[2])

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getZ(self):
        return self.z

    def toTuple(self):
        return self.x, self.y, self.z

    def toBlockPos(self):
        if isinstance(self, Pos) and not isinstance(self, BlockPos):
            return BlockPos(int(self.x), int(self.y), int(self.z))
        return self

    def clone(self):
        return Pos(self.x, self.y, self.z)


class BlockPos(Pos):

    def __init__(self, x=0, y=0, z=0):
        object.__init__(self)
        self.x = int(x)
        self.y = int(y)
        self.z = int(z)

    @staticmethod
    def fromTuple(_tuple):
        return BlockPos(_tuple[0], _tuple[1], _tuple[2])

    def addAndSet(self, other):
        self.x += other.getX()
        self.y += other.getY()
        self.z += other.getZ()
        return self

    def neighbor(self, facing):
        facingDirection = [
            BlockPos(0, -1, 0),
            BlockPos(0, 1, 0),
            BlockPos(0, 0, -1),
            BlockPos(0, 0, 1),
            BlockPos(-1, 0, 0),
            BlockPos(1, 0, 0)
        ]
        return self + facingDirection[facing]

    def toChunkPos(self):
        return ChunkPos(self.getX() >> 4, self.getZ() >> 4)


class ChunkPos(object):

    def __init__(self, x=0, z=0):
        self.x = int(x)
        self.z = int(z)

    def __add__(self, other):
        if not isinstance(other, Pos):
            return NotImplemented
        return Pos(self.getX() + other.getX(), self.getZ() + other.getZ())

    def __sub__(self, other):
        if not isinstance(other, Pos):
            return NotImplemented
        return Pos(self.getX() - other.getX(), self.getZ() - other.getZ())

    def __eq__(self, other):
        if not isinstance(other, Pos):
            return NotImplemented
        return self.getX() == other.getX() and self.getZ() == other.getZ()

    def __ne__(self, other):
        if not isinstance(other, Pos):
            return NotImplemented
        return self.getX() != other.getX() or self.getZ() != other.getZ()

    def getX(self):
        return self.x

    def getZ(self):
        return self.z

    def toBlockPos(self, relativePos=BlockPos()):
        relativePos = relativePos.toBlockPos()
        return BlockPos(self.getX() << 4 + relativePos.getX(), relativePos.getY(),
                        self.getZ() << 4 + relativePos.getZ())

    def clone(self):
        return Pos(self.x, self.z)


class Tag(object):

    def __new__(cls, typeId, value=None):
        return object.__new__(Tag._typeIdToClass(typeId), value)

    def __init__(self, typeId):
        self._type = typeId
        if not hasattr(self, "_data"):
            self._data = None

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

    def get(self, *args):
        return self._data

    def put(self, *args):
        self._data = args[0]
        return self

    def getId(self):
        return self._type

    def clone(self):
        return Tag(self._type)


class EndTag(Tag):

    def __new__(cls):
        return object.__new__(cls)

    def __init__(self):
        Tag.__init__(self, TagType.End)

    def __eq__(self, other):
        if not isinstance(other, Tag):
            return NotImplemented
        if not isinstance(other, EndTag):
            return False
        return True

    def __ne__(self, other):
        if not isinstance(other, Tag):
            return NotImplemented
        if not isinstance(other, EndTag):
            return False
        return True

    def clone(self):
        return EndTag()


class ByteTag(Tag):

    def __new__(cls, data=0):
        return object.__new__(cls, data)

    def __init__(self, data=0):
        Tag.__init__(self, TagType.Byte)
        self._data = data

    def __eq__(self, other):
        if not isinstance(other, Tag):
            return NotImplemented
        if not isinstance(other, ByteTag):
            return False
        return self.get() == other.get()

    def __ne__(self, other):
        if not isinstance(other, Tag):
            return NotImplemented
        if not isinstance(other, ByteTag):
            return False
        return self.get() != other.get()

    def clone(self):
        return ByteTag(self._data)


class ShortTag(Tag):

    def __new__(cls, data=0):
        return object.__new__(cls, data)

    def __init__(self, data=0):
        Tag.__init__(self, TagType.Short)
        self._data = data

    def __eq__(self, other):
        if not isinstance(other, Tag):
            return NotImplemented
        if not isinstance(other, ShortTag):
            return False
        return self.get() == other.get()

    def __ne__(self, other):
        if not isinstance(other, Tag):
            return NotImplemented
        if not isinstance(other, ShortTag):
            return False
        return self.get() != other.get()

    def clone(self):
        return ShortTag(self._data)


class IntTag(Tag):

    def __new__(cls, data=0):
        return object.__new__(cls, data)

    def __init__(self, data=0):
        Tag.__init__(self, TagType.Int)
        self._data = data

    def __eq__(self, other):
        if not isinstance(other, Tag):
            return NotImplemented
        if not isinstance(other, IntTag):
            return False
        return self.get() == other.get()

    def __ne__(self, other):
        if not isinstance(other, Tag):
            return NotImplemented
        if not isinstance(other, IntTag):
            return False
        return self.get() != other.get()

    def clone(self):
        return IntTag(self._data)


class LongTag(Tag):

    def __new__(cls, data=0):
        return object.__new__(cls, data)

    def __init__(self, data=0):
        Tag.__init__(self, TagType.Int64)
        self._data = data

    def __eq__(self, other):
        if not isinstance(other, Tag):
            return NotImplemented
        if not isinstance(other, LongTag):
            return False
        return self.get() == other.get()

    def __ne__(self, other):
        if not isinstance(other, Tag):
            return NotImplemented
        if not isinstance(other, LongTag):
            return False
        return self.get() != other.get()

    def clone(self):
        return LongTag(self._data)


class FloatTag(Tag):

    def __new__(cls, data=0.0):
        return object.__new__(cls, data)

    def __init__(self, data=0.0):
        Tag.__init__(self, TagType.Float)
        self._data = data

    def __eq__(self, other):
        if not isinstance(other, Tag):
            return NotImplemented
        if not isinstance(other, FloatTag):
            return False
        return self.get() == other.get()

    def __ne__(self, other):
        if not isinstance(other, Tag):
            return NotImplemented
        if not isinstance(other, FloatTag):
            return False
        return self.get() != other.get()

    def clone(self):
        return FloatTag(self._data)


class DoubleTag(Tag):

    def __new__(cls, data=0.0):
        return object.__new__(cls, data)

    def __init__(self, data=0.0):
        Tag.__init__(self, TagType.Double)
        self._data = data

    def __eq__(self, other):
        if not isinstance(other, Tag):
            return NotImplemented
        if not isinstance(other, DoubleTag):
            return False
        return self.get() == other.get()

    def __ne__(self, other):
        if not isinstance(other, Tag):
            return NotImplemented
        if not isinstance(other, DoubleTag):
            return False
        return self.get() != other.get()

    def clone(self):
        return DoubleTag(self._data)


class ByteArrayTag(Tag):

    def __new__(cls, data=None):
        if data is None:
            data = []
        return object.__new__(cls, data)

    def __init__(self, data=None):
        Tag.__init__(self, TagType.ByteArray)
        if data is None:
            data = []
        self._data = data

    def __eq__(self, other):
        if not isinstance(other, Tag):
            return NotImplemented
        if not isinstance(other, ByteArrayTag):
            return False
        return self.get() == other.get()

    def __ne__(self, other):
        if not isinstance(other, Tag):
            return NotImplemented
        if not isinstance(other, ByteArrayTag):
            return False
        return self.get() != other.get()

    def clone(self):
        return ByteArrayTag(self._data)


class StringTag(Tag):

    def __new__(cls, data=""):
        return object.__new__(cls, data)

    def __init__(self, data=""):
        Tag.__init__(self, TagType.String)
        self._data = data

    def __eq__(self, other):
        if not isinstance(other, Tag):
            return NotImplemented
        if not isinstance(other, StringTag):
            return False
        return self.get() == other.get()

    def __ne__(self, other):
        if not isinstance(other, Tag):
            return NotImplemented
        if not isinstance(other, StringTag):
            return False
        return self.get() != other.get()

    def clone(self):
        return StringTag(self._data)


class ListTag(Tag):

    def __new__(cls, tagList=None):
        if tagList is None:
            tagList = []
        return object.__new__(cls, tagList)

    def __init__(self, tagList=None):
        Tag.__init__(self, TagType.List)
        if tagList is None:
            tagList = []
        self._list = tagList
        self._listType = self.size() > 0 and self.get(0).getId() or TagType.End

    def __eq__(self, other):
        if not isinstance(other, Tag):
            return NotImplemented
        if not isinstance(other, ListTag):
            return False
        if self.size() == other.size():
            for i in range(0, self.size() - 1):
                if self.get(i) != other.get(i):
                    return False
            return True
        return False

    def __ne__(self, other):
        if not isinstance(other, Tag):
            return NotImplemented
        return not self.__eq__(other)

    @staticmethod
    def fromList(rawList, _list=None):
        """
        Python限制，无法正确设置非布尔值形态的Byte、Short、Long、Double作为元素，请手动设置
        """
        if _list is None:
            _list = ListTag()
        if rawList is None or len(rawList) == 0:
            return _list
        else:
            for element in rawList:
                if isinstance(element, int):
                    _list.add(IntTag(element))
                elif isinstance(element, float):
                    _list.add(FloatTag(element))
                elif isinstance(element, str):
                    _list.add(StringTag(element))
                elif isinstance(element, bool):
                    _list.add(ByteTag(element and 1 or 0))
                elif isinstance(element, list):
                    if len(element) > 0 and isinstance(element[0], int):
                        _list.add(ByteArrayTag(element))
                    else:
                        _list.add(ListTag.fromList(element))
                elif isinstance(element, dict):
                    _list.add(CompoundTag.fromDict(element))
                else:
                    ModBE.log(LogType.error, LogLevel.error, "ModBE",
                              "ListTag.fromList: Unsupported Type: '%s' added to a ListTag.", element)
            return _list

    @staticmethod
    def fromObject(rawList, _list=None):
        if _list is None:
            _list = ListTag()
        if rawList is None or len(rawList) == 0:
            return _list
        else:
            for element in rawList:
                if isinstance(element, list):
                    _list.add(ListTag.fromObject(element))
                elif isinstance(element, dict):
                    if "__type__" in element:
                        typeId = element["__type__"]
                        _list.add(Tag._typeIdToClass(typeId)(element["__value__"]))
                    else:
                        _list.add(CompoundTag.fromObject(element))
                else:
                    ModBE.log(LogType.error, LogLevel.error, "ModBE",
                              "ListTag.fromObject: Unsupported Type: '%s' added to a ListTag.", element)
            return _list

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
        return ListTag(self._list)


class CompoundTag(Tag):

    def __new__(cls, data=None):
        if data is None:
            data = {}
        return object.__new__(cls, data)

    def __init__(self, tagDict=None):
        Tag.__init__(self, TagType.Compound)
        if tagDict is None:
            tagDict = {}
        self._tags = tagDict

    def __eq__(self, other):
        if not isinstance(other, Tag):
            return NotImplemented
        if not isinstance(other, CompoundTag):
            return False
        for key in self.getTags():
            if not other.contains(key):
                return False
            if self.get(key) != other.get(key):
                return False
        return True

    def __ne__(self, other):
        if not isinstance(other, Tag):
            return NotImplemented
        return not self.__eq__(other)

    @staticmethod
    def fromDict(rawDict, _compound=None):
        """
        Python限制，无法正确设置非布尔值形态的Byte、Short、Long、Double和IntArray，请手动设置
        """
        if _compound is None:
            _compound = CompoundTag()
        if rawDict is None or len(rawDict) == 0:
            return _compound
        for key in rawDict:
            value = rawDict[key]
            if isinstance(value, int):
                _compound.putInt(key, value)
            elif isinstance(value, float):
                _compound.putFloat(key, value)
            elif isinstance(value, str):
                _compound.putString(key, value)
            elif isinstance(value, bool):
                _compound.putBoolean(key, value)
            elif isinstance(value, list):
                if len(value) > 0 and isinstance(value[0], int):
                    _compound.putByteArray(key, value)
                else:
                    _compound.putList(key, ListTag.fromList(value))
            elif isinstance(value, dict):
                _compound.putCompound(key, CompoundTag.fromDict(value))
            else:
                ModBE.log(LogType.error, LogLevel.error, "ModBE",
                          "CompoundTag.fromDict: Unsupported Type: '%s' added to a CompoundTag key: '%s'.", value, key)
        return _compound

    @staticmethod
    def fromObject(rawObject, _compound=None):
        if _compound is None:
            _compound = CompoundTag()
        if rawObject is None or len(rawObject) == 0:
            return _compound
        for key in rawObject:
            value = rawObject[key]
            if isinstance(value, list):
                _compound.putList(key, ListTag.fromObject(value))
            elif isinstance(value, dict):
                if "__type__" in value:
                    typeId = value["__type__"]
                    _compound.put(key, Tag._typeIdToClass(typeId)(value["__value__"]))
                else:
                    _compound.putCompound(key, CompoundTag.fromObject(value))
            else:
                ModBE.log(LogType.error, LogLevel.error, "ModBE",
                          "CompoundTag.fromObject: Unsupported Type: '%s' added to a CompoundTag key: '%s'.", value,
                          key)
        return _compound

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

    def getTags(self):
        # type: () -> dict
        return self._tags

    def getBoolean(self, name):
        # type: (str) -> int
        if self.contains(name, TagType.Byte):
            return self._tags[name].get()
        return False

    def getByte(self, name):
        # type: (str) -> int
        if self.contains(name, TagType.Byte):
            return self._tags[name].get()
        return 0

    def getShort(self, name):
        # type: (str) -> int
        if self.contains(name, TagType.Short):
            return self._tags[name].get()
        return 0

    def getInt(self, name):
        # type: (str) -> int
        if self.contains(name, TagType.Int):
            return self._tags[name].get()
        return 0

    def getLong(self, name):
        # type: (str) -> int
        if self.contains(name, TagType.Int64):
            return self._tags[name].get()
        return 0

    def getFloat(self, name):
        # type: (str) -> float
        if self.contains(name, TagType.Float):
            return self._tags[name].get()
        return 0.0

    def getDouble(self, name):
        # type: (str) -> float
        if self.contains(name, TagType.Double):
            return self._tags[name].get()
        return 0.0

    def getByteArray(self, name):
        # type: (str) -> list[int] | None
        if self.contains(name, TagType.ByteArray):
            return self._tags[name].get()
        return None

    def getString(self, name):
        # type: (str) -> str | None
        if self.contains(name, TagType.String):
            return self._tags[name].get()
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
        # type: (str) -> list[int] | None
        if self.contains(name, TagType.IntArray):
            return self._tags[name].get()
        return None

    def getBooleanTag(self, name):
        # type: (str) -> ByteTag | None
        if self.contains(name, TagType.Byte):
            return self._tags[name]
        return None

    def getByteTag(self, name):
        # type: (str) -> ByteTag | None
        if self.contains(name, TagType.Byte):
            return self._tags[name]
        return None

    def getShortTag(self, name):
        # type: (str) -> ShortTag | None
        if self.contains(name, TagType.Short):
            return self._tags[name]
        return None

    def getIntTag(self, name):
        # type: (str) -> IntTag | None
        if self.contains(name, TagType.Int):
            return self._tags[name]
        return None

    def getLongTag(self, name):
        # type: (str) -> LongTag | None
        if self.contains(name, TagType.Int64):
            return self._tags[name]
        return None

    def getFloatTag(self, name):
        # type: (str) -> FloatTag | None
        if self.contains(name, TagType.Float):
            return self._tags[name]
        return None

    def getDoubleTag(self, name):
        # type: (str) -> DoubleTag | None
        if self.contains(name, TagType.Double):
            return self._tags[name]
        return None

    def getByteArrayTag(self, name):
        # type: (str) -> ByteArrayTag | None
        if self.contains(name, TagType.ByteArray):
            return self._tags[name]
        return None

    def getStringTag(self, name):
        # type: (str) -> StringTag | None
        if self.contains(name, TagType.String):
            return self._tags[name]
        return None

    def getIntArrayTag(self, name):
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
        self._tags[name] = ByteTag(value and 1 or 0)
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
        self._tags[name] = value
        return self

    def putCompound(self, name, value):
        # type: (str, CompoundTag) -> CompoundTag
        self._tags[name] = value
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

    def __new__(cls, data=None):
        if data is None:
            data = []
        return object.__new__(cls, data)

    def __init__(self, data=None):
        Tag.__init__(self, TagType.IntArray)
        if data is None:
            data = []
        self._data = data

    def __eq__(self, other):
        if not isinstance(other, Tag):
            return NotImplemented
        if not isinstance(other, IntArrayTag):
            return False
        return self.get() == other.get()

    def __ne__(self, other):
        if not isinstance(other, Tag):
            return NotImplemented
        if not isinstance(other, IntArrayTag):
            return False
        return self.get() != other.get()

    def clone(self):
        return IntArrayTag(self._data)
