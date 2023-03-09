# -*- coding: utf-8 -*-

import client.extraClientApi as extraApi
from modbe.module import *
from modbe.enum import *


# ItemClientEvent #

def onClientItemTryUseEvent(args):
    ModBE.log(LogType.debug, LogLevel.verbose, "ModBE", "onClientItemTryUseEvent: '%s'.", args)


def onClientItemUseEvent(args):
    ModBE.log(LogType.debug, LogLevel.verbose, "ModBE", "onClientItemUseEvent: '%s'.", args)
    ModBE.preventDefault()
