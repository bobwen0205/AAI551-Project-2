# Author: Xiong Chen
# Date: 2023/11/17
# Description: This script defines the FieldInhabitant class.

class FieldInhabitant:
    def __init__(self, symbol_of_inhabitant):
        """
        Initialize a FieldInhabitant instance.
        :param symbol_of_inhabitant: A list containing the name and symbol of the inhabitant.
        :type symbol_of_inhabitant: list
        """
        # symbol_of_inhabitant = ["Potato", "P"]
        self._symbol_of_inhabitant = symbol_of_inhabitant

    def getSymbol(self):
        """
        Retrieve the symbol of the inhabitant.
        :return: The symbol of the inhabitant.
        :rtype: str
        """
        return self._symbol_of_inhabitant[1]

    def getName(self):
        """
        Retrieve the name of the inhabitant.
        :return: The name of the inhabitant.
        :rtype: str
        """
        return self._symbol_of_inhabitant[0]