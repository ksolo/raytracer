from data_structures import Color
from drawing import Canvas


class TestCanvas:
    def test_initialization_of_width_and_height(self):
        canvas = Canvas(10, 20)

        assert canvas.width == 10
        assert canvas.height == 20

    def test_initialization_all_pixels_set_to_black(self):
        canvas = Canvas(10, 20)

        for pixel in canvas:
            assert pixel == Color(0, 0, 0)

    def test_writing_pixel_to_canvas(self):
        canvas = Canvas(10, 20)
        red = Color(1, 0, 0)

        canvas.write_pixel(2, 3, red)

        assert canvas.pixel_at(2, 3) == red
