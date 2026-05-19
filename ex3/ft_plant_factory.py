class Plant:
    def __init__(self, name: str, height: float, days: int) -> None:
        self.name: str = name
        self.height: float = height
        self.days: int = days

    def show(self) -> None:
        print(
            f"Created: {self.name.capitalize()}: {self.height:.1f}cm, "
            f"{self.days} days old"
        )

    def grow(self) -> None:
        self.height += 0.8

    def age(self) -> None:
        self.days += 1


if __name__ == "__main__":
    print("=== Plant Factory Output ===")
    p1 = Plant("rose", 25.0, 30)
    p2 = Plant("Oak", 200.0, 365)
    p3 = Plant("cactus", 5.0, 90)
    p4 = Plant("Sunflower", 80.0, 45)
    p5 = Plant("Fern", 15.0, 120)

    p1.show()
    p2.show()
    p3.show()
    p4.show()
    p5.show()
