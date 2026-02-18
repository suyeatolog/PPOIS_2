from src.celestial_body import CelestialBody
from src.validators.spacecraft_validator import SpacecraftValidator
from exceptions.custom_exceptions import LaunchError
from src.planet import Planet

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
            raise LaunchError("Недостаточно топлива для запуска")
        self.status = "traveling"

    def travel_to(self, target: CelestialBody):
        if self.fuel <= 0:
            raise LaunchError("Недостаточно топлива для путешествия")
        self.destination = target
        self.status = "traveling"

        self.position = target.position
        self.status = "idle"

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
            "surface": target.surface
        }

    def move(self, dt: float):
        vx: float = 0.1
        x, y, z = self.position
        self.position = (x + vx * dt, y, z)

    def get_info(self) -> str:
        base_info = super().get_info()
        return f"{base_info}, статус={self.status}, топливо={self.fuel}, цель={self.destination.name if self.destination else 'нет'}"