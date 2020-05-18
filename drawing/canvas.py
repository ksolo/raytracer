from data_structures import Color


class Canvas:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self._initialize_pixels()

    def write_pixel(self, col, row, color):
        self.pixels[self._index_for(col, row)] = color

    def pixel_at(self, col, row):
        return self.pixels[self._index_for(col, row)]

    def __iter__(self):
        return iter(self.pixels)

    def _initialize_pixels(self):
        self.pixels = []
        for i in range(self.width * self.height):
            self.pixels.append(Color(0, 0, 0))

    def _index_for(self, col, row):
        return (self.width * row) + col
