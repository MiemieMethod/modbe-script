# -*- coding: utf-8 -*-

class BlockBase(object):

    def __init__(self, fullName, aux=0):
        self._fullName = fullName
        self._data = aux
        self._states = None
        self._serializationId = None

    def __str__(self):
        return "BlockBase(fullName=%s, aux=%s)" % (self._fullName, self._data)

    def __repr__(self):
        return "BlockBase(%s, %s)" % (self._fullName, self._data)

    def __hash__(self):
        return hash((self._fullName, self._data))

    def __eq__(self, other):
        if not isinstance(other, BlockBase):
            return NotImplemented
        return self.getBlockIdentifier() == other.getBlockIdentifier() and self.getData() == other.getData()

    def __ne__(self, other):
        if not isinstance(other, BlockBase):
            return NotImplemented
        return self.getBlockIdentifier() != other.getBlockIdentifier() or self.getData() != other.getData()

    def getBlockIdentifier(self):
        # type: () -> str
        return self._fullName

    def getData(self):
        # type: () -> int
        return self._data
