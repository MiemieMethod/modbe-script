# -*- coding: utf-8 -*-

import server.extraServerApi as extraApi
from modbe.module import *
from modbe.enum import *


def onAddEntityServerEvent(args):
    entity = Actor(args["id"])
    pos = Pos(args["posX"], args["posY"], args["posZ"])
    Callback.invoke("entityAdded", entity, args["engineTypeStr"], pos, args["dimensionId"], args["isBaby"], "itemName" in args and args["itemName"] or "minecraft:air", "auxValue" in args and args["auxValue"] or 0)
