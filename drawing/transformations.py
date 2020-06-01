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


def rotation_y(rads):
    return Matrix(
        [
            [cos(rads), 0, sin(rads), 0],
            [0, 1, 0, 0],
            [-sin(rads), 0, cos(rads), 0],
            [0, 0, 0, 1],
        ]
    )


def rotation_z(rads):
    return Matrix(
        [
            [cos(rads), -sin(rads), 0, 0],
            [sin(rads), cos(rads), 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1],
        ]
    )


def shearing(xy=0, xz=0, yx=0, yz=0, zx=0, zy=0):
    return Matrix([[1, xy, xz, 0], [yx, 1, yz, 0], [zx, zy, 1, 0], [0, 0, 0, 1]])
