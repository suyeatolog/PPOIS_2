from src.celestial_body import CelestialBody
from typing import Optional
from src.validators.planet_validator import PlanetValidator

class Planet(CelestialBody):
    def __init__(
        self,
        atmosphere: Optional[str] = None,
        surface: str = "Rocky",
        has_rings: bool = False,
    ):
        super().__init__()
        PlanetValidator.validate_surface(surface)

        self._surface = surface
        self._atmosphere = atmosphere
        self._has_rings = has_rings

    @property
    def atmosphere(self) -> Optional[str]:
        return self._atmosphere

    @atmosphere.setter
    def atmosphere(self, value: Optional[str]):
        self._atmosphere = value

    @property
    def surface(self) -> str:
        return self._surface
    
    @surface.setter
    def surface(self, value: str):
        PlanetValidator.validate_surface(value)
        self._surface = value

    @property
    def has_rings(self) -> bool:
        return self._has_rings

    @has_rings.setter
    def has_rings(self, value: bool):
        self._has_rings = value

    def move(self, dt: float):
        vx: float = 0.1
        x, y, z = self.position
        self.position = (x + vx * dt, y, z)

    def get_surface_info(self) -> str:
        return f"Поверхность планеты {self.name}={self.surface}, атмосфера={self.atmosphere}"