from FieldInhabitant import FieldInhabitant

class Veggie(FieldInhabitant):
    # name_symbol_of_vegetable = ["potato", "P"]
    # points_of_vegetable = 1
    def __init__(self, name_symbol_of_vegetable, points_of_vegetable):
        FieldInhabitant.__init__(self, name_symbol_of_vegetable)
        self._points_of_vegetable = points_of_vegetable

    def __str__(self):
        #G: Garlic 5 points
        symbol = self._symbol_of_inhabitant[1]
        name = self._symbol_of_inhabitant[0]
        point = self._points_of_vegetable
        return f"{symbol}: {name} {point} points"

    def getPoints(self):
        return self._points_of_vegetable