from dataclasses import dataclass
from numbers import Number


@dataclass
class Color:
    """ Base class for storing and manipulating colors """

    red: float
    green: float
    blue: float

    def __add__(self, other):
        return self.__class__(
            self.red + other.red, self.green + other.green, self.blue + other.blue
        )

    def __sub__(self, other):
        return self.__class__(
            self.red - other.red, self.green - other.green, self.blue - other.blue
        )

    def __mul__(self, other):
        if isinstance(other, Number):
            return self.__class__(
                self.red * other, self.green * other, self.blue * other
            )
        else:
            return self.__class__(
                self.red * other.red, self.green * other.green, self.blue * other.blue
            )

