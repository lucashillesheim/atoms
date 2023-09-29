"""Module with eletronic configuration's representation of a element"""
import json
from src.enums.energy_level import EnergyLevel
from src.enums.orbital import Orbital

class EletronicConfiguration:
    """Eletronic configuration's representation of a element"""
    def __init__(self):
        self._configuration = {}

    def add(self, level: EnergyLevel, orbital: Orbital, electrons: int):
        """Add a orbital with electrons to a specific level"""
        if level.name not in self._configuration:
            self._configuration[level.name] = {}

        if orbital.name not in self._configuration[level.name]:
            self._configuration[level.name][orbital.name] = electrons

    def has_level_and_orbital(self, level: EnergyLevel, orbital: Orbital) -> bool:
        """Verify if configuration has level and if level has orbital"""
        return level.name in self._configuration and orbital.name in self._configuration[level.name]

    def __str__(self):
        return json.dumps(self._configuration)
