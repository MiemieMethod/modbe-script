# -*- coding: utf-8 -*-

import server.extraServerApi as extraApi
import common.system.eventConf as eventConfig
import modbe.server.event.response as eventResponce

ServerSystem = extraApi.GetServerSystemCls()
eventDict = eventConfig.SystemServerEventDict


class ModBEServerSystem(ServerSystem):

    def __init__(self, namespace, systemName):
        print("[ModBE][Verbose] Server Initializing.")
        ServerSystem.__init__(self, namespace, systemName)
        self._cancelEvent = False
        self.listen()

    def listen(self):
        print("[ModBE][Verbose] Server Listening.")
        for key in eventDict:
            if hasattr(self, "on" + key.split(":")[2]):
                self.ListenForEventEngine(key.split(":")[2], self, getattr(self, "on" + key.split(":")[2]))
                print("[ModBE][Verbose] Server ", key.split(":")[2], " Listened.")

    def response(self, eventId, args):
        print("[ModBE][Verbose] Server Responsing.")
        if hasattr(eventResponce, "on" + eventId):
            getattr(eventResponce, "on" + eventId)(args)
            print("[ModBE][Verbose] Server ", eventId, " Responsed.")
        if self._cancelEvent:
            if hasattr(args, "ret"):
                args["ret"] = True
            elif hasattr(args, "cancel"):
                args["cancel"] = True
            self._cancelEvent = False
            print("[ModBE][Info] Server ", eventId, " Response Canceled.")

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
