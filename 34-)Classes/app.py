# 33. (Classes) and 34.(Constructors) videos same file
# Class names use Pascal style
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        print("move")

    def draw(self):
        print("draw")


'''
33. Video Classes
point1 = Point()
# Attirubites set anywhere in program
point1.x = 10
point1.y = 20
print(point1.x)
point1.draw()

point2 = Point()
point2.x = 1
print(point2.x)
'''

'''
34. Video Constructors
'''

point = Point(10, 20)
point.x = 11
print(point.x)


# Exercise
class Person:

    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hello, my name is {self.name}")


selcuk = Person("Selcuk DINC")
selcuk.talk()

bob = Person("Bob Smith")
bob.talk()