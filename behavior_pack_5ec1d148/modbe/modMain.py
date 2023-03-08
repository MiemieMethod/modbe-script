# -*- coding: utf-8 -*-

from common.mod import Mod
import mod.server.extraServerApi as extraServerApi
import mod.client.extraClientApi as extraClientApi

from modbe.module import *
from modbe.module import ModBE as Game
from modbe.enum import *


def entityAdded(entity, entityType, pos, dimension, isBaby, itemName, auxValue):
    # type: (Actor, str, Pos, int, bool, str, int) -> None
    Game.log(LogType.info, LogLevel.inform, "Test", "Actor Added: %s of type %s.", entity.getUniqueID(), entity.getEntityTypeId())
    # entity.despawn()


@Mod.Binding("ModBE", "1.0.0")
class ModBE(object):

    def __init__(self):
        Game.log(LogType.debug, LogLevel.verbose, "ModBE", "Mod Initialized.")
        Callback.register("entityAdded", entityAdded)

    @Mod.InitServer()
    def server(self):
        extraServerApi.RegisterSystem("ModBE", "Server", "modbe.server.system.ModBEServerSystem")
        Game.log(LogType.debug, LogLevel.verbose, "ModBE", "Server Initialized.")

    @Mod.DestroyServer()
    def serverDestroy(self):
        Game.log(LogType.debug, LogLevel.verbose, "ModBE", "Server Destroyed.")
