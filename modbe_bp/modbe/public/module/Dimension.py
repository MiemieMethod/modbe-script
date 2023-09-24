# -*- coding: utf-8 -*-
from modbe.internal.module.DimensionBase import DimensionBase
from modbe.internal.module.ModBE import ModBE
from modbe.internal.module.Level import Level
from modbe.internal.enum.Log import LogLevel, LogType
from modbe.internal.constant.Component import *


class Dimension(DimensionBase):

    def __init__(self, typeId):
        super(Dimension, self).__init__(typeId)

    def getBlock(self, blockPos):
        # type: (BlockPos) -> Block
        blockPos = blockPos.toBlockPos()
        if ModBE.isServer():
            block = _blockInfo.GetBlockNew(blockPos.toTuple(), self.getId())
            return block is not None and Block.fromDict(block) or block
        if ModBE.isClient():
            if Level.getLocalDimension() == self:
                block = _blockInfo.GetBlock(blockPos.toTuple())
                return block is not None and Block(block[0], block[1]) or block
            ModBE.log(LogType.error, LogLevel.error, "ModBE", "Dimension.getBlock: Local player is not currently in this Dimension: %s.", self.getId())
        return None