# Write a class to hold player information, e.g. what room they are in
# currently.
from room import Room


class Player():
    def __init__(self, name, room):
        self.name = name
        self.room = room
        self.items = []

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
