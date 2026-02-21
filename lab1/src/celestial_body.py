from abc import ABC, abstractmethod
from typing import Tuple
from src.validators.validator import Validator


class CelestialBody(ABC):
    def __init__(
        self,
        name: str = "Unknown",
        mass: float = 1.0,
        position: Tuple[float, float, float] = (0.0, 0.0, 0.0),
        radius: float = 1.0,
    ):
        Validator.validate_mass(mass)
        Validator.validate_position(position)
        Validator.validate_radius(radius)

        self._name = name
        self._mass = mass
        self._position = position
        self._radius = radius

    @property
    def name(self) -> str:
        return self._name
    
    @name.setter
    def name(self, new_name: str):
        self._name = new_name

    @property
    def mass(self) -> float:
        return self._mass

    @mass.setter
    def mass(self, value: float):
        Validator.validate_mass(value)
        self._mass = value

    @property
    def position(self) -> Tuple[float, float, float]:
        return self._position

    @position.setter
    def position(self, value: Tuple[float, float, float]):
        Validator.validate_position(value)
        self._position = value

    @property
    def radius(self) -> float:
        return self._radius

    @radius.setter
    def radius(self, value: float):
        Validator.validate_radius(value)
        self._radius = value

    @abstractmethod
    def move(self, dt: float):
        pass

    def get_info(self) -> str:
        return f"{self.name}: mass = {self.mass}, position = {self.position}, radius = {self.radius}"
