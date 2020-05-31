from math import sin, cos, radians

from data_structures import Matrix


def translation(x, y, z):
    return Matrix([[1, 0, 0, x], [0, 1, 0, y], [0, 0, 1, z], [0, 0, 0, 1]])


def scaling(x, y, z):
    return Matrix([[x, 0, 0, 0], [0, y, 0, 0], [0, 0, z, 0], [0, 0, 0, 1]])


def rotation_x(radians):
    return Matrix(
        [
            [1, 0, 0, 0],
            [0, cos(radians), -sin(radians), 0],
            [0, sin(radians), cos(radians), 0],
            [0, 0, 0, 1],
        ]
    )
