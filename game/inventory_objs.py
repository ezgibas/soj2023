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
        if not isinstance(other, Item):
            return False
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

    # reset the inventory
    def reset(self):
        self.items = []

    # check if the inventory has an item
    # item (Item): item to check
    def hasitem(self, item):
        return item in self.items

    # add an item to the inventory
    # item (Item): item to add
    def additem(self, item):
        if self.hasitem(item):
            item.increase()
        else:
            item.increase()
            self.items.append(item)
        if (debug):
            print(self)


# # Function object for adding an item
# class AddItem:
#     def __init__(self, item, inventory):
#         self.item = item
#         self.inventory = inventory

#     # callable:
#     # item (Item): item to add
#     # inventory (Inventory): inventory to add the item to
#     def __call__(self):
#         self.inventory.additem(self.item)
#         if (debug):
#             print(self.inventory)
