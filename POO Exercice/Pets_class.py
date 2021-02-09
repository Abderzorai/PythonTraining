# Parent class
class Dog:
    # Class attribute
    species = 'mammal'

    # Initializer / Instance attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # instance method
    def description(self):
        return "{} is {} years old".format(self.name, self.age)

    # instance method
    def speak(self, sound):
        return "{} says {}".format(self.name, sound)


# Child class (inherits from Dog class)
class RussellTerrier(Dog):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)


# Child class (inherits from Dog class)
class Bulldog(Dog):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)


class Pets(Dog):
    objects_create = 0

    def __init__(self, name, age):
        Dog.__init__(self, name, age)
        Pets.objects_create = Pets.objects_create + 1


tom = Pets('Tom', 6)
Fletcher = Pets('Fletcher', 7)
Larry = Pets('Larry', 9)

print("I have {} dogs".format(Pets.objects_create))
print("{} is {}.".format(tom.name, tom.age))
print("{} is {}.".format(Fletcher.name, Fletcher.age))
print("{} is {}.".format(Larry.name, Larry.age))
print("And they're all {}s, of course.".format(Pets.species))