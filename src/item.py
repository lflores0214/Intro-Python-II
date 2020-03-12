

class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def on_take(self):
        print(f"you took the {self.name} \n {self.description}")

    def on_drop(self):
        print(f"you dropped the {self.name}")

        def __repr__(self):
            return self.name


class Light(Item):
    def __init__(self, name, description, is_lit):
        self.name = name
        self.description = description
        self.is_lit = is_lit

    def ignite(self):
        self.is_lit = True
        print(f"You lit the {self.name}")

    def extinguish(self):
        self.is_lit = False
        print(f"You extinguished the {self.name}")


class Food(Item):
    def __init__(self, name, description, energy):
        super().__init__(name, description)
        self.energy = energy
