from FieldInhabitant import FieldInhabitant

class Creature(FieldInhabitant):
    def __init__(self, xy_coordinates, symbol_of_creature):
        FieldInhabitant.__init__(self, symbol_of_creature)
        self._xy_coordinates = xy_coordinates

    def get_coordinate(self):
        return self._xy_coordinates

    def set_new_xy(self, x, y):
        self._xy_coordinates = [x, y]