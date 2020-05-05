from dataclasses import dataclass


@dataclass
class Coordinates:
    """Base class for creating a 3D coordinate system"""

    x: float
    y: float
    z: float
    w: float

    def is_point(self):
        return self.w == float(1)

    def is_vector(self):
        return self.w == float(0)
