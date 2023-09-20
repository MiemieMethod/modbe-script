# -*- coding: utf-8 -*-

import client.extraClientApi as extraApi
import common.system.eventConf as eventConfig

from modbe.internal.module.ModBE import ModBE
from modbe.internal.enum.Log import LogLevel, LogType

ClientSystem = extraApi.GetClientSystemCls()
eventDict = eventConfig.SystemClientEventDict


class ModBEClientSystem(ClientSystem):

    def __init__(self, namespace, systemName):
        ModBE.log(LogType.debug, LogLevel.verbose, "ModBE", "Client Initializing.")
        ClientSystem.__init__(self, namespace, systemName)
        self._cancelEvent = False

        # self.listen()

    # def listen(self):
    #     ModBE.log(LogType.debug, LogLevel.verbose, "ModBE", "Client Listening.")
    #     item = extraApi.GetEngineCompFactory().CreateItem(Level.getLevelId())
    #     for key in eventDict:
    #         if hasattr(self, "on" + key.split(":")[2]):
    #             item.GetUserDataInEvent(key.split(":")[2])
    #             self.listenForEventEngine(key.split(":")[2], self, getattr(self, "on" + key.split(":")[2]))
    #             ModBE.log(LogType.debug, LogLevel.verbose, "ModBE", "Client '%s' Listened.", key.split(":")[2])
    #
    # def listenForEventEngine(self, eventName, instance, func, priority = 0):
    #     namespace = 'Minecraft'
    #     systemName = 'Engine'
    #     self.ListenForEvent(namespace, systemName, eventName, instance, func, priority)
    #
    # def response(self, eventId, args):
    #     ModBE.log(LogType.debug, LogLevel.verbose, "ModBE", "Client Responsing.")
    #     if hasattr(EventResponse, "on" + eventId):
    #         getattr(EventResponse, "on" + eventId)(args)
    #         ModBE.log(LogType.debug, LogLevel.verbose, "ModBE", "Client '%s' Responsed.", eventId)
    #     if self._cancelEvent:
    #         if "ret" in args:
    #             args["ret"] = True
    #         elif "cancel" in args:
    #             args["cancel"] = True
    #         self._cancelEvent = False
    #         ModBE.log(LogType.debug, LogLevel.verbose, "ModBE", "Client '%s' Response Canceled.", eventId)
    #
    # def onClientItemTryUseEvent(self, args):
    #     self.response("ClientItemTryUseEvent", args)
    #
    # def onClientItemUseEvent(self, args):
    #     self.response("ClientItemUseEvent", args)

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
