# Author: Xiong Chen
# Date: 2023/11/17
# Description: This script defines the Captain class, which is a subclass of Creature.
# The Captain class is used to manage the location and collection of various objects (like veggies)
# in a game or simulation environment.

from Creature import Creature

class Captain(Creature):
    def __init__(self, x, y):
        """
        Initialize a Captain instance, inheriting from the Creature class.
        :param x: The x-coordinate of the Captain.
        :type x: int
        :param y: The y-coordinate of the Captain.
        :type y: int
        """
        Creature.__init__(self, [x, y], ["Captain", 'V'])
        self._collection_list = []

    def addVeggie(self, veggie_object):
        """
        Add a vegetable object to the Captain's collection.
        :param veggie_object: The vegetable object to be added.
        :type veggie_object: object
        """

        self._collection_list.append(veggie_object)

    def get_collection_list(self):
        """
        Retrieve the list of collected vegetable objects.
        :return: List of collected vegetable objects.
        :rtype: list
        """
        return self._collection_list