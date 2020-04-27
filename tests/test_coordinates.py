from coordinates import Coordinates


class TestCoordinates:
    def test_initialization(self):
        coordinates = Coordinates(1, 2, 3)
        assert coordinates.x == 1
        assert coordinates.y == 2
        assert coordinates.z == 3
