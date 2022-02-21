from pprint import pprint



class Creature:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def breath(self):
        return 'breath'

    def move(self):
        return 'move'

    def eat(self):
        return 'eat'


class Human(Creature):

    def think(self):
        return "think"


class Animal(Creature):

    def hunt(self):
        return "dangerous animal is hunting"


class Cat(Animal):

    def hide_into_the_box(self):
        return "I am cat, give me box. I wanna hide"


human_2 = Human('Alex', 23)
print(human_2.age)
print(human_2.breath())
print(human_2.think())

print()

animal = Animal('Wolf', 5)
print(animal.age)
print(animal.name)
print(animal.hunt())

print()

cat_1 = Cat('Murka', 3)
print(cat_1.move())
print(cat_1.hunt())
print(cat_1.hide_into_the_box())




