# -*- coding: utf-8 -*-

import server.extraServerApi as extraApi
import common.system.eventConf as eventConfig

from modbe.internal.module.ModBE import ModBE
from modbe.internal.module.SystemEvent import SystemEvent
from modbe.internal.module.Level import Level
from modbe.internal.enum.LogLevel import LogLevel
from modbe.internal.enum.LogType import LogType

import functools

ServerSystem = extraApi.GetServerSystemCls()
eventDict = eventConfig.SystemServerEventDict

class ModBEServerSystem(ServerSystem):

    def __init__(self, namespace, systemName):
        ModBE.log(LogType.debug, LogLevel.verbose, "ModBE", "Server Initializing.")
        ServerSystem.__init__(self, namespace, systemName)
        self._cancelEvent = False
        self.listenEngine()

    def listenEngine(self):
        ModBE.log(LogType.debug, LogLevel.verbose, "ModBE", "Server Listening.")
        item = extraApi.GetEngineCompFactory().CreateItem(Level.getLevelId())
        for key in eventDict:
            namespacedTriple = SystemEvent.namespacedIdToTriple(key)
            setattr(self, "on" + namespacedTriple[2], functools.partial(self.response, key))
            getattr(self, "on" + namespacedTriple[2]).__name__ = "on" + namespacedTriple[2]
            item.GetUserDataInEvent(namespacedTriple[2])
            self.ListenForEventEngine(namespacedTriple[2], self, getattr(self, "on" + namespacedTriple[2]))
            ModBE.log(LogType.debug, LogLevel.verbose, "ModBE", "Server '%s' Listened.", namespacedTriple[2])

    def response(self, eventId, data=None):
        if data is None:
            data = {}
        # ModBE.log(LogType.debug, LogLevel.verbose, "ModBE", "Server Responsing.")
        if eventId in SystemEvent.registry:
            for func in SystemEvent.registry[eventId]:
                args = SystemEvent.wrapArgs(eventId, data)
                SystemEvent.executeFunction(func, args)
                # ModBE.log(LogType.debug, LogLevel.verbose, "ModBE", "Server '%s' Responsed.", eventId)
        if self._cancelEvent:
            if "ret" in data:
                data["ret"] = True
            elif "cancel" in data:
                data["cancel"] = True
            self._cancelEvent = False
            ModBE.log(LogType.debug, LogLevel.verbose, "ModBE", "Server '%s' Response Canceled.", eventId)

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
