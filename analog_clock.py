from math import radians

from drawing import Canvas
from drawing.formats import PPMFormat
from drawing.transformations import translation, rotation_z, rotation_y, rotation_x
from data_structures import Coordinates, Color

width = 900
height = 900

canvas = Canvas(width, height)
degrees_of_rotations = 360 / 12
radius = (height / 2) * 0.8

point = Coordinates.point(0, 0, 0)
translate = translation(width / 2, height / 2, 0)

for i in range(12):
    colors = [Color(1, 0, 0), Color(0, 1, 0), Color(0, 0, 1)]
    degrees = i * degrees_of_rotations
    print(f"degrees: {degrees}")
    rotate = rotation_z(radians(degrees))
    rotated_point = rotate * (translate * point)

    print(f"rotated_point: {rotated_point.x} {rotated_point.y} {rotated_point.z}")

    canvas.write_pixel(int(rotated_point.x), int(rotated_point.y), colors[i % 3])


PPMFormat(canvas).write()
