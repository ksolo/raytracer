from dataclasses import dataclass


@dataclass
class Coordinates:
    """Base class for creating a 3D coordinate system"""

    x: float
    y: float
    z: float
    w: float

    @classmethod
    def point(cls, x, y, z):
        return cls(x=x, y=y, z=z, w=1)

    @classmethod
    def vector(cls, x, y, z):
        return cls(x=x, y=y, z=z, w=0)

    def is_point(self):
        return self.w == float(1)

    def is_vector(self):
        return self.w == float(0)

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        z = self.z + other.z
        w = self.w + other.w

        return self.__class__(x=x, y=y, z=z, w=w)

    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        z = self.z - other.z
        w = self.w - other.w

        return self.__class__(x=x, y=y, z=z, w=w)

    def __neg__(self):
        return self.__class__(x=-self.x, y=-self.y, z=-self.z, w=-self.w)

    def __mul__(self, other):
        return self.__class__(
            x=self.x * other, y=self.y * other, z=self.z * other, w=self.w * other
        )

    def __truediv__(self, other):
        return self.__class__(
            x=self.x / other, y=self.y / other, z=self.z / other, w=self.w / other
        )
