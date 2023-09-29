"""Energy level of an atom"""
from typing import List
from aenum import Enum, NoAlias
from src.enums.orbital import Orbital

class EnergyLevel(Enum):
    """
    Representation of the 7 energy levels
    
    :param maximum_electrons: Maximum numbers of electrons
    :type maximum_electrons: int
    :param types_orbital: Allowed types of orbitals
    :type types_orbital: Orbital
    """
    _settings_ = NoAlias

    K = 2, [Orbital.S]
    L = 8, [Orbital.S, Orbital.P]
    M = 18, [Orbital.S, Orbital.P, Orbital.D]
    N = 32, [Orbital.S, Orbital.P, Orbital.D, Orbital.F]
    O = 32, [Orbital.S, Orbital.P, Orbital.D, Orbital.F]
    P = 18, [Orbital.S, Orbital.P, Orbital.D]
    Q = 8, [Orbital.S, Orbital.P]

    def __init__(self, maximum_electrons, types_orbital):
        self.maximum_electrons: int = maximum_electrons
        self.types_orbital: List[Orbital] = types_orbital
