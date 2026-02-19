import pytest
from src.solar_system import SolarSystem
from src.planet import Planet
from src.satellite import Satellite
from src.asteroid import Asteroid
from src.comet import Comet
from src.spacecraft import Spacecraft
from src.sun import Sun


def test_solar_system_creation():
    ss = SolarSystem()
    assert ss.bodies == []
    assert ss.planets == []
    assert ss.comets == []
    assert ss.asteroids == []
    assert ss.satellites == []
    assert ss.spacecraft is None
    assert ss.sun is None


def test_add_planet():
    ss = SolarSystem()
    planet = Planet()
    planet.name = "Earth"
    ss.add_body(planet)
    assert len(ss.planets) == 1
    assert ss.planets[0].name == "Earth"
    assert len(ss.bodies) == 1


def test_add_comet():
    ss = SolarSystem()
    comet = Comet()
    comet.name = "Halley"
    ss.add_body(comet)
    assert len(ss.comets) == 1
    assert ss.comets[0].name == "Halley"
    assert len(ss.bodies) == 1


def test_add_asteroid():
    ss = SolarSystem()
    asteroid = Asteroid()
    asteroid.name = "Ceres"
    ss.add_body(asteroid)
    assert len(ss.asteroids) == 1
    assert ss.asteroids[0].name == "Ceres"
    assert len(ss.bodies) == 1


def test_add_satellite():
    ss = SolarSystem()
    satellite = Satellite()
    satellite.name = "Moon"
    ss.add_body(satellite)
    assert len(ss.satellites) == 1
    assert ss.satellites[0].name == "Moon"
    assert len(ss.bodies) == 1


def test_add_spacecraft():
    ss = SolarSystem()
    spacecraft = Spacecraft()
    spacecraft.name = "Mars Rover"
    ss.add_body(spacecraft)
    assert ss.spacecraft is not None
    assert ss.spacecraft.name == "Mars Rover"
    assert len(ss.bodies) == 1


def test_add_second_spacecraft_raises_error():
    ss = SolarSystem()
    sc1 = Spacecraft()
    ss.add_body(sc1)
    sc2 = Spacecraft()
    with pytest.raises(ValueError, match="Spaceship already exists"):
        ss.add_body(sc2)


def test_add_sun():
    ss = SolarSystem()
    sun = Sun()
    sun.name = "Sun"
    ss.add_body(sun)
    assert ss.sun is not None
    assert ss.sun.name == "Sun"
    assert len(ss.bodies) == 1


def test_add_second_sun_raises_error():
    ss = SolarSystem()
    sun1 = Sun()
    ss.add_body(sun1)
    sun2 = Sun()
    with pytest.raises(ValueError, match="Sun already exists"):
        ss.add_body(sun2)


def test_remove_body_planet():
    ss = SolarSystem()
    planet = Planet()
    planet.name = "Mars"
    ss.add_body(planet)
    assert len(ss.planets) == 1
    assert len(ss.bodies) == 1
    ss.remove_body(planet)
    assert len(ss.planets) == 0
    assert len(ss.bodies) == 0


def test_remove_body_spacecraft():
    ss = SolarSystem()
    spacecraft = Spacecraft()
    spacecraft.name = "Mars Rover"
    ss.add_body(spacecraft)
    assert ss.spacecraft is not None
    ss.remove_body(spacecraft)
    assert ss.spacecraft is None
    assert len(ss.bodies) == 0


def test_remove_body_sun():
    ss = SolarSystem()
    sun = Sun()
    ss.add_body(sun)
    assert ss.sun is not None
    ss.remove_body(sun)
    assert ss.sun is None
    assert len(ss.bodies) == 0


def test_get_all_bodies():
    ss = SolarSystem()
    planet = Planet()
    planet.name = "Earth"
    ss.add_body(planet)
    comet = Comet()
    comet.name = "Halley"
    ss.add_body(comet)
    bodies = ss.get_all_bodies()
    assert len(bodies) == 2
    assert bodies[0].name == "Earth"
    assert bodies[1].name == "Halley"


def test_get_planets():
    ss = SolarSystem()
    planet1 = Planet()
    planet1.name = "Earth"
    planet2 = Planet()
    planet2.name = "Mars"
    ss.add_body(planet1)
    ss.add_body(planet2)
    planets = ss.get_planets()
    assert len(planets) == 2
    assert planets[0].name == "Earth"
    assert planets[1].name == "Mars"


def test_get_comets():
    ss = SolarSystem()
    comet1 = Comet()
    comet1.name = "Halley"
    comet2 = Comet()
    comet2.name = "Encke"
    ss.add_body(comet1)
    ss.add_body(comet2)
    comets = ss.get_comets()
    assert len(comets) == 2
    assert comets[0].name == "Halley"
    assert comets[1].name == "Encke"


def test_get_asteroids():
    ss = SolarSystem()
    asteroid1 = Asteroid()
    asteroid1.name = "Ceres"
    asteroid2 = Asteroid()
    asteroid2.name = "Pallas"
    ss.add_body(asteroid1)
    ss.add_body(asteroid2)
    asteroids = ss.get_asteroids()
    assert len(asteroids) == 2
    assert asteroids[0].name == "Ceres"
    assert asteroids[1].name == "Pallas"


def test_get_satellites():
    ss = SolarSystem()
    satellite1 = Satellite()
    satellite1.name = "Moon"
    satellite2 = Satellite()
    satellite2.name = "Phobos"
    ss.add_body(satellite1)
    ss.add_body(satellite2)
    satellites = ss.get_satellites()
    assert len(satellites) == 2
    assert satellites[0].name == "Moon"
    assert satellites[1].name == "Phobos"