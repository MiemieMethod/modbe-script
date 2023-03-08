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
        # if ModBE.isClient():
        #   client._cancelEvent = True

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
        "entityAdded": "AddEntityServerEvent"
        # (entity: Actor, entityType: str, pos: Pos, dimension: int, isBaby: bool, itemName: str, auxValue: int)
    }
    _serverRegistered = {}
    _clientCallbacks = {

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

    @staticmethod
    def invoke(name, *args):
        # type: (str, Any) -> None
        ModBE.log(LogType.debug, LogLevel.verbose, "ModBE", "Callback: '%s'.", name)
        if name in Callback._serverRegistered:
            ModBE.log(LogType.debug, LogLevel.verbose, "ModBE", "Callback funcs: '%s'.", Callback._serverRegistered[name])
            for hook in Callback._serverRegistered[name]:
                hook(*args)


class Actor:

    def __init__(self, uniqueID):
        self.uniqueID = uniqueID or 0
        if ModBE.isServer():
            self._factory = extraServerApi.GetEngineCompFactory()
            self._game = self._factory.CreateGame(Level.get())
            self._type = self._factory.CreateEngineType(self.uniqueID)
            self._dimension = self._factory.CreateDimension(self.uniqueID)
        if ModBE.isClient():
            self._factory = extraClientApi.GetEngineCompFactory()
            self._game = self._factory.CreateGame(Level.get())
            self._type = self._factory.CreateEngineType(self.uniqueID)

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
                ModBE.log(LogType.error, LogLevel.error, "ModBE", "Actor.despawn: Client not supported for this method.")
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
                ModBE.log(LogType.error, LogLevel.error, "ModBE", "Actor.getDimensionId: Client not supported for this method.")
        else:
            ModBE.log(LogType.error, LogLevel.error, "ModBE", "Actor.getDimensionId: Actor is not alive.")
        return 0


class Level:

    @staticmethod
    def get():
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
