class Player:
    def __init__(self, name):
        self.name = name
        self.inventory = Inventory()
        print ("player pubg")


class Item:
    def __init__(self, name):
        self.name = name


class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)
        print ("item", item.name)

    def remove_item(self, item):
        self.items.remove(item)


player = Player("player pubg")
sword = Item("akm")
shield = Item("pan")
player.inventory.add_item(sword)
player.inventory.add_item(shield)
player.inventory.items  # output: [sword, shield]
