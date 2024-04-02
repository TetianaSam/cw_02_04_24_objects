class Vechicle:
    def __init__(self, name): #inicializace, kdyz vytvarite nejaky novy object, self odkazuje samo na sebe
        self.name = name

    def start(self):
        print(f"vrvrvr startuju vozidlo{self.name}")

    def turn(self):
        print(f" i'm turning{self.name}")


v1 = Vechicle("Vechicle1")   #list()
v2 = Vechicle("Vechicle2")
v3 = Vechicle("Vechicle3")

print(v1.name)
print(v2.name)
print(v3.name)
print(type(v1)) # funkce type ukaze co to je za typ dat

v2.start()
v3.turn()