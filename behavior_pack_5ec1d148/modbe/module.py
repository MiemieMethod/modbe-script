# -*- coding: utf-8 -*-

import mod.server.extraServerApi as extraServerApi
import mod.client.extraClientApi as extraClientApi
import common.gameConfig as gameConfig


class ModBE:

    @staticmethod
    def preventDefault():
        if gameConfig.IsServer():
            server = extraServerApi.GetSystem("ModBE", "Server")
            server._cancelEvent = True
        # if gameConfig.IsClient():
        #   client._cancelEvent = True


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
        if gameConfig.IsServer():
            if name in Callback._serverCallbacks:
                if name in Callback._serverRegistered:
                    Callback._serverRegistered[name].append(hook)
                else:
                    Callback._serverRegistered[name] = [hook]

    @staticmethod
    def invoke(name, *args):
        # type: (str, Any) -> None
        print("[ModBE][Verbose] Callback:", name, ".")
        if name in Callback._serverRegistered:
            print("[ModBE][Verbose] Callback funcs:", Callback._serverRegistered[name], ".")
            for hook in Callback._serverRegistered[name]:
                hook(*args)


class Actor:

    def __init__(self, uniqueID):
        self.uniqueID = uniqueID or 0

    def getUniqueID(self):
        return self.uniqueID


class Pos:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getZ(self):
        return self.z

    def clone(self):
        return Pos(self.x, self.y, self.z)
