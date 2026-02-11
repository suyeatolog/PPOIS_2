from src.celestial_body import CelestialBody
from typing import Optional, Tuple

class Planet(CelestialBody):
    def __init__(self, name: str, mass: float, position: Tuple[float, float, float], radius: float,
                 atmosphere: Optional[str] = None, has_rings: bool = False):
        super().__init__(name, mass, position, radius)
        self.atmosphere = atmosphere
        self.has_rings = has_rings

    def move(self, dt: float):
        vx:float = 0.1
        x, y, z = self.position
        self.position = (x + vx * dt, y, z)

    def get_surface_info(self) -> str:
        return f"Поверхность планеты {self.name} изучена"
