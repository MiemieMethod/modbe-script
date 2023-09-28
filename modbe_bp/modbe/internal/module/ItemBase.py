# -*- coding: utf-8 -*-
from modbe.internal.enum.CreativeCategory import CreativeCategory
from modbe.internal.module.ModBE import ModBE
from modbe.internal.enum.Log import LogLevel, LogType


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
    
    def __str__(self):
        return "ItemBase(fullName=%s, aux=%s)" % (self._fullName, self._aux)
    
    def __repr__(self):
        return "ItemBase(%s, %s)" % (self._fullName, self._aux)
    
    def __hash__(self):
        return hash((self._fullName, self._aux))

    def getItemIdentifier(self):
        return self._fullName

    def getAuxValue(self):
        return self._aux


class ItemStackBase(object):
    TAG_ENCHANTS = "ench"

    def __init__(self, fullName, count=1, aux=0, _userData=None):
        self._item = ItemBase(fullName)
        self._block = None
        self._aux = aux
        self._count = count
        self._userData = None

    def __eq__(self, other):
        if not isinstance(other, ItemStackBase):
            return NotImplemented
        return self.getItem() == other.getItem() and self.get() == other.get() and self.getAuxValue() == other.getAuxValue() and self.getUserData() == other.getUserData()

    def __ne__(self, other):
        if not isinstance(other, ItemStackBase):
            return NotImplemented
        return self.getItem() != other.getItem() or self.get() != other.get() or self.getAuxValue() != other.getAuxValue() or self.getUserData() != other.getUserData()

    def __str__(self):
        return "ItemStackBase(fullName=%s, count=%s, aux=%s, userData=%s)" % (
        self._item.getItemIdentifier(), self._count, self._aux, self._userData)

    def __repr__(self):
        return "ItemStackBase(%s, %s, %s, %s)" % (self._item.getItemIdentifier(), self._count, self._aux, self._userData)

    def __hash__(self):
        return hash((self._item, self._count, self._aux, self._userData))

    def __len__(self):
        return self.get()

    def __lt__(self, other):
        if not isinstance(other, ItemStackBase):
            return NotImplemented
        return len(self) < len(other)

    def __le__(self, other):
        if not isinstance(other, ItemStackBase):
            return NotImplemented
        return len(self) <= len(other)

    def __gt__(self, other):
        if not isinstance(other, ItemStackBase):
            return NotImplemented
        return len(self) > len(other)

    def __ge__(self, other):
        if not isinstance(other, ItemStackBase):
            return NotImplemented
        return len(self) >= len(other)

    def __int__(self):
        return self.get()

    def __add__(self, other):
        if isinstance(other, ItemStackBase):
            if self.getItem() == other.getItem() and self.getAuxValue() == other.getAuxValue() and self.getUserData() == other.getUserData():
                return ItemStackBase(self.getItemIdentifier(), self.get() + other.get(), self.getAuxValue(),
                                 self.getUserData())
            return NotImplemented
        elif isinstance(other, int) or isinstance(other, float):
            return ItemStackBase(self.getItemIdentifier(), self.get() + int(other), self.getAuxValue(), self.getUserData())
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, ItemStackBase):
            if self.getItem() == other.getItem() and self.getAuxValue() == other.getAuxValue() and self.getUserData() == other.getUserData():
                return ItemStackBase(self.getItemIdentifier(), self.get() - other.get(), self.getAuxValue(),
                                 self.getUserData())
            return NotImplemented
        elif isinstance(other, int) or isinstance(other, float):
            return ItemStackBase(self.getItemIdentifier(), self.get() - int(other), self.getAuxValue(), self.getUserData())
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return ItemStackBase(self.getItemIdentifier(), int(self.get() * other), self.getAuxValue(), self.getUserData())
        return NotImplemented

    def __truediv__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return ItemStackBase(self.getItemIdentifier(), int(self.get() / other), self.getAuxValue(), self.getUserData())
        return NotImplemented

    def __floordiv__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return ItemStackBase(self.getItemIdentifier(), int(self.get() // other), self.getAuxValue(), self.getUserData())
        return NotImplemented

    def __mod__(self, other):
        if isinstance(other, int):
            return ItemStackBase(self.getItemIdentifier(), self.get() % other, self.getAuxValue(), self.getUserData())
        return NotImplemented

    def __pow__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return ItemStackBase(self.getItemIdentifier(), int(self.get() ** other), self.getAuxValue(), self.getUserData())
        return NotImplemented

    def __lshift__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return ItemStackBase(self.getItemIdentifier(), self.get() << int(other), self.getAuxValue(), self.getUserData())
        return NotImplemented

    def __rshift__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return ItemStackBase(self.getItemIdentifier(), self.get() >> int(other), self.getAuxValue(), self.getUserData())
        return NotImplemented

    def __and__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return ItemStackBase(self.getItemIdentifier(), self.get() & int(other), self.getAuxValue(), self.getUserData())
        return NotImplemented

    def __xor__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return ItemStackBase(self.getItemIdentifier(), self.get() ^ int(other), self.getAuxValue(), self.getUserData())
        return NotImplemented

    def __or__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return ItemStackBase(self.getItemIdentifier(), self.get() | int(other), self.getAuxValue(), self.getUserData())
        return NotImplemented

    def __radd__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return ItemStackBase(self.getItemIdentifier(), int(other) + self.get(), self.getAuxValue(), self.getUserData())
        return NotImplemented

    def __rsub__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return ItemStackBase(self.getItemIdentifier(), int(other) - self.get(), self.getAuxValue(), self.getUserData())
        return NotImplemented

    def __rmul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return ItemStackBase(self.getItemIdentifier(), int(other * self.get()), self.getAuxValue(), self.getUserData())
        return NotImplemented

    def __rtruediv__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return ItemStackBase(self.getItemIdentifier(), int(other / self.get()), self.getAuxValue(), self.getUserData())
        return NotImplemented

    def __rfloordiv__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return ItemStackBase(self.getItemIdentifier(), int(other // self.get()), self.getAuxValue(), self.getUserData())
        return NotImplemented

    def __rmod__(self, other):
        if isinstance(other, int):
            return ItemStackBase(self.getItemIdentifier(), other % self.get(), self.getAuxValue(), self.getUserData())
        return NotImplemented

    def __rpow__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return ItemStackBase(self.getItemIdentifier(), int(other ** self.get()), self.getAuxValue(), self.getUserData())
        return NotImplemented

    def __rlshift__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return ItemStackBase(self.getItemIdentifier(), int(other) << self.get(), self.getAuxValue(), self.getUserData())
        return NotImplemented

    def __rrshift__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return ItemStackBase(self.getItemIdentifier(), int(other) >> self.get(), self.getAuxValue(), self.getUserData())
        return NotImplemented

    def __rand__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return ItemStackBase(self.getItemIdentifier(), int(other) & self.get(), self.getAuxValue(), self.getUserData())
        return NotImplemented

    def __rxor__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return ItemStackBase(self.getItemIdentifier(), int(other) ^ self.get(), self.getAuxValue(), self.getUserData())
        return NotImplemented

    def __ror__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            return ItemStackBase(self.getItemIdentifier(), int(other) | self.get(), self.getAuxValue(), self.getUserData())
        return NotImplemented

    def __iadd__(self, other):
        if isinstance(other, ItemStackBase):
            if self.getItem() == other.getItem() and self.getAuxValue() == other.getAuxValue() and self.getUserData() == other.getUserData():
                self.add(other.get())
                return self
            return NotImplemented
        elif isinstance(other, int) or isinstance(other, float):
            self.add(int(other))
            return self
        return NotImplemented

    def __isub__(self, other):
        if isinstance(other, ItemStackBase):
            if self.getItem() == other.getItem() and self.getAuxValue() == other.getAuxValue() and self.getUserData() == other.getUserData():
                self.remove(other.get())
                return self
            return NotImplemented
        elif isinstance(other, int) or isinstance(other, float):
            self.remove(int(other))
            return self
        return NotImplemented

    def __imul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            self.set(int(self.get() * other))
            return self
        return NotImplemented

    def __itruediv__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            self.set(int(self.get() / other))
            return self
        return NotImplemented

    def __ifloordiv__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            self.set(int(self.get() // other))
            return self
        return NotImplemented

    def __imod__(self, other):
        if isinstance(other, int):
            self.set(self.get() % other)
            return self
        return NotImplemented

    def __ipow__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            self.set(int(self.get() ** other))
            return self
        return NotImplemented

    def __ilshift__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            self.set(self.get() << int(other))
            return self
        return NotImplemented

    def __irshift__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            self.set(self.get() >> int(other))
            return self
        return NotImplemented

    def __iand__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            self.set(self.get() & int(other))
            return self
        return NotImplemented

    def __ixor__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            self.set(self.get() ^ int(other))
            return self
        return NotImplemented

    def __ior__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            self.set(self.get() | int(other))
            return self
        return NotImplemented

    def __neg__(self):
        return ItemStackBase(self.getItemIdentifier(), -self.get(), self.getAuxValue(), self.getUserData())

    def __pos__(self):
        return ItemStackBase(self.getItemIdentifier(), +self.get(), self.getAuxValue(), self.getUserData())

    def __abs__(self):
        return ItemStackBase(self.getItemIdentifier(), abs(self.get()), self.getAuxValue(), self.getUserData())

    def __invert__(self):
        return ItemStackBase(self.getItemIdentifier(), ~self.get(), self.getAuxValue(), self.getUserData())

    def getItem(self):
        return self._item

    def get(self):
        return self._count

    def set(self, inCount):
        if inCount <= self.getMaxStackSize():
            self._count = inCount >= 0 and inCount or 0
        else:
            ModBE.log(LogType.error, LogLevel.error, "ModBE", "ItemStackBase.set: inCount > maxStackSize.")

    def add(self, addCount):
        self.set(self.get() + addCount)

    def remove(self, removeCount):
        self.set(self.get() - removeCount)

    def increase(self):
        self.add(1)

    def decrease(self):
        self.remove(1)

    def getUserData(self):
        return self._userData

    def getItemIdentifier(self):
        return self.getItem().getItemIdentifier()
    def getAuxValue(self):
        return self._aux