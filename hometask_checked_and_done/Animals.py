from abc import ABC, abstractmethod
import random


class Animal(ABC):
    @abstractmethod
    def __init__(self):
        pass

    def eat(self):
        pass

    def make_sound(self):
        pass


class Mammal(Animal):
    def __init__(self, *, age: int, name: str):
        self.age = age
        self.satiety = 3
        self.name = name

    def eat(self):
        self.satiety += 1
        print(f'{self.name} has been fed and has {self.satiety} satiety')
        return self.satiety

    def make_sound(self):
        self.satiety -= 1
        print(f'{self.name} made a sound.....and has {self.satiety} satiety')
        return self.satiety
    # def feeding(self):
    #     self.satiety -= 2


class Bird(Animal):
    def __init__(self, *, age: int, name: str):
        self.age = age
        self.satiety = 3
        self.name = name

    def eat(self):
        self.satiety += 1
        print(f'{self.name} has been fed and has {self.satiety}')
        return self.satiety

    def make_sound(self):
        self.satiety -= 1
        print(f'{self.name} made a sound..... and has {self.satiety} satiety')
        return self.satiety
    # def flying(self):
    #     self.satiety -= 2


class Storage:
    def __init__(self):
        self.food_stock = 1000

    def __sub__(self, other=2):
        self.food_stock -= other

    def replenishment(self):
        self.food_stock += 500
        return self.food_stock


A = Storage()
B = Mammal(age=5, name='charlie')
C = Bird(age=3, name='jack')
Zoo = [B, C]


def living(creature):
    random_number = random.randint(1, 2)
    if random_number == 1:
        creature.eat()
        A.__sub__()
    else:
        creature.make_sound()


for animal in Zoo:
    while animal.satiety > 0 and A.food_stock > 6:
        living(animal)
    else:
        print(f'{animal.name} died because of famine')
