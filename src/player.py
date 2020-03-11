# Write a class to hold player information, e.g. what room they are in
# currently.
from room import Room
class Player():
    def __init__(self, name, room, items):
        self.name = name
        self.room = room
        self.items = []
    def travel(self, room, direction):
        if getattr(room, f"{direction}_to") != None:
            newRoom = getattr(room, f"{direction}_to")
            self.room = newRoom
        else:
            print("\n ** There is nothing in this direction ** ")
    def __repr__(self):
        return self.name