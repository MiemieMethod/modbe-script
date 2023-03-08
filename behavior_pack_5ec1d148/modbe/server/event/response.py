# -*- coding: utf-8 -*-

import server.extraServerApi as extraApi
from modbe.module import ModBE, Callback, Actor, Pos


def onAddEntityServerEvent(args):
    entity = Actor(args["id"])
    pos = Pos(args["posX"], args["posY"], args["posZ"])
    Callback.invoke("entityAdded", entity, args["engineTypeStr"], pos, args["dimensionId"], args["isBaby"], hasattr(args, "itemName") and args["itemName"] or "minecraft:air", hasattr(args, "auxValue") and args["auxValue"] or 0)
    # ModBE.preventDefault()
