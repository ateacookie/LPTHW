class Inventory(object):

    def __init__(self):
        self.inventory = []

    def add(self, thing):
        self.inventory.append(thing)

    def remove(self, thing):
        self.inventory.remove(thing)

    def printInventory(self):
        return str(self.inventory)

INV = Inventory()


