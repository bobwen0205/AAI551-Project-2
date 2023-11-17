# Author: Xiong Chen
# Date: 2023/11/17
# Description: This script defines the Veggie class, which is a subclass of FieldInhabitant.

from FieldInhabitant import FieldInhabitant

class Veggie(FieldInhabitant):
    # name_symbol_of_vegetable = ["potato", "P"]
    # points_of_vegetable = 1
    def __init__(self, name_symbol_of_vegetable, points_of_vegetable):
        """
        Initialize a Veggie instance, inheriting from the FieldInhabitant class.
        :param name_symbol_of_vegetable: A list containing the name and symbol of the vegetable.
        :type name_symbol_of_vegetable: list
        :param points_of_vegetable: The points associated with the vegetable.
        :type points_of_vegetable: int
        """
        FieldInhabitant.__init__(self, name_symbol_of_vegetable)
        self._points_of_vegetable = points_of_vegetable

    def __str__(self):
        """
        Return a string representation of the Veggie instance.
        :return: String representation of the vegetable with its symbol, name, and points.
        :rtype: str
        """
        #G: Garlic 5 points
        symbol = self._symbol_of_inhabitant[1]
        name = self._symbol_of_inhabitant[0]
        point = self._points_of_vegetable
        return f"{symbol}: {name} {point} points"

    def getPoints(self):
        """
        Retrieve the points of the vegetable.
        :return: The points of the vegetable.
        :rtype: int
        """
        return self._points_of_vegetable