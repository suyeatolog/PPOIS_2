from pathlib import Path
from solar_system_simulator import SolarSystemInitializer

IMAGES_DIR = Path(__file__).parent.parent / "images"

OBJECT_TO_IMAGE = {
    "Sun": "sun.png",
    "Mercury": "mercury.png",
    "Venus": "venus.png",
    "Earth": "earth.png",
    "Mars": "mars.png",
    "Jupiter": "jupiter.png",
    "Saturn": "saturn.png",
    "Uranus": "uranus.png",
    "Neptune": "neptune.png",
    "Moon": "moon.png",
    "Halley's Comet": "comet.png",
    "Ceres": "ceres.png",
}

class SolarSystemModel:
    def __init__(self):
        initializer = SolarSystemInitializer()
        self.solar_system = initializer.get_solar_system()
        self.current_body = self.solar_system.sun
        self.spacecraft = self.solar_system.get_spacecraft()