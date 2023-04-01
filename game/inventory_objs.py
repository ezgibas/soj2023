debug = True
# An item in the inventory
# name (string): name of the item
# count (int): how many of the item


class Item:

    # constructor
    def __init__(self, name, description=""):
        self.name = name
        self.description = description
        self.count = 0

    # equality operator
    # two items are the same if they have the same name
    def __eq__(self, other):
        return self.name == other.name

    # string representation of the item
    def __str__(self):
        return self.name + " (" + str(self.count) + ")"

    # increase the count of the item
    def increase(self):
        self.count += 1

# Inventory of the player
# items (list of Item): items in the inventory


class Inventory:
    # constructor
    def __init__(self, items):
        self.items = []

    # string representation of the inventory
    def __str__(self):
        result = "Inventory: \n"
        for item in self.items:
            result += str(item) + "\n"
        return result

    # add an item to the inventory
    # item (Item): item to add
    def additem(self, item):
        self.items.append(item)


# Function object for adding an item
class AddItem:
    def __init__(self, item, inventory):
        self.item = item
        self.inventory = inventory

    # callable:
    # item (Item): item to add
    # inventory (Inventory): inventory to add the item to
    def __call__(self):
        if self.item in self.inventory.items:
            self.item.increase()
        else:
            self.item.increase()
            self.inventory.additem(self.item)
        if (debug):
            print(self.inventory)
