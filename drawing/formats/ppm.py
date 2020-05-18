from collections import deque


class ColorFormatter:
    def __init__(self, color, scale):
        self.color = color
        self.scale = scale

    def _scale_color(self):
        return [
            max(self.scale, int(self.color.red * self.scale)),
            max(self.scale, int(self.color.red * self.scale)),
            max(self.scale, int(self.color.red * self.scale)),
        ]

    def __repr__(self):
        return " ".join(self._scale_color())


class PPMFormat:
    PPM_VERSION = "P3"
    COLOR_SCALE = 255
    PIXELS_PER_LINE = 5

    def __init__(self, drawable):
        self.drawable = drawable

    def lines(self):
        return self._header() + self._pixel_lines()

    def _header(self):
        width = self.drawable.width
        height = self.drawable.height

        return [self.PPM_VERSION, f"{width} {height}", self.COLOR_SCALE]

    def _pixed_lines(self):
        formatted_pixels = self._formatted_pixels()
        lines = []

        for _ in range(len(formatted_pixels) / self.PIXELS_PER_LINE):
            line = [formatted_pixels.popleft() for _ in self.PIXELS_PER_LINE]
            lines.append(" ".join(line))

        lines.extend(" ".join(formatted_pixels))

        return lines

    def _formatted_pixels(self):
        return deque(
            [str(ColorFormatter(pixel, self.COLOR_SCALE)) for pixel in self.drawable]
        )
