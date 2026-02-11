from typing import Tuple
from abc import ABC, abstractmethod
from src.validator import Validator

class CelestialBody(ABC):
    def __init__(self, name:str, mass: float, position: Tuple[float, float, float], radius:float):
        Validator.validate_mass(mass)
        Validator.validate_position(position)
        Validator.validate_radius(radius)

        self.name = name
        self.mass = mass
        self.position = position
        self.radius = radius

    @abstractmethod
    def move(self, dt: float):
        pass

    def get_info(self) -> str:
        return f"{self.name}: масса = {self.mass}, позиция = {self.position}, радиус = {self.radius}"