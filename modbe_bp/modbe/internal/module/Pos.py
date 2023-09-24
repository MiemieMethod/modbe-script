# -*- coding: utf-8 -*-
import math


class Pos(object):

    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        if not isinstance(other, Pos):
            return NotImplemented
        return Pos(self.getX() + other.getX(), self.getY() + other.getY(), self.getZ() + other.getZ())

    def __sub__(self, other):
        if not isinstance(other, Pos):
            return NotImplemented
        return Pos(self.getX() - other.getX(), self.getY() - other.getY(), self.getZ() - other.getZ())

    def __mul__(self, other):
        if isinstance(other, Pos):
            return self.getX() * other.getX() + self.getY() * other.getY() + self.getZ() * other.getZ()
        elif isinstance(other, int) or isinstance(other, float):
            return Pos(self.getX() * other, self.getY() * other, self.getZ() * other)
        return NotImplemented

    def __eq__(self, other):
        if not isinstance(other, Pos):
            return NotImplemented
        return self.getX() == other.getX() and self.getY() == other.getY() and self.getZ() == other.getZ()

    def __ne__(self, other):
        if not isinstance(other, Pos):
            return NotImplemented
        return self.getX() != other.getX() or self.getY() != other.getY() or self.getZ() != other.getZ()

    def __hash__(self):
        return hash(self.toTuple())

    def __str__(self):
        return "Pos(x=%s, y=%s, z=%s)" % (self.x, self.y, self.z)

    def __repr__(self):
        return "Pos(%s, %s, %s)" % (self.x, self.y, self.z)

    def __len__(self):
        return (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5

    def __lt__(self, other):
        if not isinstance(other, Pos):
            return NotImplemented
        return len(self) < len(other)

    def __le__(self, other):
        if not isinstance(other, Pos):
            return NotImplemented
        return len(self) <= len(other)

    def __gt__(self, other):
        if not isinstance(other, Pos):
            return NotImplemented
        return len(self) > len(other)

    def __ge__(self, other):
        if not isinstance(other, Pos):
            return NotImplemented
        return len(self) >= len(other)

    def __neg__(self):
        return Pos(-self.x, -self.y, -self.z)

    def __pos__(self):
        return self.clone()

    def __abs__(self):
        return Pos(abs(self.x), abs(self.y), abs(self.z))

    @staticmethod
    def fromTuple(_tuple):
        return Pos(_tuple[0], _tuple[1], _tuple[2])

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getZ(self):
        return self.z

    def toTuple(self):
        return self.x, self.y, self.z

    def toBlockPos(self):
        if isinstance(self, Pos) and not isinstance(self, BlockPos):
            return BlockPos(int(self.x), int(self.y), int(self.z))
        return self

    def clone(self):
        return Pos(self.x, self.y, self.z)

    def distanceTo(self, other):
        if not isinstance(other, Pos):
            return NotImplemented
        return len(other - self)

    def isNan(self):
        return math.isnan(self.x) or math.isnan(self.y) or math.isnan(self.z)

    def isFinite(self):
        return math.isfinite(self.x) and math.isfinite(self.y) and math.isfinite(self.z)

    def isZero(self):
        return self.x == 0 and self.y == 0 and self.z == 0

    def isOne(self):
        return self.x == 1 and self.y == 1 and self.z == 1

    def cross(self, other):
        if not isinstance(other, Pos):
            return NotImplemented
        return Pos(self.getY() * other.getZ() - self.getZ() * other.getY(), self.getZ() * other.getX() - self.getX() * other.getZ(), self.getX() * other.getY() - self.getY() * other.getX())

    def normalize(self):
        length = len(self)
        if length == 0:
            return Pos()
        return Pos(self.getX() / length, self.getY() / length, self.getZ() / length)


class BlockPos(Pos):

    def __init__(self, x=0, y=0, z=0):
        object.__init__(self)
        self.x = int(x)
        self.y = int(y)
        self.z = int(z)

    def __mul__(self, other):
        if isinstance(other, Pos):
            return self.getX() * other.getX() + self.getY() * other.getY() + self.getZ() * other.getZ()
        elif isinstance(other, int) or isinstance(other, float):
            return Pos(int(self.getX() * other), int(self.getY() * other), int(self.getZ() * other))
        return NotImplemented

    @staticmethod
    def fromTuple(_tuple):
        return BlockPos(_tuple[0], _tuple[1], _tuple[2])

    def addAndSet(self, other):
        self.x += other.getX()
        self.y += other.getY()
        self.z += other.getZ()
        return self

    def neighbor(self, facing):
        facingDirection = [
            BlockPos(0, -1, 0),
            BlockPos(0, 1, 0),
            BlockPos(0, 0, -1),
            BlockPos(0, 0, 1),
            BlockPos(-1, 0, 0),
            BlockPos(1, 0, 0)
        ]
        return self + facingDirection[facing]

    def relative(self, facing, distance=1):
        facingDirection = [
            BlockPos(0, -1, 0),
            BlockPos(0, 1, 0),
            BlockPos(0, 0, -1),
            BlockPos(0, 0, 1),
            BlockPos(-1, 0, 0),
            BlockPos(1, 0, 0)
        ]
        return self + facingDirection[facing] * distance

    def toChunkPos(self):
        return ChunkPos(int(self.getX()) >> 4, int(self.getZ()) >> 4)

    def center(self):
        return Pos(self.getX() + 0.5, self.getY() + 0.5, self.getZ() + 0.5)


class ChunkPos(object):

    def __init__(self, x=0, z=0):
        self.x = int(x)
        self.z = int(z)

    def __add__(self, other):
        if not isinstance(other, Pos):
            return NotImplemented
        return Pos(self.getX() + other.getX(), self.getZ() + other.getZ())

    def __sub__(self, other):
        if not isinstance(other, Pos):
            return NotImplemented
        return Pos(self.getX() - other.getX(), self.getZ() - other.getZ())

    def __eq__(self, other):
        if not isinstance(other, Pos):
            return NotImplemented
        return self.getX() == other.getX() and self.getZ() == other.getZ()

    def __ne__(self, other):
        if not isinstance(other, Pos):
            return NotImplemented
        return self.getX() != other.getX() or self.getZ() != other.getZ()

    def __hash__(self):
        return hash(self.toTuple())

    def __str__(self):
        return "ChunkPos(x=%s, z=%s)" % (self.x, self.z)

    def __repr__(self):
        return "ChunkPos(%s, %s)" % (self.x, self.z)

    def __len__(self):
        return (self.x ** 2 + self.z ** 2) ** 0.5

    def __lt__(self, other):
        if not isinstance(other, ChunkPos):
            return NotImplemented
        return len(self) < len(other)

    def __le__(self, other):
        if not isinstance(other, ChunkPos):
            return NotImplemented
        return len(self) <= len(other)

    def __gt__(self, other):
        if not isinstance(other, ChunkPos):
            return NotImplemented
        return len(self) > len(other)

    def __ge__(self, other):
        if not isinstance(other, ChunkPos):
            return NotImplemented
        return len(self) >= len(other)

    def __neg__(self):
        return ChunkPos(-self.x, -self.z)

    def __pos__(self):
        return self.clone()

    def __abs__(self):
        return ChunkPos(abs(self.x), abs(self.z))
    @staticmethod
    def fromTuple(_tuple):
        return ChunkPos(_tuple[0], _tuple[1])

    def getX(self):
        return self.x

    def getZ(self):
        return self.z

    def toBlockPos(self, relativePos=BlockPos()):
        relativePos = relativePos.toBlockPos()
        return BlockPos(float(self.getX() << 4) + relativePos.getX(), relativePos.getY(), float(self.getZ() << 4) + relativePos.getZ())

    def clone(self):
        return Pos(self.x, self.z)

    def toTuple(self):
        return self.x, self.z

