class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name: str = name
        self.height: int = height
        self.age: int = age

    def show(self) -> None:
        print(f"{self.name.capitalize()}: {self.height}cm, "
              f"{self.age} days old")


if __name__ == "__main__":
    print("=== Garden Plant Registry ===")
    p1 = Plant("rose", 25, 30)
    p2 = Plant("sunflower", 80, 45)
    p3 = Plant("cactus", 15, 120)

    p1.show()
    p2.show()
    p3.show()
