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

    def test_point_conveniece_constructor(self):
        coordinates = Coordinates.point(1, 2, 3)
        assert coordinates.is_point()
        assert not coordinates.is_vector()

    def test_vector_conveniece_constructor(self):
        coordinates = Coordinates.vector(1, 2, 3)
        assert not coordinates.is_point()
        assert coordinates.is_vector()

    def test_coordinates_addition(self):
        coord_1 = Coordinates(x=3, y=-2, z=5, w=1)
        coord_2 = Coordinates(x=-2, y=3, z=1, w=0)

        result = coord_1 + coord_2
        assert result == Coordinates(x=1, y=1, z=6, w=1)
