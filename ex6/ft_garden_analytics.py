from typing import Any


class Plant:
    class Stats:
        def __init__(self) -> None:
            self.grow_calls: int = 0
            self.age_calls: int = 0
            self.show_calls: int = 0
            self.shade_calls: int = 0

    def __init__(self, name: str, height: float, days: int) -> None:
        self.name: str = name
        self.height: float = height
        self.days: int = days
        self.stats: Plant.Stats = Plant.Stats()

    @staticmethod
    def is_older_than_year(days: int) -> bool:
        return days > 365

    @classmethod
    def anonymous(cls) -> "Plant":
        return cls("Unknown plant", 0.0, 0)

    def get_height(self) -> float:
        return self.height

    def get_age(self) -> int:
        return self.days

    def show(self) -> None:
        print(f"{self.name}: {self.height:.1f}cm, {self.days} days old")
        self.stats.show_calls += 1

    def grow(self, new_height: float) -> None:
        self.height = new_height
        self.stats.grow_calls += 1

    def age(self, new_days: int) -> None:
        self.days = new_days
        self.stats.age_calls += 1


class Flower(Plant):
    def __init__(self, name: str, height: float,
                 days: int, color: str, bloomed: bool) -> None:
        super().__init__(name, height, days)
        self.color: str = color
        self.bloomed: bool = bloomed

    def bloom(self) -> None:
        self.bloomed = True

    def show(self) -> None:
        super().show()
        print(f"Color: {self.color}")
        if self.bloomed:
            print(f"{self.name}, is blooming beautifully!")
        else:
            print(f"{self.name} has not bloomed yet")
            self.bloom()


class Tree(Plant):
    def __init__(self, name: str, height: float,
                 days: int, diameter: float) -> None:
        super().__init__(name, height, days)
        self.diameter: float = diameter

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self.diameter:.1f}cm")

    def product_shade(self) -> None:
        print(f"[asking the {self.name} to produce shade]")
        print(f"Tree {self.name} now produces a shade of {self.height:.1f}"
              f"cm long and {self.diameter}cm wide.")
        self.stats.shade_calls += 1


class Vegetable(Plant):
    def __init__(self, name: str, height: float,
                 days: int, season: str, n_value: Any) -> None:
        super().__init__(name, height, days)
        self.season: str = season
        self.n_value: Any = n_value

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self.season}")
        print(f"Nutritional value: {self.n_value}")

    def set_n_value(self, new_value: Any) -> None:
        self.n_value = new_value


class Seed(Flower):
    def __init__(self, name, height, days, color, bloomed, num) -> None:
        super().__init__(name, height, days, color, bloomed)
        self.num = num

    def show(self) -> None:
        super().show()
        print(f"Seeds: {self.num}")

    def put_number_seed(self, number) -> None:
        if (self.bloomed is True):
            self.num = number


def display_analitics_values(plant: Plant) -> None:
    print(f"[statistics for {plant.name}]")
    print(f"Stats: {plant.stats.grow_calls} grow, "
          f"{plant.stats.age_calls} age, {plant.stats.show_calls} show")


if __name__ == "__main__":
    print("=== Garden statistics ===")
    print("=== Check year-old")
    planta = Plant.anonymous()
    print(f"Is 30 days more than a year?-> {planta.is_older_than_year(30)}")
    print(f"Is 400 days more than a year?-> {planta.is_older_than_year(400)}")
    print("\n")

    print("=== Flower")
    rosa = Flower("Rosa", 15.0, 10, "red", False)
    rosa.show()
    display_analitics_values(rosa)
    print("[asking the rose to grow and bloom]")
    rosa.grow(23.0)
    rosa.bloom()
    rosa.show()
    display_analitics_values(rosa)
    print("\n")

    print("=== Tree")
    oak = Tree("Oak", 200.0, 365, 5.0)
    oak.show()
    print(f"[statistics for {oak.name}]")
    print(f"Stats: {oak.stats.grow_calls} grow, {oak.stats.age_calls} age,"
          f"{oak.stats.show_calls} show \n{oak.stats.shade_calls} shade")
    oak.product_shade()
    print(f"[statistics for {oak.name}]")
    print(f"Stats: {oak.stats.grow_calls} grow, {oak.stats.age_calls} age,"
          f"{oak.stats.show_calls} show \n{oak.stats.shade_calls} shade")

    print()
    print("=== Seed")
    seed = Seed("Sunflower", 80, 45, "yellow", False, 0)
    seed.show()
    print("[make sunflower grow, age and bloom]")
    seed.put_number_seed(42)
    seed.grow(110)
    seed.age(65)
    seed.bloom()
    seed.show()
    display_analitics_values(seed)
    print("\n")

    print("=== Anonymous")
    anonymous = Plant.anonymous()
    anonymous.show()
    display_analitics_values(anonymous)
