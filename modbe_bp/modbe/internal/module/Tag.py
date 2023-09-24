# -*- coding: utf-8 -*-
from common.CompoundTag import Type as TagType
from modbe.internal.module.ModBE import ModBE
from modbe.internal.enum.Log import LogLevel, LogType

__all__ = [
    "TagType",
    "Tag",
    "EndTag",
    "ByteTag",
    "ShortTag",
    "IntTag",
    "Int64Tag",
    "FloatTag",
    "DoubleTag",
    "ByteArrayTag",
    "StringTag",
    "ListTag",
    "CompoundTag",
    "IntArrayTag"
]

class Tag(object):

    def __new__(cls, typeId, value=None):
        return object.__new__(Tag._typeIdToClass(typeId), value)

    def __init__(self, typeId):
        self._type = typeId
        if not hasattr(self, "_data"):
            self._data = None

    def __str__(self):
        return "Tag(type=%s, value=%s)" % (self._type, self._data)

    def __repr__(self):
        return "Tag(%s, %s)" % (self._type, self._data)

    def __hash__(self):
        return hash((self._type, self._data))

    @staticmethod
    def _typeIdToClass(typeId):
        classes = [
            EndTag,
            ByteTag,
            ShortTag,
            IntTag,
            Int64Tag,
            FloatTag,
            DoubleTag,
            ByteArrayTag,
            StringTag,
            ListTag,
            CompoundTag,
            IntArrayTag
        ]
        return classes[typeId]

    def get(self, *args):
        return self._data

    def put(self, *args):
        self._data = args[0]
        return self

    def getId(self):
        return self._type

    def copy(self):
        return Tag(self._type)


class EndTag(Tag):

    def __new__(cls):
        return object.__new__(cls)

    def __init__(self):
        super(EndTag, self).__init__(TagType.End)

    def __str__(self):
        return "EndTag()"

    def __repr__(self):
        return "EndTag()"

    def __hash__(self):
        return hash(self._type)

    def __eq__(self, other):
        if not isinstance(other, Tag):
            return NotImplemented
        if not isinstance(other, EndTag):
            return False
        return True

    def __ne__(self, other):
        if not isinstance(other, Tag):
            return NotImplemented
        if not isinstance(other, EndTag):
            return False
        return True

    def copy(self):
        return EndTag()


class ByteTag(Tag):

    def __new__(cls, data=0):
        return object.__new__(cls, data)

    def __init__(self, data=0):
        super(ByteTag, self).__init__(TagType.Byte)
        self._data = data

    def __str__(self):
        return "ByteTag(value=%s)" % self._data

    def __repr__(self):
        return "ByteTag(%s)" % self._data

    def __eq__(self, other):
        if not isinstance(other, Tag):
            return NotImplemented
        if not isinstance(other, ByteTag):
            return False
        return self.get() == other.get()

    def __ne__(self, other):
        if not isinstance(other, Tag):
            return NotImplemented
        if not isinstance(other, ByteTag):
            return False
        return self.get() != other.get()

    def copy(self):
        return ByteTag(self._data)


class ShortTag(Tag):

    def __new__(cls, data=0):
        return object.__new__(cls, data)

    def __init__(self, data=0):
        super(ShortTag, self).__init__(TagType.Short)
        self._data = data

    def __str__(self):
        return "ShortTag(value=%s)" % self._data

    def __repr__(self):
        return "ShortTag(%s)" % self._data

    def __eq__(self, other):
        if not isinstance(other, Tag):
            return NotImplemented
        if not isinstance(other, ShortTag):
            return False
        return self.get() == other.get()

    def __ne__(self, other):
        if not isinstance(other, Tag):
            return NotImplemented
        if not isinstance(other, ShortTag):
            return False
        return self.get() != other.get()

    def copy(self):
        return ShortTag(self._data)


class IntTag(Tag):

    def __new__(cls, data=0):
        return object.__new__(cls, data)

    def __init__(self, data=0):
        super(IntTag, self).__init__(TagType.Int)
        self._data = data

    def __str__(self):
        return "IntTag(value=%s)" % self._data

    def __repr__(self):
        return "IntTag(%s)" % self._data

    def __eq__(self, other):
        if not isinstance(other, Tag):
            return NotImplemented
        if not isinstance(other, IntTag):
            return False
        return self.get() == other.get()

    def __ne__(self, other):
        if not isinstance(other, Tag):
            return NotImplemented
        if not isinstance(other, IntTag):
            return False
        return self.get() != other.get()

    def copy(self):
        return IntTag(self._data)


