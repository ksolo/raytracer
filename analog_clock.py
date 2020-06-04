from math import radians

from drawing import Canvas
from drawing.formats import PPMFormat
from drawing.transformations import translation, rotation_z, rotation_y, rotation_x
from data_structures import Coordinates, Color

width = 900
height = 900

canvas = Canvas(width, height)
point = Coordinates.point(int(width / 2), int(height / 2), 0)
degrees_of_rotations = 360 / 12
radius = (height / 2) * 0.8
white = Color(1, 1, 1)
translate = translation(0, -radius, 0)

canvas.write_pixel(point.x, point.y, white)
tranlated_point = translate * point
canvas.write_pixel(int(tranlated_point.x), int(tranlated_point.y), white)

PPMFormat(canvas).write()
