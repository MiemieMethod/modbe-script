# -*- coding: utf-8 -*-

from common.mod import Mod
import mod.server.extraServerApi as extraServerApi
import mod.client.extraClientApi as extraClientApi

from modbe.module import ModBE, Callback, Actor, Pos


def entityAdded(entity, entityType, pos, dimension, isBaby, itemName, auxValue):
    # type: (Actor, str, Pos, int, bool, str, int) -> None
    print("[Test][Info] Actor Added: " + entity.getUniqueID())


@Mod.Binding("ModBE", "1.0.0")
class ModBE(object):

    def __init__(self):
        print("[ModBE][Verbose] Mod Initialized.")
        Callback.register("entityAdded", entityAdded)

    @Mod.InitServer()
    def server(self):
        extraServerApi.RegisterSystem("ModBE", "Server", "modbe.server.system.ModBEServerSystem")
        print("[ModBE][Verbose] Server Initialized.")

    @Mod.DestroyServer()
    def serverDestroy(self):
        print("[ModBE][Verbose] Server Destroyed.")
