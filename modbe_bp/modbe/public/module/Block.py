# -*- coding: utf-8 -*-
from modbe.internal.module.BlockBase import BlockBase
from modbe.internal.module.Tag import *
from modbe.internal.module.ModBE import ModBE
from modbe.internal.enum.Log import LogLevel, LogType
from modbe.internal.constant.Component import *

class Block(BlockBase):

    def __init__(self, fullName, aux=0):
        super(Block, self).__init__(fullName, aux)
        if ModBE.isServer():
            self._states = Block.getStatesFromAux(self._fullName, self._data)
            self._serializationId = CompoundTag().putString("name", self._fullName).putCompound(
                "states", CompoundTag.fromDict(self._states))
        if ModBE.isClient():
            pass

    def __eq__(self, other):
        if not isinstance(other, BlockBase):
            return NotImplemented
        return self.getBlockIdentifier() == other.getBlockIdentifier() and self.getData() == other.getData()

    def __ne__(self, other):
        if not isinstance(other, BlockBase):
            return NotImplemented
        return self.getBlockIdentifier() != other.getBlockIdentifier() or self.getData() != other.getData()

    @staticmethod
    def fromDict(blockDict):
        return Block(blockDict["name"], "aux" in blockDict and blockDict["aux"] or 0)

    @staticmethod
    def getStatesFromAux(name, aux):
        """
        仅服务端
        """
        if ModBE.isServer():
            return _blockState.GetBlockStatesFromAuxValue(name, aux)
        else:
            ModBE.log(LogType.error, LogLevel.error, "ModBE",
                      "Block.getStatesFromAux: Client not supported for this method.")

    @staticmethod
    def getAuxFromStates(name, states):
        """
        仅服务端
        """
        if ModBE.isServer():
            return _blockState.GetBlockStatesFromAuxValue(name, states)
        else:
            ModBE.log(LogType.error, LogLevel.error, "ModBE",
                      "Block.getAuxFromStates: Client not supported for this method.")

    def _getBlockBasicDict(self):
        """
        仅服务端
        """
        if ModBE.isServer():
            return _blockInfo.GetBlockBasicInfo(self._fullName)
        else:
            ModBE.log(LogType.error, LogLevel.error, "ModBE",
                      "Block._getBlockBasicDict: Client not supported for this method.")

    def getRenderLayer(self):
        # type: () -> int
        """
        仅服务端
        """
        if ModBE.isServer():
            return self._getBlockBasicDict()["renderLayer"]
        else:
            ModBE.log(LogType.error, LogLevel.error, "ModBE",
                      "Block.getRenderLayer: Client not supported for this method.")

    def getDestroySpeed(self):
        # type: () -> float
        """
        仅服务端
        """
        if ModBE.isServer():
            return self._getBlockBasicDict()["destroyTime"]
        else:
            ModBE.log(LogType.error, LogLevel.error, "ModBE",
                      "Block.getDestroySpeed: Client not supported for this method.")

    def getSolid(self):
        # type: () -> bool
        """
        仅服务端
        """
        if ModBE.isServer():
            return self._getBlockBasicDict()["solid"]
        else:
            ModBE.log(LogType.error, LogLevel.error, "ModBE", "Block.getSolid: Client not supported for this method.")

    def getExplosionResistance(self):
        # type: () -> float
        """
        仅服务端
        """
        if ModBE.isServer():
            return self._getBlockBasicDict()["explosionResistance"]
        else:
            ModBE.log(LogType.error, LogLevel.error, "ModBE",
                      "Block.getExplosionResistance: Client not supported for this method.")

    def getLightEmission(self):
        # type: () -> int
        """
        仅服务端
        """
        if ModBE.isServer():
            return self._getBlockBasicDict()["blockLightEmission"]
        else:
            ModBE.log(LogType.error, LogLevel.error, "ModBE",
                      "Block.getLightEmission: Client not supported for this method.")

    def getLight(self):
        # type: () -> int
        """
        仅服务端
        """
        if ModBE.isServer():
            return self._getBlockBasicDict()["blockLightAbsorption"]
        else:
            ModBE.log(LogType.error, LogLevel.error, "ModBE", "Block.getLight: Client not supported for this method.")

    def getMapColor(self):
        # type: () -> str
        """
        仅服务端
        """
        if ModBE.isServer():
            return self._getBlockBasicDict()["mapColor"]
        else:
            ModBE.log(LogType.error, LogLevel.error, "ModBE",
                      "Block.getMapColor: Client not supported for this method.")

    def getCreativeCategory(self):
        # type: () -> int
        """
        仅服务端
        """
        if ModBE.isServer():
            return self._getBlockBasicDict()["creativeCategory"]
        else:
            ModBE.log(LogType.error, LogLevel.error, "ModBE",
                      "Block.getCreativeCategory: Client not supported for this method.")

    def getStates(self):
        """
        仅服务端
        """
        if ModBE.isServer():
            return self._states
        else:
            ModBE.log(LogType.error, LogLevel.error, "ModBE",
                      "Block.getStates: Client not supported for this method.")

    def hasState(self, stateType):
        """
        仅服务端
        """
        if ModBE.isServer():
            if stateType in self._states:
                return True
            return False
        else:
            ModBE.log(LogType.error, LogLevel.error, "ModBE",
                      "Block.hasState: Client not supported for this method.")

    def getState(self, stateType):
        """
        仅服务端
        """
        if ModBE.isServer():
            if self.hasState(stateType):
                return self._states[stateType]
            else:
                ModBE.log(LogType.error, LogLevel.error, "ModBE",
                          "Block.getState: Cannot find state '%s' in current Block.", stateType)
            return None
        else:
            ModBE.log(LogType.error, LogLevel.error, "ModBE",
                      "Block.getState: Client not supported for this method.")