class Int64Tag(Tag):

    def __new__(cls, data=0):
        return object.__new__(cls, data)

    def __init__(self, data=0):
        super(Int64Tag, self).__init__(TagType.Int64)
        self._data = data

    def __str__(self):
        return "Int64Tag(value=%s)" % self._data

    def __repr__(self):
        return "Int64Tag(%s)" % self._data

    def __eq__(self, other):
        if not isinstance(other, Tag):
            return NotImplemented
        if not isinstance(other, Int64Tag):
            return False
        return self.get() == other.get()

    def __ne__(self, other):
        if not isinstance(other, Tag):
            return NotImplemented
        if not isinstance(other, Int64Tag):
            return False
        return self.get() != other.get()

    def copy(self):
        return Int64Tag(self._data)


class FloatTag(Tag):

    def __new__(cls, data=0.0):
        return object.__new__(cls, data)

    def __init__(self, data=0.0):
        super(FloatTag, self).__init__(TagType.Float)
        self._data = data

    def __str__(self):
        return "FloatTag(value=%s)" % self._data

    def __repr__(self):
        return "FloatTag(%s)" % self._data

    def __eq__(self, other):
        if not isinstance(other, Tag):
            return NotImplemented
        if not isinstance(other, FloatTag):
            return False
        return self.get() == other.get()

    def __ne__(self, other):
        if not isinstance(other, Tag):
            return NotImplemented
        if not isinstance(other, FloatTag):
            return False
        return self.get() != other.get()

    def copy(self):
        return FloatTag(self._data)


class DoubleTag(Tag):

    def __new__(cls, data=0.0):
        return object.__new__(cls, data)

    def __init__(self, data=0.0):
        super(DoubleTag, self).__init__(TagType.Double)
        self._data = data

    def __str__(self):
        return "DoubleTag(value=%s)" % self._data

    def __repr__(self):
        return "DoubleTag(%s)" % self._data

    def __eq__(self, other):
        if not isinstance(other, Tag):
            return NotImplemented
        if not isinstance(other, DoubleTag):
            return False
        return self.get() == other.get()

    def __ne__(self, other):
        if not isinstance(other, Tag):
            return NotImplemented
        if not isinstance(other, DoubleTag):
            return False
        return self.get() != other.get()

    def copy(self):
        return DoubleTag(self._data)


class ByteArrayTag(Tag):

    def __new__(cls, data=None):
        if data is None:
            data = []
        return object.__new__(cls, data)

    def __init__(self, data=None):
        super(ByteArrayTag, self).__init__(TagType.ByteArray)
        if data is None:
            data = []
        self._data = data

    def __str__(self):
        return "ByteArrayTag(value=%s)" % self._data

    def __repr__(self):
        return "ByteArrayTag(%s)" % self._data

    def __eq__(self, other):
        if not isinstance(other, Tag):
            return NotImplemented
        if not isinstance(other, ByteArrayTag):
            return False
        return self.get() == other.get()

    def __ne__(self, other):
        if not isinstance(other, Tag):
            return NotImplemented
        if not isinstance(other, ByteArrayTag):
            return False
        return self.get() != other.get()

    def __len__(self):
        return len(self._data)

    def __getitem__(self, index):
        return self._data[index]

    def __setitem__(self, index, value):
        self._data[index] = value

    def __delitem__(self, index):
        del self._data[index]

    def __iter__(self):
        return iter(self._data)

    def __contains__(self, item):
        return item in self._data

    def copy(self):
        return ByteArrayTag(self._data)


class StringTag(Tag):

    def __new__(cls, data=""):
        return object.__new__(cls, data)

    def __init__(self, data=""):
        super(StringTag, self).__init__(TagType.String)
        self._data = data

    def __str__(self):
        return "StringTag(value=%s)" % self._data

    def __repr__(self):
        return "StringTag(%s)" % self._data

    def __eq__(self, other):
        if not isinstance(other, Tag):
            return NotImplemented
        if not isinstance(other, StringTag):
            return False
        return self.get() == other.get()

    def __ne__(self, other):
        if not isinstance(other, Tag):
            return NotImplemented
        if not isinstance(other, StringTag):
            return False
        return self.get() != other.get()

    def copy(self):
        return StringTag(self._data)


