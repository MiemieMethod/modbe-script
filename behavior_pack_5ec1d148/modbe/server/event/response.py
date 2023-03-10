# -*- coding: utf-8 -*-

import server.extraServerApi as extraApi
from modbe.module import *
from modbe.enum import *


# EntityServerEvent #

def onAddEntityServerEvent(args):
    entity = Actor(args["id"])
    pos = BlockPos(args["posX"], args["posY"], args["posZ"])
    dimension = Dimension(args["dimensionId"])
    Callback.invoke(Callback._getCallbackNameByEngineEvent("AddEntityServerEvent"), entity, args["engineTypeStr"], pos, dimension, args["isBaby"],
                    "itemName" in args and args["itemName"] or "minecraft:air",
                    "auxValue" in args and args["auxValue"] or 0)


# ItemServerEvent #

def onServerItemTryUseEvent(args):
    entity = Actor(args["playerId"])
    itemStack = ItemStack.fromDict(args["itemDict"])
    Callback.invoke(Callback._getCallbackNameByEngineEvent("ServerItemTryUseEvent"), entity, args["itemName"], args["auxValue"], itemStack)
    ModBE.log(LogType.debug, LogLevel.verbose, "ModBE", "onServerItemTryUseEvent: '%s'.", args)


# UndocumentedServerEvent #

def onServerItemUseEvent(args):
    entity = Actor(args["playerId"])
    Callback.invoke(Callback._getCallbackNameByEngineEvent("ServerItemUseEvent"), entity, args["itemName"], args["auxValue"])
    ModBE.log(LogType.debug, LogLevel.verbose, "ModBE", "onServerItemUseEvent: '%s'.", args)
