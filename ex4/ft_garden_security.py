class Plant:
    def __init__(self, name: str, height: float, days: int) -> None:
        self.name: str = name
        if height >= 0:
            self.height: float = height
        else:
            self.height = 0.0
        if days >= 0:
            self.days: int = days
        else:
            self.days = 0

    def set_height(self, nw_height: float) -> None:
        if nw_height >= 0:
            self.height = nw_height
            print(f"Height update: {self.height}cm")
        else:
            print(f"{self.name.capitalize()}: Error, height can't be negative")
            print("Height update rejected")

    def set_days(self, nw_days: int) -> None:
        if nw_days >= 0:
            self.days = nw_days
            print(f"Age update: {self.days} days")
        else:
            print(f"{self.name.capitalize()}: Error, age can't be negative")
            print("Age update rejected")

    def get_height(self) -> float:
        return self.height

    def get_age(self) -> int:
        return self.days

    def show(self) -> None:
        print(
            f"Plant created: {self.name.capitalize()}: {self.height:.1f}cm, "
            f"{self.days} days old"
        )

    def grow(self) -> None:
        self.height += 0.8

    def age(self) -> None:
        self.days += 1


if __name__ == "__main__":
    print("=== Garden Security System ===")
    p1 = Plant("Rose", 15.0, 10)
    p1.show()

    print("\n")

    p1.set_height(25.0)
    p1.set_days(30)

    print("\n")

    p1.set_height(-25.0)
    p1.set_days(-30)

    print("\n")
    print(
        f"Current state: {p1.name}: "
        f"{p1.get_height():.1f}cm, {p1.get_age()} days old")
