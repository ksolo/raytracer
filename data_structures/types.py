from dataclasses import dataclass


@dataclass
class Coordinates:
    """Base class for creating a 3D coordinate system"""

    x: float
    y: float
    z: float
    w: float
