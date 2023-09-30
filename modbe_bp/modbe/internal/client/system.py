# -*- coding: utf-8 -*-

import client.extraClientApi as extraApi
import common.system.eventConf as eventConfig

from modbe.internal.module.ModBE import ModBE
from modbe.internal.enum.Log import LogLevel, LogType
from modbe.internal.module.SystemEvent import SystemEvent

from modbe.internal.module.Callback import Callback

import functools

ClientSystem = extraApi.GetClientSystemCls()
eventDict = eventConfig.SystemClientEventDict


class ModBEClientSystem(ClientSystem):

    def __init__(self, namespace, systemName):
        ModBE.log(LogType.debug, LogLevel.verbose, "ModBE", "Client Initializing.")
        ClientSystem.__init__(self, namespace, systemName)
        self._cancelEvent = False
        self.listenEngine()

    def listenEngine(self):
        ModBE.log(LogType.debug, LogLevel.verbose, "ModBE", "Client Listening.")
        for key in eventDict:
            SystemEvent.listenEngineEvent(key, self)
            ModBE.log(LogType.debug, LogLevel.verbose, "ModBE", "Client '%s' Listened.", key.split(":")[2])

    def listenForEventEngine(self, eventName, instance, func, priority = 0):
        namespace = 'Minecraft'
        systemName = 'Engine'
        self.ListenForEvent(namespace, systemName, eventName, instance, func, priority)

    def response(self, eventId, data=None):
        if data is None:
            data = {}
        # ModBE.log(LogType.debug, LogLevel.verbose, "ModBE", "Client Responsing.")
        if eventId in SystemEvent.registry:
            for func in SystemEvent.registry[eventId]:
                args = SystemEvent.wrapArgs(eventId, data)
                SystemEvent.executeFunction(func, args)
                # ModBE.log(LogType.debug, LogLevel.verbose, "ModBE", "Client '%s' Responsed.", eventId)
        if self._cancelEvent:
            if "ret" in data:
                data["ret"] = True
            elif "cancel" in data:
                data["cancel"] = True
            self._cancelEvent = False
            ModBE.log(LogType.debug, LogLevel.verbose, "ModBE", "Client '%s' Response Canceled.", eventId)

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
