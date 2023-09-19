# -*- coding: utf-8 -*-

import server.extraServerApi as extraServerApi
import client.extraClientApi as extraClientApi
import common.gameConfig as GameConfig
from mod_log import logger

from modbe.internal.enum.LogLevel import LogLevel
from modbe.internal.enum.LogType import LogType


class ModBE(object):

    @staticmethod
    def isServer():
        # type: () -> bool
        return GameConfig.IsServer()

    @staticmethod
    def isClient():
        # type: () -> bool
        return GameConfig.IsClient()

    @staticmethod
    def preventDefault():
        if ModBE.isServer():
            server = extraServerApi.GetSystem("ModBE", "Server")
            server._cancelEvent = True
        if ModBE.isClient():
            client = extraClientApi.GetSystem("ModBE", "Client")
            client._cancelEvent = True

    @staticmethod
    def log(logType, logLevel, logArea, message, *args):
        # type: (int, int, str, str, Any) -> None
        level = LogLevel.toString(logLevel)
        if logType == LogType.debug:
            logger.debug("[" + level + "][" + logArea + "] " + message, *args)
        elif logType == LogType.info:
            logger.info("[" + level + "][" + logArea + "] " + message, *args)
        elif logType == LogType.error:
            logger.error("[" + level + "][" + logArea + "] " + message, *args)