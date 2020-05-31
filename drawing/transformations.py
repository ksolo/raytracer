from math import sin, cos

from data_structures import Matrix


def translation(x, y, z):
    return Matrix([[1, 0, 0, x], [0, 1, 0, y], [0, 0, 1, z], [0, 0, 0, 1]])


def scaling(x, y, z):
    return Matrix([[x, 0, 0, 0], [0, y, 0, 0], [0, 0, z, 0], [0, 0, 0, 1]])


def rotation_x(rads):
    return Matrix(
        [
            [1, 0, 0, 0],
            [0, cos(rads), -sin(rads), 0],
            [0, sin(rads), cos(rads), 0],
            [0, 0, 0, 1],
        ]
    )