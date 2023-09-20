# -*- coding: utf-8 -*-
import server.extraServerApi as extraServerApi
import client.extraClientApi as extraClientApi

from modbe.internal.module.ModBE import ModBE

__all__ = ["_game", "_factory", "_blockInfo"]

if ModBE.isServer():
    _factory = extraServerApi.GetEngineCompFactory()
    _game = _factory.CreateGame(extraServerApi.GetLevelId())
    _blockInfo = _factory.CreateBlockInfo(extraServerApi.GetLevelId())
if ModBE.isClient():
    _factory = extraClientApi.GetEngineCompFactory()
    _game = _factory.CreateGame(extraClientApi.GetLevelId())
    _blockInfo = _factory.CreateBlockInfo(extraClientApi.GetLevelId())