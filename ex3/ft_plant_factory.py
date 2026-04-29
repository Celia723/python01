class Plant:
    def __init__(self, name, height, days):
        self.name = name
        self.height = height
        self.days = days 

    def show(self):
        print(f"Created: {self.name.capitalize()}: {self.height:.1f}cm, {self.days} days old")

    def grow(self):
        self.height += 0.8
    
    def age(self):
        self.days += 1


if __name__ == "__main__":
    print("=== Plant Factory Output ===")
    p1 = Plant("rose", 25, 30)
    p2 = Plant("Oak", 200, 365)
    p3 = Plant("catus", 5, 90)
    p4 = Plant("Sunflower", 80, 45)
    p5 = Plant("Fern", 15, 120)

    p1.show()
    p2.show()
    p3.show()
    p4.show()
    p5.show()