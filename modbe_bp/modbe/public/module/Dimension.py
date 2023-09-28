# -*- coding: utf-8 -*-
from modbe.internal.module.DimensionBase import DimensionBase
from modbe.internal.module.ModBE import ModBE
from modbe.internal.enum.Log import LogLevel, LogType
from modbe.internal.constant.Component import *

from modbe.public.module.Block import Block


class Dimension(DimensionBase):

    def __init__(self, typeId):
        super(Dimension, self).__init__(typeId)

    def __str__(self):
        return "Dimension(id=%s)" % self._id

    def __repr__(self):
        return "Dimension(%s)" % self._id

    def getBlock(self, blockPos):
        # type: (BlockPos) -> Block
        blockPos = blockPos.toBlockPos()
        if ModBE.isServer():
            block = _blockInfo_.GetBlockNew(blockPos.toTuple(), self.getDimensionId())
            return block is not None and Block.fromDict(block) or block
        elif ModBE.isClient():
            if self.getLocalDimension() == self:
                block = _blockInfo_.GetBlock(blockPos.toTuple())
                return block is not None and Block(block[0], block[1]) or block
            ModBE.log(LogType.error, LogLevel.error, "ModBE", "Dimension.getBlock: Local player is not currently in this Dimension: %s.", self.getId())
        return None

    @staticmethod
    def getLocalDimension():
        """
        仅客户端
        """
        if ModBE.isClient():
            return Dimension(_game_.GetCurrentDimension())
        else:
            ModBE.log(LogType.error, LogLevel.error, "ModBE", "Level.getLocalDimension: Server not supported for this method.")

    def getLiquidBlock(self, blockPos):
        # type: (BlockPos) -> Block
        """
        仅服务端
        """
        blockPos = blockPos.toBlockPos()
        if ModBE.isServer():
            block = _blockInfo_.GetLiquidBlock(blockPos.toTuple(), self.getId())
            return block is not None and Block.fromDict(block) or block
        if ModBE.isClient():
            ModBE.log(LogType.error, LogLevel.error, "ModBE",
                      "Dimension.getLiquidBlock: Client not supported for this method.")
        return None

    def getExtraBlock(self, blockPos):
        # type: (BlockPos) -> Block
        """
        仅服务端
        """
        blockPos = blockPos.toBlockPos()
        if ModBE.isServer():
            block = self.getBlock(blockPos)
            liquid = self.getLiquidBlock(blockPos)
            if liquid.getBlockIdentifier() != block.getBlockIdentifier():
                return liquid
        if ModBE.isClient():
            ModBE.log(LogType.error, LogLevel.error, "ModBE",
                      "Dimension.getLiquidBlock: Client not supported for this method.")
        return None

