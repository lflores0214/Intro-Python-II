# Write a class to hold player information, e.g. what room they are in
# currently.
from room import Room
from item import Light, Food
import os


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
            os.system('clear')
            print(
                f"\n ** There is nothing in this direction ** \n \n {self.room}")

    def check_inventory(self):
        if len(self.items) == 0:
            print(
                f"{self.name} has nothing in their inventory. \n Check rooms with 'c' to look for anything useful ")
        else:
            print(f"{self.name} has: ")
            for item in self.items:
                print(f"{item.name}: {item.description} ")

    def take_item(self, item):
        self.items.append(item)
        self.room.items.remove(item)
        print(f"you took the {item.name}")

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
