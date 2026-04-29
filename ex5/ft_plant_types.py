class Plant:
    def __init__(self, name, height, days):
        self.name = name
        if(height >= 0):
            self.height = height
        if (days >= 0):
            self.days = days
    
    def set_height(self, nw_height):
        if (nw_height >= 0):
            self.height = nw_height
            print(f"Height update: {self.height}cm")
        else:
            print(f"{self.name.capitalize()}: Error, height can't be negative")
            print("Height update rejected")
    
    def set_days(self, nw_days):
        if (nw_days >= 0):
            self.days = nw_days
            print(f"Age update: {self.height} days")
        else:
            print(f"{self.name.capitalize()}: Error, age can't be negative")
            print("Age update rejected")
    
    def get_height(self):
        return self.height
    
    def get_age(self):
        return self.days

    def show(self):
        print(f"Plant created: {self.name.capitalize()}: {self.height:.1f}cm, {self.days} days old")

    def grow(self):
        self.height += 0.8
    
    def age(self):
        self.days += 1




if __name__ == "__main__":
    

