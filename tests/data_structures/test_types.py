from data_structures.types import Coordinates


class TestCoordinates:
    def test_initialization(self):
        coordinates = Coordinates(x=1, y=2, z=3, w=4)

        assert coordinates.x == 1
        assert coordinates.y == 2
        assert coordinates.z == 3
        assert coordinates.w == 4

    def test_is_point(self):
        coordinates = Coordinates(x=0, y=0, z=0, w=1)
        assert coordinates.is_point()
        assert not coordinates.is_vector()

    def test_is_vector(self):
        coordinates = Coordinates(x=0, y=0, z=0, w=0)
        assert not coordinates.is_point()
        assert coordinates.is_vector()
