#Task1implement class Human/ Class fields should store the following: full name, date of birth, contact number, city,
# country, home adress. implement class methods for data input and output,
# provide access to individual fields through class methods

class Human:
    def __init__(self, name, contact, city=None):
        self.__name = name
        self.contact = contact
        self.city = city

    def get_name(self):
        return self.__name

    def set_name(self, new_name):
        if len(new_name)<3:
            return False
        self.__name = new_name
        return True



h1 = Human("Human 1", "contact")
h2 = Human("Human 2", "contact2", "city")


print(h1.get_name())

#h1.__name == "Nove jmeno"
h1.set_name("Nove jmeno")
print(h1.get_name())
