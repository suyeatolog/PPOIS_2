from typing import List, Optional
from src.celestial_body import CelestialBody
from src.planet import Planet
from src.comet import Comet
from src.asteroid import Asteroid
from src.satellite import Satellite
from src.sun import Sun
from src.spacecraft import Spacecraft

class SolarSystem():
    def __init__(self):
        self.bodies: List[CelestialBody] = []
        self.planets: List[Planet] = []
        self.comets: List[Comet] = []
        self.asteroids: List[Asteroid] = []
        self.satellites: List[Satellite] = []
        self.spacecraft: Spacecraft = None
        self.sun: Sun = None

    def add_body(self, body: CelestialBody):
        self.bodies.append(body)
        if isinstance(body, Planet):
            self.planets.append(body)
        elif isinstance(body, Comet):
            self.comets.append(body)
        elif isinstance(body, Asteroid):
            self.asteroids.append(body)
        elif isinstance(body, Satellite):
            self.satellites.append(body)
        elif isinstance(body, Spacecraft):
            if self.spacecraft is not None:
                raise ValueError("Spaceship already exists")
            else:
                self.spacecraft = body
        elif isinstance(body, Sun):
            if self.sun is not None:
                raise ValueError("Sun already exists")
            else:
                self.sun = body

    def remove_body(self, body: CelestialBody):
        if body in self.bodies:
            self.bodies.remove(body)
        if isinstance(body, Planet) and body in self.planets:
            self.planets.remove(body)
        elif isinstance(body, Satellite) and body in self.satellites:
            self.satellites.remove(body)
        elif isinstance(body, Asteroid) and body in self.asteroids:
            self.asteroids.remove(body)
        elif isinstance(body, Comet) and body in self.comets:
            self.comets.remove(body)
        elif isinstance(body, Spacecraft):
            if self.spacecraft == body:
                self.spacecraft = None
        elif isinstance(body, Sun):
            if self.sun == body:
                self.sun = None

    def get_all_bodies(self) -> List[CelestialBody]:
        return self.bodies

    def get_planets(self) -> List[Planet]:
        return self.planets

    def get_satellites(self) -> List[Satellite]:
        return self.satellites

    def get_asteroids(self) -> List[Asteroid]:
        return self.asteroids
    
    def get_comets(self) -> List[Comet]:
        return self.comets

    def get_spacecraft(self) -> Optional[Spacecraft]:
        return self.spacecraft

    def get_sun(self) -> Optional[Sun]:
        return self.sun