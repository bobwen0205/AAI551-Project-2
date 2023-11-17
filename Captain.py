from Creature import Creature

class Captain(Creature):
    def __init__(self, x, y):
        Creature.__init__(self, [x, y], ["Captain", 'V'])
        self._collection_list = []

    def addVeggie(self, veggie_object):
        self._collection_list.append(veggie_object)

    def get_collection_list(self):
        return self._collection_list