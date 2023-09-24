# -*- coding: utf-8 -*-
import server.extraServerApi as extraServerApi
import client.extraClientApi as extraClientApi

from modbe.internal.module.ModBE import ModBE
from modbe.internal.enum.Log import LogLevel, LogType
from modbe.internal.constant.Component import *

Dimension = __import__("modbe.public.module.Dimension").Dimension


class Level(object):

    @staticmethod
    def getLevelId():
        if ModBE.isServer():
            return extraServerApi.GetLevelId()
        if ModBE.isClient():
            return extraClientApi.GetLevelId()

    @staticmethod
    def getLocalDimension():
        """
        仅客户端
        """
        if ModBE.isClient():
            return Dimension(_game.GetCurrentDimension())
        else:
            ModBE.log(LogType.error, LogLevel.error, "ModBE", "Level.getLocalDimension: Server not supported for this method.")

