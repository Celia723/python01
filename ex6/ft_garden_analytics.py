class Plant:
    class Stats:
        def __init__(self):
            self.grow_calls = 0
            self.age_calls = 0
            self.show_calls = 0

    def __init__(self, name, height, days):
        self.name = name
        self.height = height
        self.days = days
        self.stats = Plant.Stats()
    @staticmethod
    def is_older_than_year(days):
        return days > 365

    @classmethod
    def anonymous(cls):
        return cls("Unknown plant", 0, 0)

    def get_height(self):
        return self.height

    def get_age(self):
        return self.days

    def show(self):
        print(f"{self.name}: {self.height:.1f}cm, {self.days} days old")
        self.stats.show_calls += 1
    def grow(self, new_height):
        self.height = new_height
        self.stats.grow_calls += 1

    def age(self, new_days):
        self.days = new_days
        self.stats.age_calls += 1

class Flower(Plant):
    def __init__(self, name, height, days, color, bloomed):
        super().__init__(name, height, days)
        self.color = color
        self.bloomed = bloomed

    def bloom(self):
        self.bloomed = True

    def show(self):
        super().show()
        print(f"Color: {self.color}")
        if self.bloomed:
            print(f"{self.name}, is blooming beautifully!")
        else:
            print(f"{self.name} has not bloomed yet")
            self.bloom()
        print(f"[statistics for {self.name}]")
        print(f"Stats: {self.stats.grow_calls} grow, {self.stats.age_calls} age, {self.stats.show_calls} show")


class Tree(Plant):
    def __init__(self, name, height, days, diameter):
        super().__init__(name, height, days)
        self.diameter = diameter
        self.stats.shade_calls = 0

    def show(self):
        super().show()
        print(f"Trunk diameter: {self.diameter:.1f}cm")
        """
        print(f"[asking the {self.name} to produce shade]")
        print(f"Tree {self.name} now produces a shade of {self.height:.1f} long and {self.diameter:.1f} cm wide")
"""
    def product_shade(self):
        print(f"[asking the {self.name} to produce shade]")
        print(f"Tree {self.name} now produces a shade of {self.height:.1f}cm long and {self.diameter}cm wide.")
        self.stats.shade_calls += 1

class Vegetable(Plant):
    def __init__(self, name, height, days, season, n_value):
        super().__init__(name, height, days)
        self.season = season
        self.n_value = n_value

    def show(self):
        super().show()
        print(f"Harvest season: {self.season}")
        print(f"Nutritional value: {self.n_value}")

    def set_n_value(self, new_value):
        self.n_value = new_value


if __name__ == "__main__":

    print("=== Garden statistics ===")
    print("=== Check year-old")
    planta = Plant.anonymous()
    print(f"Is 30 days more than a year?-> {planta.is_older_than_year(30)}")
    print(f"Is 400 days more than a year?-> {planta.is_older_than_year(400)}")
    print("\n")
    print("=== Flower")
    rosa = Flower("Rosa", 15, 10, "red", False)
    rosa.show()
    print("[asking the rose to grow and bloom]")
    rosa.grow(23)
    rosa.bloom()
    rosa.show()
    print("\n")
    print("=== Tree")
    oak = Tree("Oak", 200, 365, 5)
    oak.show()
    print(f"[statistics for {oak.name}]")
    print(f"Stats: {oak.stats.grow_calls} grow, {oak.stats.age_calls} age, {oak.stats.show_calls} show \n{oak.stats.shade_calls} shade")
    oak.product_shade()
    print(f"[statistics for {oak.name}]")
    print(f"Stats: {oak.stats.grow_calls} grow, {oak.stats.age_calls} age, {oak.stats.show_calls} show \n{oak.stats.shade_calls} shade")
