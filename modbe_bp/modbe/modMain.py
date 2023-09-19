# -*- coding: utf-8 -*-

from common.mod import Mod
import mod.server.extraServerApi as extraServerApi
import mod.client.extraClientApi as extraClientApi

from modbe.internal.module.ModBE import ModBE as Game
from modbe.internal.enum.LogType import LogType
from modbe.internal.enum.LogLevel import LogLevel


@Mod.Binding("ModBE", "1.0.0")
class ModBE(object):

    def __init__(self):
        Game.log(LogType.debug, LogLevel.verbose, "ModBE", "Mod Initialized.")

    @Mod.InitServer()
    def server(self):
        extraServerApi.RegisterSystem("ModBE", "Server", "modbe.internal.server.system.ModBEServerSystem")
        Game.log(LogType.debug, LogLevel.verbose, "ModBE", "Server Initialized.")

    @Mod.DestroyServer()
    def serverDestroy(self):
        Game.log(LogType.debug, LogLevel.verbose, "ModBE", "Server Destroyed.")

    @Mod.InitClient()
    def client(self):
        extraClientApi.RegisterSystem("ModBE", "Client", "modbe.internal.client.system.ModBEClientSystem")
        Game.log(LogType.debug, LogLevel.verbose, "ModBE", "Client Initialized.")

    @Mod.DestroyClient()
    def clientDestroy(self):
        Game.log(LogType.debug, LogLevel.verbose, "ModBE", "Client Destroyed.")
