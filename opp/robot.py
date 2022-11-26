class  Robot:
    def __init__(self, name, color, weight):
        self.name = name
        self.color = color
        self.weight = weight        

    def introduce_self(self):
        print("My name is "+ self.name)


class Person:
    def __init__(self, name, personality, is_sitting):
        self.name = name
        self.personality =personality
        self.is_sitting = is_sitting

    def sit_down(self):
        self.is_sitting = True

    def stand_up(self):
        self.is_sitting = False


p1 = Person("Ngoc", "aggressive", False)

# r1 = Robot()
# r1.name = "Tom"
# r1.color = "red"
# r1.weight = 30


# r2 = Robot()
# r2.name = "jery"
# r2.color = "blue"
# r2.weight = 18

r1 = Robot("Tom", "red", 30)
r2= Robot("jery", "blue", 18)

# r1.introduce_self()
# r2.introduce_self()