class ListTag(Tag):

    def __new__(cls, tagList=None):
        if tagList is None:
            tagList = []
        return object.__new__(cls, tagList)

    def __init__(self, tagList=None):
        super(ListTag, self).__init__(TagType.List)
        if tagList is None:
            tagList = []
        self._list = tagList
        self._listType = self.size() > 0 and self.get(0).getId() or TagType.End

    def __str__(self):
        return "ListTag(value=%s)" % self._list

    def __repr__(self):
        return "ListTag(%s)" % self._list

    def __eq__(self, other):
        if not isinstance(other, Tag):
            return NotImplemented
        if not isinstance(other, ListTag):
            return False
        if self.size() == other.size():
            for i in range(0, self.size() - 1):
                if self.get(i) != other.get(i):
                    return False
            return True
        return False

    def __ne__(self, other):
        if not isinstance(other, Tag):
            return NotImplemented
        return not self.__eq__(other)

    def __len__(self):
        return self.size()

    def __getitem__(self, index):
        tag = self.get(index)
        if tag.getId() != TagType.List or tag.getId() != TagType.Compound:
            return self.get(index).get()
        return self.get(index)

    def __setitem__(self, index, value):
        if isinstance(value, Tag):
            self._list[index] = value
        elif isinstance(value, int):
            self._list[index] = IntTag(value)
        elif isinstance(value, float):
            self._list[index] = FloatTag(value)
        elif isinstance(value, str):
            self._list[index] = StringTag(value)
        elif isinstance(value, bool):
            self._list[index] = ByteTag(value and 1 or 0)
        else:
            return NotImplemented

    def __delitem__(self, index):
        self.erase(index)

    def __iter__(self):
        return iter(self._list)

    def __contains__(self, item):
        return item in self._list

    def __add__(self, other):
        if not isinstance(other, Tag):
            return NotImplemented
        if not isinstance(other, ListTag):
            return NotImplemented
        return ListTag(self._list + other.getList())

    def __iadd__(self, other):
        if not isinstance(other, Tag):
            return NotImplemented
        if not isinstance(other, ListTag):
            return NotImplemented
        self._list += other.getList()
        return self

    @staticmethod
    def fromList(rawList, _list=None):
        """
        Python限制，无法正确设置“非布尔值形态的Byte”、Short、Long、Double、ByteArray和IntArray作为元素，请手动设置
        """
        if _list is None:
            _list = ListTag()
        if rawList is None or len(rawList) == 0:
            return _list
        else:
            for element in rawList:
                if isinstance(element, int):
                    _list.add(IntTag(element))
                elif isinstance(element, float):
                    _list.add(FloatTag(element))
                elif isinstance(element, str):
                    _list.add(StringTag(element))
                elif isinstance(element, bool):
                    _list.add(ByteTag(element and 1 or 0))
                elif isinstance(element, list):
                    _list.add(ListTag.fromList(element))
                elif isinstance(element, dict):
                    _list.add(CompoundTag.fromDict(element))
                else:
                    ModBE.log(LogType.error, LogLevel.error, "ModBE", "ListTag.fromList: Unsupported Type: '%s' added to a ListTag.", element)
            return _list

    def toList(self):
        result = []
        for element in self._list:
            if isinstance(element, ListTag):
                result.append(element.toList())
            elif isinstance(element, CompoundTag):
                result.append(element.toDict())
            elif isinstance(element, Tag):
                result.append(element.get())
            else:
                ModBE.log(LogType.error, LogLevel.error, "ModBE", "ListTag.toList: Unsupported Type: '%s' serialized to a list.", element)
        return result

    @staticmethod
    def fromObject(rawList, _list=None):
        if _list is None:
            _list = ListTag()
        if rawList is None or len(rawList) == 0:
            return _list
        else:
            for element in rawList:
                if isinstance(element, list):
                    _list.add(ListTag.fromObject(element))
                elif isinstance(element, dict):
                    if "__type__" in element:
                        typeId = element["__type__"]
                        _list.add(Tag._typeIdToClass(typeId)(element["__value__"]))
                    else:
                        _list.add(CompoundTag.fromObject(element))
                else:
                    ModBE.log(LogType.error, LogLevel.error, "ModBE", "ListTag.fromObject: Unsupported Type: '%s' added to a ListTag.", element)
            return _list

    def getListType(self):
        return self._listType

    def getList(self):
        return self._list

    def size(self):
        return len(self._list)

    def get(self, index):
        return self._list[index]

    def add(self, tag):
        # type: (Tag) -> ListTag
        self._list.append(tag)
        if self.size() == 1:
            self._listType = self.get(0).getId()
        return self

    def put(self, data):
        self._list = data
        self._listType = self.size() > 0 and self.get(0).getId() or TagType.End
        return self

    def erase(self, index):
        # type: (int) -> Tag
        return self._list.pop(index)

    def popBack(self):
        return self._list.pop()

    def forEachCompoundTag(self, func):
        # type: (Callable[[CompoundTag], None]) -> None
        for tag in self._list:
            if isinstance(tag, CompoundTag):
                func(tag)

    def copy(self):
        return ListTag(self._list)


