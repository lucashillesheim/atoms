"""THe hydrogen class"""
from src.classes.atom import Atom

class Hydrogen(Atom):
    """A hydrogen represantation"""
    def __init__(self):
        super().__init__(1)
        