

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
