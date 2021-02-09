class Pets:

    dogs = []

    def __init__(self, dogs):
        self.dogs = dogs

# Parent class
class Dog:
    # Class attribute
    species = 'mammal'

    # Initializer / Instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.is_hungry = True

    # instance method
    def description(self):
        return "{} is {} years old".format(self.name, self.age)

    # instance method
    def speak(self, sound):
        return "{} says {}".format(self.name, sound)

    def eat(self):
        self.is_hungry = False


# Child class (inherits from Dog class)
class RussellTerrier(Dog):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)


# Child class (inherits from Dog class)
class Bulldog(Dog):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)


my_dogs = [
    Bulldog("Tom", 6),
    RussellTerrier("Fletcher", 7),
    Dog("Larry", 9)
]

my_pets = Pets(my_dogs)

for dog in my_pets.dogs:
    if dog.is_hungry == True:
         print("All the dogs are very hungry")
    else:
         print("They are not hungry")

for dog in my_pets.dogs:
    dog.eat()
    if dog.is_hungry == True:
         print("All the dogs are very hungry")
    else:
         print("They are not hungry")
