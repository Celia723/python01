class Plant:
    def __init__(self, name: str, height: float, days: int) -> None:
        self.name: str = name
        self.height: float = height
        self.days: int = days

    def show(self) -> None:
        print(f"{self.name.capitalize()}: "
              f"{self.height:.1f}cm, {self.days} days old")

    def grow(self) -> None:
        self.height += 0.8

    def age(self) -> None:
        self.days += 1


if __name__ == "__main__":
    p1 = Plant("rose", 25.0, 30)
    initial_height = p1.height
    print("=== Garden Plant Growth ===")
    p1.show()
    for i in range(1, 8):
        print(f"=== Day {i} ===")
        p1.age()
        p1.grow()
        p1.show()

    print(f"Growth this week: {(p1.height - initial_height):.1f}cm")
