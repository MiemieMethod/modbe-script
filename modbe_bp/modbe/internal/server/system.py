# -*- coding: utf-8 -*-

import server.extraServerApi as extraApi
import common.system.eventConf as eventConfig

from modbe.internal.module.ModBE import ModBE
from modbe.internal.enum.Log import LogLevel, LogType
from modbe.internal.module.SystemEvent import SystemEvent
from modbe.internal.constant.Component import *

from modbe.internal.module.Callback import Callback

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
        for key in eventDict:
            SystemEvent.listenEngineEvent(key, self)
            ModBE.log(LogType.debug, LogLevel.verbose, "ModBE", "Server '%s' Listened.", key.split(":")[2])

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


from modbe.public.module.Dimension import Dimension
from modbe.internal.module.Pos import BlockPos
from modbe.internal.constant.Component import *

if ModBE.isServer():
    @Callback.registerCallback("ItemUseBefore")
    def onItemUseBefore(data):
        # type: (dict) -> None
        blocks = _blockInfo_.GetLoadBlocks()
        print(blocks)
