from math import sqrt

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

    def magnitude(self):
        x_squared = self.x ** 2
        y_squared = self.y ** 2
        z_squared = self.z ** 2

        return sqrt(x_squared + y_squared + z_squared)

    def normalize(self):
        magnitude = self.magnitude()
        x = self.x / magnitude
        y = self.y / magnitude
        z = self.z / magnitude

        return self.__class__.vector(x, y, z)

    def dot_product(self, vector):
        xs = self.x * vector.x
        ys = self.y * vector.y
        zs = self.z * vector.z
        ws = self.w * vector.w
        return xs + ys + zs + ws

    def cross_product(self, vector):
        x = self.y * vector.z - self.z * vector.y
        y = self.z * vector.x - self.x * vector.z
        z = self.x * vector.y - self.y * vector.x

        return self.__class__.vector(x, y, z)

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

    def __iter__(self):
        return iter([self.x, self.y, self.z, self.w])
