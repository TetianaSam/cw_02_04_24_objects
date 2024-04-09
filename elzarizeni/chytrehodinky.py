from elektricke import ElektrickeZarizeni
from waterproof import Waterproof

class ChytreHodinky(ElektrickeZarizeni,Waterproof):
    def __init__(self,name):
        self.name = name
