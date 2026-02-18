from src.celestial_body import CelestialBody
from typing import Optional, List
from src.validators.planet_validator import PlanetValidator
from src.satellite import Satellite

class Planet(CelestialBody):
    def __init__(
        self,
        atmosphere: Optional[str] = None,
        surface: str = "Rocky",
        has_rings: bool = False,
        satellites: List[Satellite] = None
    ):
        super().__init__()
        PlanetValidator.validate_surface(surface)

        self._surface = surface
        self._atmosphere = atmosphere
        self._has_rings = has_rings
        self._satellites = satellites if satellites is not None else []

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

    @property
    def satellites(self) -> List[Satellite]:
        return self._satellites

    @satellites.setter
    def satellites(self, value: List[Satellite]):
        if not isinstance(value, list):
            raise TypeError("Спутники должны быть представлены в виде списка")
        for sat in value:
            if not isinstance(sat, Satellite):
                raise TypeError("Все элементы списка спутников должны быть объектами класса Satellite")
        self._satellites = value

    def add_satellite(self, satellite: Satellite):
        if not isinstance(satellite, Satellite):
            raise TypeError("Можно добавить только объект класса Satellite")
        self._satellites.append(satellite)

    def remove_satellite(self, satellite: Satellite):
        if satellite in self._satellites:
            self._satellites.remove(satellite)

    def move(self, dt: float):
        vx: float = 0.1
        x, y, z = self.position
        self.position = (x + vx * dt, y, z)

    def get_surface_info(self) -> str:
        return f"Поверхность планеты {self.name}={self.surface}, атмосфера={self.atmosphere}"