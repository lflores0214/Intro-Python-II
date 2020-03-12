# Implement a class to hold room information. This should have name and
# description attributes.
import os

class Room():
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.items = []

        self.n_to = None
        self.s_to = None
        self.w_to = None
        self.e_to = None

    def __str__(self):
        os.system('clear')
        s = "**************"
        s += "\n\n"
        s += f"{self.name}"
        s += "\n\n"
        s += f"{self.description}"
        s += "\n\n"
        s += f"{self.get_pathways()}"
        s += "\n\n"
        s += "**************"
        return str(s)

    def get_pathways(self):
        pathways = []
        if self.n_to:
            pathways.append('n')
        if self.s_to:
            pathways.append('s')
        if self.w_to:
            pathways.append('w')
        if self.e_to:
            pathways.append('e')
        return pathways

    def check_items(self):
        print(f"{self.name} has: ")
        for item in self.items:
            print(item.name)
