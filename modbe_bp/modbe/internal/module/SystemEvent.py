# -*- coding: utf-8 -*-
import inspect
import functools

from modbe.internal.constant.Event import eventMaps,eventArgs


class SystemEvent(object):
    registry = {}
    map = eventMaps
    args = eventArgs

    def __init__(self):
        pass

    @staticmethod
    def namespacedIdToTriple(namespacedId):
        return namespacedId.split(":")

    @staticmethod
    def executeFunction(userFunc, args, **kwargs):
        argSpec = inspect.getargspec(userFunc)
        argCount = len(argSpec.args)
        minArgCount = min(argCount, len(args))
        keywords = dict(zip(argSpec.args[len(args):], [None] * (argCount - len(args))))
        keywords.update(kwargs)
        partialFunc = functools.partial(userFunc, *args[:minArgCount], **keywords)
        partialFunc()

    @staticmethod
    def wrapArgs(evenId, data):
        result = []
        if evenId in SystemEvent.args:
            if isinstance(SystemEvent.args[evenId], list):
                for argName in SystemEvent.args[evenId]:
                    result.append(data[argName])
            elif isinstance(SystemEvent.args[evenId], type(lambda: 0)):
                result = SystemEvent.args[evenId](data)
        return result

