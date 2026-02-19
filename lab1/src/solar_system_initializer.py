from src.solar_system import SolarSystem
from src.sun import Sun
from src.spacecraft import Spacecraft
from src.planet import Planet
from src.comet import Comet
from src.asteroid import Asteroid
from src.satellite import Satellite


class SolarSystemInitializer:
    def __init__(self):
        self.solar_system = SolarSystem()
        self._create_sun()
        self._create_planets()
        self._create_comets()
        self._create_asteroids()
        self._create_satellites()
        self._create_spacecraft()

    def _create_sun(self):
        sun = Sun(temperature=5778, luminosity=3.828e26)
        sun.name = "Sun"
        sun.mass = 1.989e30
        sun.position = (0.0, 0.0, 0.0)
        sun.radius = 696340.0
        self.solar_system.add_body(sun)

    def _create_planets(self):
        mercury = Planet(atmosphere=None, has_rings=False, surface="Rocky")
        mercury.name = "Mercury"
        mercury.mass = 3.3e23
        mercury.position = (5.79e10, 0.0, 0.0)
        mercury.radius = 2439.7
        self.solar_system.add_body(mercury)

        venus = Planet(atmosphere="Carbon Dioxide", has_rings=False, surface="Rocky")
        venus.name = "Venus"
        venus.mass = 4.86e24
        venus.position = (1.08e11, 0.0, 0.0)
        venus.radius = 6051.8
        self.solar_system.add_body(venus)

        earth = Planet(atmosphere="Nitrogen, Oxygen", has_rings=False, surface="Rocky")
        earth.name = "Earth"
        earth.mass = 5.97e24
        earth.position = (1.5e11, 0.0, 0.0)
        earth.radius = 6371.0
        self.solar_system.add_body(earth)

        mars = Planet(atmosphere="Carbon Dioxide", has_rings=False, surface="Rocky")
        mars.name = "Mars"
        mars.mass = 6.39e23
        mars.position = (2.28e11, 0.0, 0.0)
        mars.radius = 3389.5
        self.solar_system.add_body(mars)

        jupiter = Planet(atmosphere="Hydrogen, Helium", has_rings=True, surface="Gas")
        jupiter.name = "Jupiter"
        jupiter.mass = 1.898e27
        jupiter.position = (7.78e11, 0.0, 0.0)
        jupiter.radius = 69911.0
        self.solar_system.add_body(jupiter)

        saturn = Planet(atmosphere="Hydrogen, Helium", has_rings=True, surface="Gas")
        saturn.name = "Saturn"
        saturn.mass = 5.68e26
        saturn.position = (1.43e12, 0.0, 0.0)
        saturn.radius = 58232.0
        self.solar_system.add_body(saturn)

        uranus = Planet(atmosphere="Hydrogen, Helium, Methane", has_rings=True, surface="Icy")
        uranus.name = "Uranus"
        uranus.mass = 8.68e25
        uranus.position = (2.87e12, 0.0, 0.0)
        uranus.radius = 25362.0
        self.solar_system.add_body(uranus)

        neptune = Planet(atmosphere="Hydrogen, Helium, Methane", has_rings=False, surface="Icy")
        neptune.name = "Neptune"
        neptune.mass = 1.02e26
        neptune.position = (4.5e12, 0.0, 0.0)
        neptune.radius = 24622.0
        self.solar_system.add_body(neptune)

    def _create_comets(self):
        halley = Comet(core_diameter=10.0, period=75.3, eccentricity=0.967)
        halley.name = "Halley's Comet"
        halley.mass = 2.2e14
        halley.position = (5e12, 0.0, 0.0)
        halley.radius = 5.0
        self.solar_system.add_body(halley)

    def _create_asteroids(self):
        ceres = Asteroid(composition="rocky", orbit_type="main belt")
        ceres.name = "Ceres"
        ceres.mass = 9.39e20
        ceres.position = (4.14e11, 0.0, 0.0)
        ceres.radius = 473.0
        self.solar_system.add_body(ceres)

    def _create_satellites(self):
        moon = Satellite(orbited_planet="Earth", orbital_period=27.3, distance_from_planet=384400.0)
        moon.name = "Moon"
        moon.mass = 7.34e22
        moon.position = (1.5e11, 384400.0, 0.0)
        moon.radius = 1737.4
        self.solar_system.add_body(moon)

    def _create_spacecraft(self):
        spacecraft = Spacecraft(fuel=5000.0, status="idle")
        spacecraft.name = "Mars Explorer"
        spacecraft.mass = 1000.0
        spacecraft.position = (0.0, 0.0, 0.0)
        spacecraft.radius = 2.0
        self.solar_system.add_body(spacecraft)

    def get_solar_system(self):
        return self.solar_system