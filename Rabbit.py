# Author: Xiong Chen
# Date: 2023/11/17
# Description: This script defines the Rabbit class, which is a subclass of Creature.

from Creature import Creature

class Rabbit(Creature):
    def __init__(self, x, y):
        """
        Initialize a Rabbit instance, inheriting from the Creature class.
        :param x: The x-coordinate of the Rabbit.
        :type x: int
        :param y: The y-coordinate of the Rabbit.
        :type y: int
        """
        Creature.__init__(self, [x, y], ["Rabbit", "R"])