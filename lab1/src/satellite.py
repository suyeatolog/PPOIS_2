from src.celestial_body import CelestialBody
from src.validators.satellite_validator import SatelliteValidator


class Satellite(CelestialBody):
    def __init__(
        self,
        orbited_planet: str = "Земля",
        orbital_period: float = 27.3,
        distance_from_planet: float = 384400.0,
    ):
        super().__init__()
        SatelliteValidator.validate_orbited_planet(orbited_planet)
        SatelliteValidator.validate_orbital_period(orbital_period)
        SatelliteValidator.validate_distance(distance_from_planet)

        self._orbited_planet = orbited_planet
        self._orbital_period = orbital_period
        self._distance_from_planet = distance_from_planet

    @property
    def orbited_planet(self) -> str:
        return self._orbited_planet

    @orbited_planet.setter
    def orbited_planet(self, value: str):
        SatelliteValidator.validate_orbited_planet(value)
        self._orbited_planet = value

    @property
    def orbital_period(self) -> float:
        return self._orbital_period

    @orbital_period.setter
    def orbital_period(self, value: float):
        SatelliteValidator.validate_orbital_period(value)
        self._orbital_period = value

    @property
    def distance_from_planet(self) -> float:
        return self._distance_from_planet

    @distance_from_planet.setter
    def distance_from_planet(self, value: float):
        SatelliteValidator.validate_distance(value)
        self._distance_from_planet = value

    def move(self, dt: float):
        vx: float = 0.05
        x, y, z = self.position
        self.position = (x + vx * dt, y, z)

    def get_info(self) -> str:
        base_info = super().get_info()
        return f"{base_info}, планета={self.orbited_planet}, период={self.orbital_period} дней, расстояние={self.distance_from_planet} км"