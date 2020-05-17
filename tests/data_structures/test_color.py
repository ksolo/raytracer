from data_structures import Color


class TestColor:
    def test_initialization(self):
        color = Color(-0.5, 0.4, 1.7)

        assert color.red == -0.5
        assert color.green == 0.4
        assert color.blue == 1.7

    def test_adding_colors(self):
        c1 = Color(0.9, 0.6, 0.75)
        c2 = Color(0.7, 0.1, 0.25)

        result = c1 + c2

        assert result == Color(1.6, 0.7, 1.0)

    def test_subtracting_colors(self):
        c1 = Color(0.9, 0.6, 0.75)
        c2 = Color(0.7, 0.1, 0.25)

        result = c1 - c2

        assert round(result.red, 2) == 0.2
        assert round(result.green, 2) == 0.5
        assert round(result.blue, 2) == 0.5

    def test_multiplying_by_scalar(self):
        color = Color(0.2, 0.3, 0.4)

        result = color * 2

        assert result == Color(0.4, 0.6, 0.8)

    def test_mult_by_other_color(self):
        c1 = Color(1, 0.2, 0.4)
        c2 = Color(0.9, 1, 0.1)

        result = c1 * c2

        assert round(result.red, 2) == 0.9
        assert round(result.green, 2) == 0.2
        assert round(result.blue, 2) == 0.04
