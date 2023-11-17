# Author: Xiong Chen
# Date: 2023/11/17
# Description: This script defines the Creature class, which is a subclass of FieldInhabitant.

from FieldInhabitant import FieldInhabitant

class Creature(FieldInhabitant):
    def __init__(self, xy_coordinates, symbol_of_creature):
        """
        Initialize a Creature instance, inheriting from the FieldInhabitant class.
        :param xy_coordinates: The initial x and y coordinates of the Creature.
        :type xy_coordinates: list
        :param symbol_of_creature: A symbol representing the Creature.
        :type symbol_of_creature: str
        """
        FieldInhabitant.__init__(self, symbol_of_creature)
        self._xy_coordinates = xy_coordinates

    def get_coordinate(self):
        """
        Retrieve the current coordinates of the Creature.
        :return: The current x and y coordinates.
        :rtype: list
        """
        return self._xy_coordinates

    def set_new_xy(self, x, y):
        """
        Set new x and y coordinates for the Creature.
        :param x: The new x-coordinate.
        :type x: int
        :param y: The new y-coordinate.
        :type y: int
        """
        self._xy_coordinates = [x, y]