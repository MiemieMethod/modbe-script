# -*- coding: utf-8 -*-
from modbe.internal.module.ModBE import ModBE

from modbe.internal.enum.Log import LogLevel, LogType
from modbe.internal.constant.Component import *


class DimensionBase(object):
    registry = {}

    def __init__(self, typeId):
        self._id = typeId

    def __str__(self):
        return "DimensionBase(id=%s)" % self._id

    def __repr__(self):
        return "DimensionBase(%s)" % self._id

    def __hash__(self):
        return hash(self._id)

    def __eq__(self, other):
        if not isinstance(other, DimensionBase):
            return NotImplemented
        return self.getId() == other.getId()

    def __ne__(self, other):
        if not isinstance(other, DimensionBase):
            return NotImplemented
        return self.getId() != other.getId()

    def __lt__(self, other):
        if not isinstance(other, DimensionBase):
            return NotImplemented
        return self.getId() < other.getId()

    def __le__(self, other):
        if not isinstance(other, DimensionBase):
            return NotImplemented
        return self.getId() <= other.getId()

    def __gt__(self, other):
        if not isinstance(other, DimensionBase):
            return NotImplemented
        return self.getId() > other.getId()

    def __ge__(self, other):
        if not isinstance(other, DimensionBase):
            return NotImplemented
        return self.getId() >= other.getId()

    def getId(self):
        return self._id

    def getBlock(self, blockPos):
        # type: (BlockPos) -> Block
        pass

    def getLiquidBlock(self, blockPos):
        # type: (BlockPos) -> Block
        """
        仅服务端
        """
        pass

    def getExtraBlock(self, blockPos):
        # type: (BlockPos) -> Block
        """
        仅服务端
        """
        pass

    def getChunk(self, pos):
        # type: (ChunkPos) -> LevelChunk
        pass