class CompoundTag(Tag):

    def __new__(cls, data=None):
        if data is None:
            data = {}
        return object.__new__(cls, data)

    def __init__(self, tagDict=None):
        super(CompoundTag, self).__init__(TagType.Compound)
        if tagDict is None:
            tagDict = {}
        self._tags = tagDict

    def __str__(self):
        return "CompoundTag(value=%s)" % self._tags

    def __repr__(self):
        return "CompoundTag(%s)" % self._tags

    def __eq__(self, other):
        if not isinstance(other, Tag):
            return NotImplemented
        if not isinstance(other, CompoundTag):
            return False
        for key in self.getTags():
            if not other.contains(key):
                return False
            if self.get(key) != other.get(key):
                return False
        return True

    def __ne__(self, other):
        if not isinstance(other, Tag):
            return NotImplemented
        return not self.__eq__(other)

    def __contains__(self, item):
        return item in self._tags

    def __getitem__(self, key):
        tag = self.get(key)
        if tag.getId() != TagType.List or tag.getId() != TagType.Compound:
            return self.get(key).get()
        return self.get(key)

    def __setitem__(self, key, value):
        if isinstance(value, Tag):
            self.put(key, value)
        elif isinstance(value, int):
            self.putInt(key, value)
        elif isinstance(value, float):
            self.putFloat(key, value)
        elif isinstance(value, str):
            self.putString(key, value)
        elif isinstance(value, bool):
            self.putBoolean(key, value)
        else:
            return NotImplemented

    def __delitem__(self, key):
        self.remove(key)

    def __iter__(self):
        return iter(self._tags)

    def __len__(self):
        return len(self._tags)

    def __add__(self, other):
        if not isinstance(other, Tag):
            return NotImplemented
        if not isinstance(other, CompoundTag):
            return NotImplemented
        tags = self._tags.copy()
        tags.update(other.getTags())
        return CompoundTag(tags)

    def __iadd__(self, other):
        if not isinstance(other, Tag):
            return NotImplemented
        if not isinstance(other, CompoundTag):
            return NotImplemented
        self._tags.update(other.getTags())
        return self

    @staticmethod
    def fromDict(rawDict, _compound=None):
        """
        Python限制，无法正确设置“非布尔值形态的Byte”、Short、Long、Double、ByteArray和IntArray，请手动设置
        """
        if _compound is None:
            _compound = CompoundTag()
        if rawDict is None or len(rawDict) == 0:
            return _compound
        for key in rawDict:
            value = rawDict[key]
            if isinstance(value, int) or isinstance(value, float) or isinstance(value, str) or isinstance(value, bool):
                _compound[key] = value
            elif isinstance(value, list):
                _compound.putList(key, ListTag.fromList(value))
            elif isinstance(value, dict):
                _compound.putCompound(key, CompoundTag.fromDict(value))
            else:
                ModBE.log(LogType.error, LogLevel.error, "ModBE", "CompoundTag.fromDict: Unsupported Type: '%s' added to a CompoundTag key: '%s'.", value, key)
        return _compound

    def toDict(self):
        result = {}
        for key in self._tags:
            value = self._tags[key]
            if isinstance(value, ListTag):
                result[key] = value.toList()
            elif isinstance(value, CompoundTag):
                result[key] = value.toDict()
            elif isinstance(value, Tag):
                result[key] = value.get()
            else:
                ModBE.log(LogType.error, LogLevel.error, "ModBE", "CompoundTag.toDict: Unsupported Type: '%s' serialized to a dict key: '%s'.", value, key)
        return result

    @staticmethod
    def fromObject(rawObject, _compound=None):
        if _compound is None:
            _compound = CompoundTag()
        if rawObject is None or len(rawObject) == 0:
            return _compound
        for key in rawObject:
            value = rawObject[key]
            if isinstance(value, list):
                _compound.putList(key, ListTag.fromObject(value))
            elif isinstance(value, dict):
                if "__type__" in value:
                    typeId = value["__type__"]
                    _compound.put(key, Tag._typeIdToClass(typeId)(value["__value__"]))
                else:
                    _compound.putCompound(key, CompoundTag.fromObject(value))
            else:
                ModBE.log(LogType.error, LogLevel.error, "ModBE", "CompoundTag.fromObject: Unsupported Type: '%s' added to a CompoundTag key: '%s'.", value, key)
        return _compound

    def remove(self, name):
        # type: (str) -> bool
        if self.contains(name):
            del self._tags[name]
            return True
        return False

    def contains(self, name, typeId=TagType.End):
        # type: (str, int) -> bool
        if typeId <= TagType.End or typeId > TagType.IntArray:
            return name in self._tags
        else:
            return name in self._tags and self._tags[name].getId() == typeId

    def get(self, name):
        # type: (str) -> Tag | None
        if self.contains(name):
            return self._tags[name]
        return None

    def getTags(self):
        # type: () -> dict
        return self._tags

    def getBoolean(self, name):
        # type: (str) -> int
        if self.contains(name, TagType.Byte):
            return self._tags[name].get()
        return False

    def getByte(self, name):
        # type: (str) -> int
        if self.contains(name, TagType.Byte):
            return self._tags[name].get()
        return 0

    def getShort(self, name):
        # type: (str) -> int
        if self.contains(name, TagType.Short):
            return self._tags[name].get()
        return 0

    def getInt(self, name):
        # type: (str) -> int
        if self.contains(name, TagType.Int):
            return self._tags[name].get()
        return 0

    def getInt64(self, name):
        # type: (str) -> int
        if self.contains(name, TagType.Int64):
            return self._tags[name].get()
        return 0

    def getFloat(self, name):
        # type: (str) -> float
        if self.contains(name, TagType.Float):
            return self._tags[name].get()
        return 0.0

    def getDouble(self, name):
        # type: (str) -> float
        if self.contains(name, TagType.Double):
            return self._tags[name].get()
        return 0.0

    def getByteArray(self, name):
        # type: (str) -> list[int] | None
        if self.contains(name, TagType.ByteArray):
            return self._tags[name].get()
        return None

    def getString(self, name):
        # type: (str) -> str | None
        if self.contains(name, TagType.String):
            return self._tags[name].get()
        return None

    def getList(self, name):
        # type: (str) -> ListTag | None
        if self.contains(name, TagType.List):
            return self._tags[name]
        return None

    def getCompound(self, name):
        # type: (str) -> CompoundTag | None
        if self.contains(name, TagType.Compound):
            return self._tags[name]
        return None

    def getIntArray(self, name):
        # type: (str) -> list[int] | None
        if self.contains(name, TagType.IntArray):
            return self._tags[name].get()
        return None

    def getBooleanTag(self, name):
        # type: (str) -> ByteTag | None
        if self.contains(name, TagType.Byte):
            return self._tags[name]
        return None

    def getByteTag(self, name):
        # type: (str) -> ByteTag | None
        if self.contains(name, TagType.Byte):
            return self._tags[name]
        return None

    def getShortTag(self, name):
        # type: (str) -> ShortTag | None
        if self.contains(name, TagType.Short):
            return self._tags[name]
        return None

    def getIntTag(self, name):
        # type: (str) -> IntTag | None
        if self.contains(name, TagType.Int):
            return self._tags[name]
        return None

    def getInt64Tag(self, name):
        # type: (str) -> Int64Tag | None
        if self.contains(name, TagType.Int64):
            return self._tags[name]
        return None

    def getFloatTag(self, name):
        # type: (str) -> FloatTag | None
        if self.contains(name, TagType.Float):
            return self._tags[name]
        return None

    def getDoubleTag(self, name):
        # type: (str) -> DoubleTag | None
        if self.contains(name, TagType.Double):
            return self._tags[name]
        return None

    def getByteArrayTag(self, name):
        # type: (str) -> ByteArrayTag | None
        if self.contains(name, TagType.ByteArray):
            return self._tags[name]
        return None

    def getStringTag(self, name):
        # type: (str) -> StringTag | None
        if self.contains(name, TagType.String):
            return self._tags[name]
        return None

    def getIntArrayTag(self, name):
        # type: (str) -> IntArrayTag | None
        if self.contains(name, TagType.IntArray):
            return self._tags[name]
        return None

    def put(self, name, tag):
        # type: (str, Tag) -> CompoundTag
        self._tags[name] = tag
        return self

    def putBoolean(self, name, value):
        # type: (str, bool) -> CompoundTag
        self._tags[name] = ByteTag(value and 1 or 0)
        return self

    def putByte(self, name, value):
        # type: (str, int) -> CompoundTag
        self._tags[name] = ByteTag(value)
        return self

    def putShort(self, name, value):
        # type: (str, int) -> CompoundTag
        self._tags[name] = ShortTag(value)
        return self

    def putInt(self, name, value):
        # type: (str, int) -> CompoundTag
        self._tags[name] = IntTag(value)
        return self

    def putInt64(self, name, value):
        # type: (str, int) -> CompoundTag
        self._tags[name] = Int64Tag(value)
        return self

    def putFloat(self, name, value):
        # type: (str, float) -> CompoundTag
        self._tags[name] = FloatTag(value)
        return self

    def putDouble(self, name, value):
        # type: (str, float) -> CompoundTag
        self._tags[name] = DoubleTag(value)
        return self

    def putByteArray(self, name, value):
        # type: (str, list[int]) -> CompoundTag
        self._tags[name] = ByteArrayTag(value)
        return self

    def putString(self, name, value):
        # type: (str, str) -> CompoundTag
        self._tags[name] = StringTag(value)
        return self

    def putList(self, name, value):
        # type: (str, ListTag) -> CompoundTag
        self._tags[name] = value
        return self

    def putCompound(self, name, value):
        # type: (str, CompoundTag) -> CompoundTag
        self._tags[name] = value
        return self

    def putIntArray(self, name, value):
        # type: (str, list[int]) -> CompoundTag
        self._tags[name] = IntArrayTag(value)
        return self

    def clear(self):
        self._tags.clear()

    def append(self, other):
        if not isinstance(other, Tag):
            return NotImplemented
        if not isinstance(other, CompoundTag):
            return NotImplemented
        self._tags.update(other.getTags())

    def isEmpty(self):
        return len(self._tags) == 0

    def rename(self, oldName, newName):
        # type: (str, str) -> bool
        if self.contains(oldName):
            self._tags[newName] = self._tags[oldName]
            del self._tags[oldName]
            return True
        return False

    def size(self):
        return len(self._tags)

    def clone(self):
        return self.copy()

    def copy(self):
        return CompoundTag(self._tags)

    def deepCopy(self):
        return CompoundTag.fromObject(self.toObject())


class IntArrayTag(Tag):

    def __new__(cls, data=None):
        if data is None:
            data = []
        return object.__new__(cls, data)

    def __init__(self, data=None):
        super(IntArrayTag, self).__init__(TagType.IntArray)
        if data is None:
            data = []
        self._data = data

    def __str__(self):
        return "IntArrayTag(value=%s)" % self._data

    def __repr__(self):
        return "IntArrayTag(%s)" % self._data

    def __eq__(self, other):
        if not isinstance(other, Tag):
            return NotImplemented
        if not isinstance(other, IntArrayTag):
            return False
        return self.get() == other.get()

    def __ne__(self, other):
        if not isinstance(other, Tag):
            return NotImplemented
        if not isinstance(other, IntArrayTag):
            return False
        return self.get() != other.get()

    def __len__(self):
        return len(self._data)

    def __getitem__(self, index):
        return self._data[index]

    def __setitem__(self, index, value):
        self._data[index] = value

    def __delitem__(self, index):
        del self._data[index]

    def __iter__(self):
        return iter(self._data)

    def __contains__(self, item):
        return item in self._data

    def copy(self):
        return IntArrayTag(self._data)

