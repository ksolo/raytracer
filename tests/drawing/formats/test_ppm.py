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
