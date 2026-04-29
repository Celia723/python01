
class Plant:
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age

if __name__ == "__main__": 
    print("=== Welcome to My Garden ===")
    p1 = Plant("Rose", 25, 30)
    print(f"Plant: {p1.name.capitalize()} \n"
          f"Height: {p1.height}cm \n"
          f"Age: {p1.age} days \n")
    print("=== End of Program ===")
    
