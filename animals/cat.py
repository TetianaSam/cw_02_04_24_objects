from animal import Animal
from dog import Dog

class Cat(Animal,Dog):
    def make_sound(self):
        print("mau mau")