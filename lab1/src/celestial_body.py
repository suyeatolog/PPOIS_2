from typing import Tuple
from abc import ABC, abstractmethod
from exceptions.custom_exceptions import InvalidMassError

class CelestialBody(ABC):
    def __init__(self, name:str, mass: float, position: Tuple[float, float, float], radius:float):
        if mass <= 0:
            raise InvalidMassError("Масса должна быть положительной!")
        self.name = name
        self.mass = mass
        self.position = position
        self.radius = radius

    @abstractmethod
    def move(self, dt: float):
        pass

    def get_info(self) -> str:
        return f"{self.name}: масса = {self.mass}, позиция = {self.position}, радиус = {self.radius}"