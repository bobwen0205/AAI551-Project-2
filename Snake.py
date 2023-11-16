# Author: Mingzhi Wen
# Date: Nov 16, 2023
# Description: This program is the Snake class (bonus part) of game Captain Veggie

from Creature import Creature

class Snake(Creature):
    def __init__(self, x, y):
        # Call the __init__ method of the super class (Creature) to initialize the Snake
        Creature.__init__(self, [x, y], ["Snake", 'S'])