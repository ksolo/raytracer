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
