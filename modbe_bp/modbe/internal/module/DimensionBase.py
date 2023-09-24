# -*- coding: utf-8 -*-

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
        return self.getDimensionId() == other.getDimensionId()

    def __ne__(self, other):
        if not isinstance(other, DimensionBase):
            return NotImplemented
        return self.getDimensionId() != other.getDimensionId()

    def __lt__(self, other):
        if not isinstance(other, DimensionBase):
            return NotImplemented
        return self.getDimensionId() < other.getDimensionId()

    def __le__(self, other):
        if not isinstance(other, DimensionBase):
            return NotImplemented
        return self.getDimensionId() <= other.getDimensionId()

    def __gt__(self, other):
        if not isinstance(other, DimensionBase):
            return NotImplemented
        return self.getDimensionId() > other.getDimensionId()

    def __ge__(self, other):
        if not isinstance(other, DimensionBase):
            return NotImplemented
        return self.getDimensionId() >= other.getDimensionId()

    def __int__(self):
        return self.getDimensionId()

    def getDimensionId(self):
        return self._id
