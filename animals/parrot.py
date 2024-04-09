from animal import Animal
from walkable import Walkable
from flyable import Flyable

class Parrot (Animal,Walkable,Flyable):
    def walk(self):
        print("Parrot walking")
    def fly(self):
        print("Parrot flying")
