# -*- coding: utf-8 -*-

import server.extraServerApi as extraApi
import common.system.eventConf as eventConfig

import modbe.server.event.response as eventResponce
from modbe.module import ModBE
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
        for key in eventDict:
            if hasattr(self, "on" + key.split(":")[2]):
                self.ListenForEventEngine(key.split(":")[2], self, getattr(self, "on" + key.split(":")[2]))
                ModBE.log(LogType.debug, LogLevel.verbose, "ModBE", "Server '%s' Listened.", key.split(":")[2])

    def response(self, eventId, args):
        ModBE.log(LogType.debug, LogLevel.verbose, "ModBE", "Server Responsing.")
        if hasattr(eventResponce, "on" + eventId):
            getattr(eventResponce, "on" + eventId)(args)
            ModBE.log(LogType.debug, LogLevel.verbose, "ModBE", "Server '%s' Responsed.", eventId)
        if self._cancelEvent:
            if hasattr(args, "ret"):
                args["ret"] = True
            elif hasattr(args, "cancel"):
                args["cancel"] = True
            self._cancelEvent = False
            ModBE.log(LogType.debug, LogLevel.verbose, "ModBE", "Server '%s' Response Canceled.", eventId)

    def onAddEntityServerEvent(self, args):
        self.response("AddEntityServerEvent", args)

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
