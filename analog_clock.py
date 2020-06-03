from math import radians

from drawing import Canvas
from drawing.formats import PPMFormat
from drawing.transformations import translation, rotation_z
from data_structures import Coordinates, Color

width = 900
height = 900

canvas = Canvas(width, height)
point = Coordinates.point(width / 2, height / 2, 0)
degrees_of_rotations = 360 / 12
radius = (height / 2) * 0.8
white = Color(1, 1, 1)

for i in range(12):
    translate = translation(0, radius, 0)
    rotations = rotation_z(radians(int(i * degrees_of_rotations)))

    pixel_location = [
        int(coordinate) for coordinate in (rotations * (translate * point))
    ]
    import pdb

    pdb.set_trace()

    canvas.write_pixel(pixel_location[0], pixel_location[1], white)

PPMFormat(canvas).write()
