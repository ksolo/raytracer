from data_structures import Color
from drawing import Canvas
from drawing.formats import PPMFormat


class TestPPMFormat:
    def test_file_headers(self):
        canvas = Canvas(5, 3)
        formatter = PPMFormat(canvas)

        lines = formatter.lines()

        assert lines[0] == "P3"
        assert lines[1] == "5 3"
        assert lines[2] == 255

    def test_constructing_pixel_data(self):
        canvas = Canvas(5, 3)
        c1 = Color(1.5, 0, 0)
        c2 = Color(0, 0.5, 0)
        c3 = Color(-0.5, 0, 1)

        canvas.write_pixel(0, 0, c1)
        canvas.write_pixel(2, 1, c2)
        canvas.write_pixel(4, 2, c3)

        lines = PPMFormat(canvas).lines()

        assert lines[3] == "255 0 0 0 0 0 0 0 0 0 0 0 0 0 0"
        assert lines[4] == "0 0 0 0 0 0 0 128 0 0 0 0 0 0 0"
        assert lines[5] == "0 0 0 0 0 0 0 0 0 0 0 0 0 0 255"
