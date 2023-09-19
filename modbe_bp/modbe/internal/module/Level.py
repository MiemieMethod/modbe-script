# -*- coding: utf-8 -*-
import server.extraServerApi as extraServerApi
import client.extraClientApi as extraClientApi

from modbe.internal.module.ModBE import ModBE
from modbe.internal.enum.LogLevel import LogLevel
from modbe.internal.enum.LogType import LogType


class Level(object):

    @staticmethod
    def getLevelId():
        if ModBE.isServer():
            return extraServerApi.GetLevelId()
        if ModBE.isClient():
            return extraClientApi.GetLevelId()

