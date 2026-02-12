from src.celestial_body import CelestialBody
from src.validators.asteroid_validator import AsteroidValidator


class Asteroid(CelestialBody):
    def __init__(
        self,
        composition: str = "rocky",
        orbit_type: str = "main belt",
    ):
        super().__init__()
        AsteroidValidator.validate_composition(composition)
        AsteroidValidator.validate_orbit_type(orbit_type)

        self._composition = composition
        self._orbit_type = orbit_type

    @property
    def composition(self) -> str:
        return self._composition

    @composition.setter
    def composition(self, value: str):
        AsteroidValidator.validate_composition(value)
        self._composition = value

    @property
    def orbit_type(self) -> str:
        return self._orbit_type

    @orbit_type.setter
    def orbit_type(self, value: str):
        AsteroidValidator.validate_orbit_type(value)
        self._orbit_type = value

    def move(self, dt: float):
        vx: float = 0.05
        x, y, z = self.position
        self.position = (x + vx * dt, y, z)

    def get_info(self) -> str:
        base_info = super().get_info()
        return f"{base_info}, состав={self.composition}, тип орбиты={self.orbit_type}"
