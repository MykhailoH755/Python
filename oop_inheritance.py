class Animal:
    def sound(self):
        pass  

class Cat(Animal):
    def sound(self):
        return "Мяу!"

class Dog(Animal):
    def sound(self):
        return "Гав!"

class Parrot(Animal):
    def sound(self):
        return "Крр!"


animals = [Cat(), Dog(), Parrot()]

for animal in animals:
    print(animal.sound())  
