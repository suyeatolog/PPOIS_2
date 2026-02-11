from src.celestial_body import CelestialBody
from typing import Tuple
from src.validators.sun_validator import SunValidator

class Sun(CelestialBody):
    def __init__(self, name: str, mass: float, position: Tuple[float, float, float], radius: float, temperature: float,
                 luminosity: float):
        super().__init__(name, mass, position, radius)
        SunValidator.validate_temperature(temperature)
        SunValidator.validate_luminosity(luminosity)

        self.temperature = temperature
        self.luminosity = luminosity

    def move(self, dt: float):
        pass

    def get_info(self) -> str:
        base_info = super().get_info()
        return f"{base_info}, температура={self.temperature}, светимость={self.luminosity:.2e}"