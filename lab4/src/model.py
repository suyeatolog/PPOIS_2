from pathlib import Path
from solar_system_simulator import SolarSystemInitializer
from solar_system_simulator import Planet, Comet, Asteroid, Satellite, Sun

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

    def get_all_bodies(self):
        return self.solar_system.get_all_bodies()
    
    def get_celestial_bodies_only(self):
        all_bodies = self.get_all_bodies()
        return [body for body in all_bodies if body != self.spacecraft]

    def get_body_by_name(self, name: str):
        for body in self.get_all_bodies():
            if body.name == name:
                return body
        return None
    
    def travel_to(self, target_body):
        if self.spacecraft:
            self.spacecraft.travel_to(target_body)
            self.current_body = target_body

    def get_fuel_level(self):
        if self.spacecraft:
            return self.spacecraft.fuel
        return 0
    
    def fuel_up(self):
        if self.spacecraft:
            self.spacecraft.fuel_up_spaceship()

    def launch_spacecraft(self):
        if self.spacecraft:
            self.spacecraft.launch()

    def check_launch_status(self):
        if not self.spacecraft:
            return False
        return self.spacecraft.status == "traveling"
    
    def collect_data(self):
        if not self.check_launch_status():
            return "Error: Spacecraft is not launched."
        if not self.current_body:
            return "Error: No target object."

        if isinstance(self.current_body, Planet):
            return self.spacecraft.collect_atmosphere_and_surface_data(self.current_body)
        elif isinstance(self.current_body, Comet):
            return self.spacecraft.collect_comet_data(self.current_body)
        elif isinstance(self.current_body, Asteroid):
            return self.spacecraft.collect_asteroid_data(self.current_body)
        elif isinstance(self.current_body, Satellite):
            return self.spacecraft.collect_satellite_data(self.current_body)
        elif isinstance(self.current_body, Sun):
            return "Too hot to collect data. It is highly recommended to leave asap."
        else:
            return "Current object doesn't support data collection."