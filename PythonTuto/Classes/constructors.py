# define a class
class Point:
    # this is a constructor
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def move(self):
        print("Move")
    def draw(self):
        print("Draw")


# can't create an object without x, y
point1 = Point(10, 15)
print(str(point1.x) + " " + str(point1.y))

# update value
point1.x = 5
point1.y = 12
print(str(point1.x) + " " + str(point1.y))