from src.celestial_body import CelestialBody
from typing import Optional


class Planet(CelestialBody):
    def __init__(
        self,
        atmosphere: Optional[str] = None,
        has_rings: bool = False,
    ):
        super().__init__()
        self._atmosphere = atmosphere
        self._has_rings = has_rings

    @property
    def atmosphere(self) -> Optional[str]:
        return self._atmosphere

    @atmosphere.setter
    def atmosphere(self, value: Optional[str]):
        self._atmosphere = value

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
        return f"Поверхность планеты {self.name} изучена"