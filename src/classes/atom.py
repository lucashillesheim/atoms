"""Creates a represenation of an Atom"""
from src.enums.energy_level import EnergyLevel
from src.classes.eletronic_configuration import EletronicConfiguration
from src.enums.orbital import Orbital

class Atom:
    """Creates a represenation of an Atom"""
    def __init__(self, particles: int, electronegativity: float, neutrons: int = 0):
        self._protons = particles
        self._electrons = particles
        self._neutrons = neutrons
        self._atomic_number = self._protons
        self._atomic_mass = self._protons + self._neutrons
        self._electronegativity = electronegativity

    def get_eletronic_configuration(self) -> EletronicConfiguration:
        """Returns the eletronic configuration based on the atomic mass"""
        eletronic_configuration = EletronicConfiguration()
        remain_electrons = [self._atomic_mass]
        levels = list(EnergyLevel)

        level: EnergyLevel
        for level in levels:
            orbitals = level.types_orbital
            for orbital in orbitals:
                if not eletronic_configuration.has_level_and_orbital(level, orbital):
                    self._add_electron(level, orbital, remain_electrons, eletronic_configuration)

                    index_next_level = levels.index(level) + 1
                    index_next_level_s = 0
                    index_next_level_p = 0
                    if len(levels) > index_next_level:

                        if orbital == Orbital.D:
                            index_next_level_s += 1

                        if orbital == Orbital.F:
                            index_next_level_s += 1
                            index_next_level_p += 1

                        if orbital is not Orbital.D and orbital is not Orbital.P and orbital is not Orbital.S:
                            self._add_electron(levels[index_next_level], Orbital.D, remain_electrons, eletronic_configuration)

                        if len(levels) >= index_next_level_p + 1 and orbital is not Orbital.P and orbital is not Orbital.S:
                            self._add_electron(levels[index_next_level + index_next_level_p], Orbital.P, remain_electrons, eletronic_configuration)

                        if len(levels) >= index_next_level_s + 1 and orbital is not Orbital.S:
                            self._add_electron(levels[index_next_level + index_next_level_s], Orbital.S, remain_electrons, eletronic_configuration)

            if remain_electrons[0] == 0:
                break

        return eletronic_configuration

    def _add_electron(self, level, orbital, remain_electrons, eletronic_configuration):
        """Add electrons to the specific orbital"""
        print(level.name, orbital.name, remain_electrons)
        eletrons = remain_electrons[0]
        if eletrons > 0:
            if eletrons >= orbital.value:
                eletronic_configuration.add(level, orbital, orbital.value)
                remain_electrons[0] -= orbital.value
            else:
                eletronic_configuration.add(level, orbital, eletrons)
                remain_electrons[0] = 0
