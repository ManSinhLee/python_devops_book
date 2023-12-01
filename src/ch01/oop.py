class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} says Woof!")

    def celebrate_birthday(self):
        self.age += 1
        print(f"{self.name} is now {self.age} years old!")

# Creating instances of the Dog class
dog1 = Dog(name="Buddy", age=3)
dog2 = Dog(name="Max", age=5)

# Accessing attributes and calling methods
print(f"{dog1.name} is {dog1.age} years old.")
dog1.bark()
dog1.celebrate_birthday()

print(f"{dog2.name} is {dog2.age} years old.")
dog2.bark()
dog2.celebrate_birthday()
