from collections import deque


class ColorFormatter:
    def __init__(self, color, scale):
        self.color = color
        self.scale = scale

    def _scale_color(self):
        color = self.color * self.scale
        return [
            self._normalize_color_component(color.red),
            self._normalize_color_component(color.green),
            self._normalize_color_component(color.blue),
        ]

    def _normalize_color_component(self, component):
        if component > 255:
            return 255
        elif component < 0:
            return 0
        else:
            return int(round(component))

    def __repr__(self):
        color_components = [str(component) for component in self._scale_color()]
        return " ".join(color_components)


class PPMFormat:
    PPM_VERSION = "P3"
    COLOR_SCALE = 255
    PIXELS_PER_LINE = 5

    def __init__(self, drawable):
        self.drawable = drawable

    def lines(self):
        return self._header() + self._pixel_lines() + self._new_line()

    def _header(self):
        width = self.drawable.width
        height = self.drawable.height

        return [self.PPM_VERSION, f"{width} {height}", str(self.COLOR_SCALE)]

    def _pixel_lines(self):
        formatted_pixels = self._formatted_pixels()

        lines = []
        for _ in range(int(len(formatted_pixels) / self.PIXELS_PER_LINE)):
            line = [formatted_pixels.popleft() for _ in range(self.PIXELS_PER_LINE)]
            lines.append(" ".join(line))
        if len(formatted_pixels):
            lines.append(" ".join(formatted_pixels))

        return lines

    def _formatted_pixels(self):
        return deque(
            [str(ColorFormatter(pixel, self.COLOR_SCALE)) for pixel in self.drawable]
        )

    def _new_line(self):
        return ["\n"]
