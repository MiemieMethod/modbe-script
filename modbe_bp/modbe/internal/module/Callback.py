# -*- coding: utf-8 -*-
from modbe.internal.module.SystemEvent import SystemEvent
from modbe.internal.module.ModBE import ModBE

from modbe.internal.enum.Log import LogLevel, LogType
from modbe.internal.constant.Component import *

class Callback(object):

    def __init__(self):
        pass

    @staticmethod
    def registerCallback(callbackId):
        eventId = SystemEvent.map[callbackId]
        if eventId not in SystemEvent.registry:
            SystemEvent.registry[eventId] = []
        def decorator(callback):
            SystemEvent.registry[eventId].append(callback)
            def inner(*args, **kwargs):
                ModBE.log(LogType.debug, LogLevel.verbose, "ModBE", "Manually invoked an instance of callback '%s'.", callbackId)
                callback(*args, **kwargs)
            return inner
        return decorator

    @staticmethod
    def invokeCallback(callbackId, *args, **kwargs):
        eventId = SystemEvent.map[callbackId]
        if eventId in SystemEvent.registry:
            for func in SystemEvent.registry[eventId]:
                SystemEvent.executeFunction(func, args, **kwargs)
                ModBE.log(LogType.debug, LogLevel.verbose, "ModBE", "Manually invoked callback '%s'.", callbackId)
        return None