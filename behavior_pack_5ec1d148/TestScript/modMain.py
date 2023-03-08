# -*- coding: utf-8 -*-

from common.mod import Mod

from modbe.module import ModBE
from modbe.enum import LogType, LogLevel

from TestScript.server import main as serverMain
from TestScript.client import main as clientMain


@Mod.Binding("ModBETest", "1.0.0")
class ModBETest(object):

    def __init__(self):
        if ModBE.isServer():
            serverMain()
        if ModBE.isServer():
            clientMain()
        ModBE.log(LogType.info, LogLevel.inform, "ModBETest", "Mod Initialized.")  # 用于输出日志
