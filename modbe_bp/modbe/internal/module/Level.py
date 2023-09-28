# -*- coding: utf-8 -*-
import server.extraServerApi as extraServerApi
import client.extraClientApi as extraClientApi

from modbe.internal.module.ModBE import ModBE
from modbe.internal.enum.Log import LogLevel, LogType
from modbe.internal.constant.Component import *



class Level(object):

    @staticmethod
    def getLevelId():
        if ModBE.isServer():
            return extraServerApi.GetLevelId()
        if ModBE.isClient():
            return extraClientApi.GetLevelId()
