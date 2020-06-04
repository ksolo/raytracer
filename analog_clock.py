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
white = Color(1, 1, 1)

point = Coordinates.point(int(width / 2), int(height / 2), 0)
translate = translation(0, -radius, 0)

for i in range(12):
    rotate = rotation_z(radians(i * degrees_of_rotations))
    rotated_point = rotate * (translate * point)

    canvas.write_pixel(int(rotated_point.x), int(rotated_point.y), white)


PPMFormat(canvas).write()
