# define Parent Class
class Mammal:
    def walk(self):
        print("Walk")


# define child inherit from ParentClass(Mammal)
class Dog(Mammal):
    def bark(self):
        print("Bark")


# another child
class Cat(Mammal):
    def voice(self):
        print("Meaao")

# create objects
dog1 = Dog()
dog1.walk()
dog1.bark()

cat1 = Cat()
cat1.walk()
cat1.voice()