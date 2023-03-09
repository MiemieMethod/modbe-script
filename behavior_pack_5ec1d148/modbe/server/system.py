# -*- coding: utf-8 -*-

import server.extraServerApi as extraApi
import common.system.eventConf as eventConfig

import modbe.server.event.response as EventResponse
from modbe.module import ModBE, Level
from modbe.enum import *

ServerSystem = extraApi.GetServerSystemCls()
eventDict = eventConfig.SystemServerEventDict


class ModBEServerSystem(ServerSystem):

    def __init__(self, namespace, systemName):
        ModBE.log(LogType.debug, LogLevel.verbose, "ModBE", "Server Initializing.")
        ServerSystem.__init__(self, namespace, systemName)
        self._cancelEvent = False
        self.listen()

    def listen(self):
        ModBE.log(LogType.debug, LogLevel.verbose, "ModBE", "Server Listening.")
        item = extraApi.GetEngineCompFactory().CreateItem(Level.getLevelId())
        for key in eventDict:
            if hasattr(self, "on" + key.split(":")[2]):
                item.GetUserDataInEvent(key.split(":")[2])
                self.ListenForEventEngine(key.split(":")[2], self, getattr(self, "on" + key.split(":")[2]))
                ModBE.log(LogType.debug, LogLevel.verbose, "ModBE", "Server '%s' Listened.", key.split(":")[2])

    def response(self, eventId, args):
        ModBE.log(LogType.debug, LogLevel.verbose, "ModBE", "Server Responsing.")
        if hasattr(EventResponse, "on" + eventId):
            getattr(EventResponse, "on" + eventId)(args)
            ModBE.log(LogType.debug, LogLevel.verbose, "ModBE", "Server '%s' Responsed.", eventId)
        if self._cancelEvent:
            if "ret" in args:
                args["ret"] = True
            elif "cancel" in args:
                args["cancel"] = True
            self._cancelEvent = False
            ModBE.log(LogType.debug, LogLevel.verbose, "ModBE", "Server '%s' Response Canceled.", eventId)

    def onAddEntityServerEvent(self, args):
        self.response("AddEntityServerEvent", args)

    def onServerItemTryUseEvent(self, args):
        self.response("ServerItemTryUseEvent", args)

    def onServerItemUseEvent(self, args):
        self.response("ServerItemUseEvent", args)

    def Update(self):
        """
        do update for every event in this method
        """
        pass

    def DestroyEvents(self):
        pass

    def Destroy(self):
        """
        do remove for every event in this method
        """
        pass
