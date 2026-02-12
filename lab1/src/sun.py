from src.celestial_body import CelestialBody
from src.validators.sun_validator import SunValidator


class Sun(CelestialBody):
    def __init__(
        self,
        temperature: float = 5778.0,
        luminosity: float = 3.828e26,
    ):
        super().__init__()
        SunValidator.validate_temperature(temperature)
        SunValidator.validate_luminosity(luminosity)

        self._temperature = temperature
        self._luminosity = luminosity

    @property
    def temperature(self) -> float:
        return self._temperature

    @temperature.setter
    def temperature(self, value: float):
        SunValidator.validate_temperature(value)
        self._temperature = value

    @property
    def luminosity(self) -> float:
        return self._luminosity

    @luminosity.setter
    def luminosity(self, value: float):
        SunValidator.validate_luminosity(value)
        self._luminosity = value

    def move(self, dt: float):
        pass

    def get_info(self) -> str:
        base_info = super().get_info()
        return f"{base_info}, температура={self.temperature}, светимость={self.luminosity:.2e}"