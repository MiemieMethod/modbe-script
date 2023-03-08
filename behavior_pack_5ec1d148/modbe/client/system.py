# -*- coding: utf-8 -*-

import client.extraClientApi as extraApi
import common.system.eventConf as eventConfig

import modbe.client.event.response as EventResponse
from modbe.module import ModBE
from modbe.enum import *

ClientSystem = extraApi.GetClientSystemCls()
eventDict = eventConfig.SystemClientEventDict


class ModBEClientSystem(ClientSystem):

    def __init__(self, namespace, systemName):
        ModBE.log(LogType.debug, LogLevel.verbose, "ModBE", "Client Initializing.")
        ClientSystem.__init__(self, namespace, systemName)
        self._cancelEvent = False
        self.listen()

    def listen(self):
        ModBE.log(LogType.debug, LogLevel.verbose, "ModBE", "Client Listening.")
        for key in eventDict:
            if hasattr(self, "on" + key.split(":")[2]):
                self.ListenForEventEngine(key.split(":")[2], self, getattr(self, "on" + key.split(":")[2]))
                ModBE.log(LogType.debug, LogLevel.verbose, "ModBE", "Client '%s' Listened.", key.split(":")[2])

    def response(self, eventId, args):
        ModBE.log(LogType.debug, LogLevel.verbose, "ModBE", "Client Responsing.")
        if hasattr(EventResponse, "on" + eventId):
            getattr(EventResponse, "on" + eventId)(args)
            ModBE.log(LogType.debug, LogLevel.verbose, "ModBE", "Client '%s' Responsed.", eventId)
        if self._cancelEvent:
            if hasattr(args, "ret"):
                args["ret"] = True
            elif hasattr(args, "cancel"):
                args["cancel"] = True
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
