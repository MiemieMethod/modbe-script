# -*- coding: utf-8 -*-


import mod.server.extraServerApi as extraServerApi
import mod.client.extraClientApi as extraClientApi
import common.gameConfig as GameConfig
from mod_log import logger

from modbe.enum import *

__all__ = ["ModBE", "Callback", "Actor", "Pos"]


# Modules #

class ModBE:

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


class Callback:
    _serverCallbacks = {
        "entityAdd": "AddEntityServerEvent",
        # (entity, entityType, pos, dimension, isBaby, itemName, auxValue) # type: (Actor, str, Pos, int, bool, str, int) -> None
        "itemUse": "ServerItemUseEvent",  # (entity, oldName, oldAux) # type: (Actor, str, int) -> None
        "itemTryUse": "ServerItemTryUseEvent"  # (entity, oldName, oldAux, itemStack) # type: (Actor, str, int, ItemStack) -> None
    }
    _serverRegistered = {}
    _clientCallbacks = {
        "itemUse": "ClientItemUseEvent",  # (entity, oldName, oldAux, itemStack) # type: (Actor, str, int, ItemStack) -> None
        "itemTryUse": "ClientItemTryUseEvent"  # (entity, oldName, oldAux, itemStack) # type: (Actor, str, int, ItemStack) -> None
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
    def getCallbackNameByEngineEvent(name):
        callbacks = {}
        if ModBE.isServer():
            callbacks = Callback._serverCallbacks
        if ModBE.isClient():
            callbacks = Callback._clientCallbacks
        for key in callbacks:
            if callbacks[key] == name:
                return key


class Actor:

    def __new__(cls, uniqueID):
        _identifier = "minecraft:unknown"
        if ModBE.isServer():
            _identifier = extraServerApi.GetEngineCompFactory().CreateEngineType(uniqueID).GetEngineTypeStr()
        if ModBE.isClient():
            _identifier = extraClientApi.GetEngineCompFactory().CreateEngineType(uniqueID).GetEngineTypeStr()
        if _identifier == "minecraft:player":
            return Player(uniqueID)

    def __init__(self, uniqueID):
        self.uniqueID = uniqueID or "0"
        if ModBE.isServer():
            self._factory = extraServerApi.GetEngineCompFactory()
            self._game = self._factory.CreateGame(Level.getLevelId())
            self._type = self._factory.CreateEngineType(self.uniqueID)
            self._dimension = self._factory.CreateDimension(self.uniqueID)
            self._item = self._factory.CreateItem(self.uniqueID)
        if ModBE.isClient():
            self._factory = extraClientApi.GetEngineCompFactory()
            self._game = self._factory.CreateGame(Level.getLevelId())
            self._type = self._factory.CreateEngineType(self.uniqueID)
        ModBE.log(LogType.debug, LogLevel.verbose, "ModBE", "Actor: '%s' initialized.", uniqueID)

    def getUniqueID(self):
        if not self.isAlive():
            ModBE.log(LogType.error, LogLevel.error, "ModBE", "Actor.getUniqueID: Actor is not alive.")
        return self.uniqueID

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

    def isAlive(self):
        game = None
        if self._game:
            return self._game.IsEntityAlive(self.uniqueID)
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
                server.DestroyEntity(self.uniqueID)
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
                self._game.KillEntity(self.uniqueID)
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


class Level:

    @staticmethod
    def getLevelId():
        if ModBE.isServer():
            return extraServerApi.GetLevelId()
        if ModBE.isClient():
            return extraClientApi.GetLevelId()


# Interfaces #

class Pos:

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
