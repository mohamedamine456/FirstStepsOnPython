# define a class
class Point:
    def move(self):
        print("Move")
    def draw(self):
        print("Draw")


# create an object from a class

point1 = Point()
point1.x = 10
point1.y = 20
print(point1.x + point1.y)
point1.move()
point1.draw()