# -*- coding: utf-8 -*-
from modbe.internal.enum.CreativeCategory import CreativeCategory


class ItemBase(object):
    categoryFromString = {
        "all": CreativeCategory.All,
        "construction": CreativeCategory.Construction,
        "nature": CreativeCategory.Nature,
        "equipment": CreativeCategory.Equipment,
        "items": CreativeCategory.Items,
        "commands": CreativeCategory.Commands,
        "none": CreativeCategory.Count,
        "custom": CreativeCategory.Custom
    }

    def __init__(self, fullName, aux=0):
        self._fullName = fullName
        self._aux = aux
        self._block = None

    def __eq__(self, other):
        if isinstance(other, ItemBase):
            return self.getItemIdentifier() == other.getItemIdentifier() and self.getAuxValue() == other.getAuxValue()
        elif isinstance(other, str):
            if self.getAuxValue() == 0:
                return self.getItemIdentifier() == other
            else:
                return self.getItemIdentifier() + ":" + str(self.getAuxValue()) == other
        else:
            return NotImplemented

    def __ne__(self, other):
        if not isinstance(other, ItemBase) or not isinstance(other, str):
            return NotImplemented
        return not self.__eq__(other)

    def getItemIdentifier(self):
        return self._fullName

    def getAuxValue(self):
        return self._aux