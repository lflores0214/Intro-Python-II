# Write a class to hold player information, e.g. what room they are in
# currently.
from room import Room
from item import Light, Food


class Player():
    def __init__(self, name, room):
        self.name = name
        self.room = room
        self.items = []
        self.hp = 100

    def travel(self, room, direction):
        if getattr(self.room, f"{direction}_to"):
            self.room = getattr(self.room, f"{direction}_to")
            print(self.room)
        else:
            print("\n ** There is nothing in this direction ** ")

    def check_inventory(self):
        print(f"{self.name} has: ")
        for item in self.items:
            print(item.name)

    def eat(self, food_item):
        if not isinstance(food_item, Food):
            print(f"you cannot eat {food_item.name}")
        elif self.hp == 100:
            print(f"{self.name} is already at full health")
        else:
            self.hp += food_item.energy
            print(
                f"{self.name} has eaten {food_item.name}, your hp is now {self.hp} ")
            self.items.remove(food_item)
