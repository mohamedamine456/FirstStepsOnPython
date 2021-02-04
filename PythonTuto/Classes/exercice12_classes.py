# define the Person Class
class Person:
    def __init__(self, name):
        self.name = name
    def talk(self):
        print(f"Hello I am {self.name}")


# create object and call talk function
person1 = Person("Mohamed Amine")
person1.talk()

# create another one
person2 = Person("Mamado Moctar")
person2.talk()