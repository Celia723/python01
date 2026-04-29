class Plant:
    def __init__(self, name, height, days):
        self.name = name
        self.height = height
        self.days = days 

    def show(self):
        print(f"{self.name.capitalize()}: {self.height:.1f}cm, {self.days} days old")

    def grow(self):
        self.height += 0.8
    
    def age(self):
        self.days += 1


if __name__ == "__main__":
    p1 = Plant("rose", 25, 30)
    print("=== Garden Plant Growth ===")
    p1.show()
    for i in range(1,8):
        print(f"=== Day {i} ===")
        p1.age()
        p1.grow()
        p1.show()
