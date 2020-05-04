from data_structures.types import Coordinates


class TestCoordinatesInitializations:
    def test_sets_x_y_z_w(self):
        coordinates = Coordinates(x=1, y=2, z=3, w=4)

        assert coordinates.x == 1
        assert coordinates.y == 2
        assert coordinates.z == 3
        assert coordinates.w == 4
