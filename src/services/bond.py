"""Module to bond atoms"""
from typing import List
from src.classes.atom import Atom

class Bond:
    """Static class to create the bond between atoms"""

    def __new__(cls):
        raise TypeError("This is a static class and cannot be instantiated.")

    @staticmethod
    def covalent(atoms: List[Atom]):
        """Return de bond between two atoms"""
        for atom in atoms:
            first_config = atom.get_eletronic_configuration()
    