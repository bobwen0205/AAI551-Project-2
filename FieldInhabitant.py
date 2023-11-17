class FieldInhabitant:
    def __init__(self, symbol_of_inhabitant):
        # symbol_of_inhabitant = ["Potato", "P"]
        self._symbol_of_inhabitant = symbol_of_inhabitant

    def getSymbol(self):
        return self._symbol_of_inhabitant[1]

    def getName(self):
        return self._symbol_of_inhabitant[0]