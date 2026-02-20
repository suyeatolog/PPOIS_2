from src.celestial_body import CelestialBody
from src.validators.spacecraft_validator import SpacecraftValidator
from exceptions.custom_exceptions import LaunchError, FullFuelError
from src.planet import Planet
from src.comet import Comet
from src.asteroid import Asteroid
from src.satellite import Satellite
class Spacecraft(CelestialBody):
    def __init__(
        self,
        fuel: float = 1000.0,
        status: str = "idle",
    ):
        super().__init__()
        SpacecraftValidator.validate_fuel(fuel)
        SpacecraftValidator.validate_status(status)

        self._fuel = fuel
        self._status = status
        self._destination = None

    @property
    def fuel(self) -> float:
        return self._fuel

    @fuel.setter
    def fuel(self, value: float):
        SpacecraftValidator.validate_fuel(value)
        self._fuel = value

    @property
    def status(self) -> str:
        return self._status

    @status.setter
    def status(self, value: str):
        SpacecraftValidator.validate_status(value)
        self._status = value

    @property
    def destination(self) -> CelestialBody:
        return self._destination

    @destination.setter
    def destination(self, value: CelestialBody):
        self._destination = value

    def launch(self):
        if self.fuel <= 0:
            raise LaunchError("Not enough fuel to launch")
        self.status = "traveling"

    def travel_to(self, target: CelestialBody):
        if self.fuel <= 0:
            raise LaunchError("Not enough fuel to travel")
        self.destination = target
        self.status = "traveling"

        self.position = target.position
        self.status = "idle"
        self.fuel -= 1000

    def fuel_up_spaceship(self):
        if self.fuel == 5000:
            raise FullFuelError("Already full. No need to fulfill")
        self.fuel = 5000

    def collect_data(self, target: CelestialBody) -> dict:

        return {
            "object_name": target.name,
            "mass": target.mass,
            "position": target.position,
            "radius": target.radius
        }

    def collect_atmosphere_and_surface_data(self, target: Planet) -> dict:
        return {
            "planet_name": target.name,
            "atmosphere": target.atmosphere,
            "surface": target.surface,
            "has_rings": target.has_rings
        }

    def collect_comet_data(self, target: Comet) -> dict:
        return {
            "comet_name": target.name,
            "period": target.period,
            "eccentricity": target.eccentricity,
            "tail_length": target.tail_length
        }

    def collect_asteroid_data(self, target: Asteroid) -> dict:
        return {
            "asteroid_name": target.name,
            "composition": target.composition,
            "orbit_type": target.orbit_type
        }

    def collect_satellite_data(self, target: Satellite) -> dict:
        return {
            "satellite_name": target.name,
            "orbited_planet": target.orbited_planet,
            "orbital_period": target.orbital_period,
            "distance_from_planet": target.distance_from_planet
        }

    def move(self, dt: float):
        vx: float = 0.1
        x, y, z = self.position
        self.position = (x + vx * dt, y, z)

    def get_info(self) -> str:
        base_info = super().get_info()
        return f"{base_info}, статус={self.status}, топливо={self.fuel}, цель={self.destination.name if self.destination else 'нет'}"