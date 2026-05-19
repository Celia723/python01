class Plant:
    def __init__(self, name: str, height: float, days: int) -> None:
        self.name: str = name
        self.height: float = height if height >= 0 else 0.0
        self.days: int = days if days >= 0 else 0

    def set_height(self, nw_height: float) -> None:
        if nw_height >= 0:
            self.height = nw_height
            print(f"Height update: {self.height}cm")
        else:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")

    def set_days(self, nw_days: int) -> None:
        if nw_days >= 0:
            self.days = nw_days
            print(f"Age update: {self.days} days")
        else:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")

    def get_height(self) -> float:
        return self.height

    def get_age(self) -> int:
        return self.days

    def show(self) -> None:
        print(f"{self.name}: {self.height:.1f}cm, {self.days} days old")

    def grow(self) -> None:
        self.height += 42

    def age(self) -> None:
        self.days += 20


class Flower(Plant):
    def __init__(self, name: str, height: float,
                 days: int, color: str, bloomed: bool = False) -> None:
        super().__init__(name, height, days)
        self.color: str = color
        self.bloomed: bool = bloomed

    def bloom(self) -> None:
        self.bloomed = True

    def show(self) -> None:
        super().show()
        print(f"Color: {self.color}")
        if self.bloomed:
            print(f"{self.name} is blooming beautifully!")
        else:
            print(f"{self.name} has not bloomed yet")
            print(f"[asking the {self.name} to bloom]")
            self.bloom()


class Tree(Plant):
    def __init__(self, name: str, height: float,
                 days: int, diameter: float) -> None:
        super().__init__(name, height, days)
        self.diameter: float = diameter

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {self.diameter:.1f}cm")
        print(f"[asking the {self.name} to produce shade]")
        print(
            f"Tree {self.name} now produces a shade of "
            f"{self.height:.1f} long and {self.diameter:.1f} cm wide"
        )


class Vegetable(Plant):
    def __init__(self, name: str, height: float,
                 days: int, season: str, n_value: int) -> None:
        super().__init__(name, height, days)
        self.season: str = season
        self.n_value: int = n_value

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self.season}")
        print(f"Nutritional value: {self.n_value}")

    def age(self) -> None:
        self.days += 20

    def grow(self) -> None:
        self.height += 42

    def set_n_value(self, new_value: int) -> None:
        self.n_value = new_value


if __name__ == "__main__":
    print("=== Garden Plant Types ===")

    print("=== Flower ===")
    flower = Flower("Rose", 15, 10, "red", False)
    flower.show()
    flower.show()

    print("\n=== Tree ===")
    tree = Tree("Oak", 200, 365, 5)
    tree.show()

    print("\n=== Vegetable ===")
    tomato = Vegetable("Tomato", 5, 10, "April", 0)
    tomato.show()
    print("[make tomato grow and age for 20 days]")
    tomato.age()
    tomato.grow()
    tomato.set_n_value(20)
    tomato.show()
