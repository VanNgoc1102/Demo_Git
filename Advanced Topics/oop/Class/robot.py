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

r1 = Robot("Tom", "red", 30)
r2= Robot("jery", "blue", 18)

print(r1.introduce_self())
print(r2.introduce_self())