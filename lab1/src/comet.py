from src.celestial_body import CelestialBody
from src.validators.comet_validator import CometValidator


class Comet(CelestialBody):
    def __init__(
        self,
        core_diameter: float = 5.0,
        period: float = 1.0,
        eccentricity: float = 0.1,
        tail_length: float = 0.0,
    ):
        super().__init__()
        CometValidator.validate_core_diameter(core_diameter)
        CometValidator.validate_period(period)
        CometValidator.validate_eccentricity(eccentricity)

        self._core_diameter = core_diameter
        self._period = period
        self._eccentricity = eccentricity
        self._tail_length = tail_length

    @property
    def core_diameter(self) -> float:
        return self._core_diameter

    @core_diameter.setter
    def core_diameter(self, value: float):
        CometValidator.validate_core_diameter(value)
        self._core_diameter = value

    @property
    def period(self) -> float:
        return self._period

    @period.setter
    def period(self, value: float):
        CometValidator.validate_period(value)
        self._period = value

    @property
    def eccentricity(self) -> float:
        return self._eccentricity

    @eccentricity.setter
    def eccentricity(self, value: float):
        CometValidator.validate_eccentricity(value)
        self._eccentricity = value

    @property
    def tail_length(self) -> float:
        return self._tail_length

    @tail_length.setter
    def tail_length(self, value: float):
        self._tail_length = value

    def move(self, dt: float):
        vx: float = 0.1
        x, y, z = self.position
        self.position = (x + vx * dt, y, z)

    def approach_sun(self):
        self.tail_length += 100

    def is_active(self) -> bool:
        return self.tail_length > 0

    def get_tail_status(self) -> str:
        if self.tail_length > 0:
            return f"Хвост кометы {self.name} длиной {self.tail_length} км"
        return f"У кометы {self.name} пока нет хвоста"

    def get_info(self) -> str:
        base_info = super().get_info()
        return f"{base_info}, диаметр ядра={self.core_diameter}, период={self.period}, эксцентриситет={self.eccentricity}, длина хвоста={self.tail_length}"
