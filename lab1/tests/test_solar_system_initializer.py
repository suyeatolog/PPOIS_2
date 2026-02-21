from src.solar_system_initializer import SolarSystemInitializer


def test_solar_system_initializer_creation():
    initializer = SolarSystemInitializer()
    solar_system = initializer.get_solar_system()

    assert solar_system is not None
    assert solar_system.sun is not None
    assert solar_system.spacecraft is not None


def test_solar_system_initializer_sun():
    initializer = SolarSystemInitializer()
    solar_system = initializer.get_solar_system()
    
    sun = solar_system.sun
    assert sun.name == "Sun"
    assert sun.mass == 1.989e30
    assert sun.position == (0.0, 0.0, 0.0)
    assert sun.radius == 696340.0
    assert sun.temperature == 5778
    assert sun.luminosity == 3.828e26


def test_solar_system_initializer_planets():
    initializer = SolarSystemInitializer()
    solar_system = initializer.get_solar_system()

    planets = solar_system.get_planets()
    assert len(planets) == 8

    names = {planet.name for planet in planets}
    expected_names = {"Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"}
    assert names == expected_names

    earth = next(p for p in planets if p.name == "Earth")
    assert earth.atmosphere == "Nitrogen, Oxygen"
    assert earth.has_rings is False
    assert earth.surface == "Rocky"
    assert earth.mass == 5.97e24
    assert earth.position == (1.5e11, 0.0, 0.0)
    assert earth.radius == 6371.0


def test_solar_system_initializer_comets():
    initializer = SolarSystemInitializer()
    solar_system = initializer.get_solar_system()

    comets = solar_system.get_comets()
    assert len(comets) == 1

    comet = comets[0]
    assert comet.name == "Halley's Comet"
    assert comet.core_diameter == 10.0
    assert comet.period == 75.3
    assert comet.eccentricity == 0.967
    assert comet.mass == 2.2e14
    assert comet.position == (5e12, 0.0, 0.0)
    assert comet.radius == 5.0


def test_solar_system_initializer_asteroids():
    initializer = SolarSystemInitializer()
    solar_system = initializer.get_solar_system()

    asteroids = solar_system.get_asteroids()
    assert len(asteroids) == 1

    asteroid = asteroids[0]
    assert asteroid.name == "Ceres"
    assert asteroid.composition == "rocky"
    assert asteroid.orbit_type == "main belt"
    assert asteroid.mass == 9.39e20
    assert asteroid.position == (4.14e11, 0.0, 0.0)
    assert asteroid.radius == 473.0


def test_solar_system_initializer_satellites():
    initializer = SolarSystemInitializer()
    solar_system = initializer.get_solar_system()

    satellites = solar_system.get_satellites()
    assert len(satellites) == 1

    satellite = satellites[0]
    assert satellite.name == "Moon"
    assert satellite.orbited_planet == "Earth"
    assert satellite.orbital_period == 27.3
    assert satellite.distance_from_planet == 384400.0
    assert satellite.mass == 7.34e22
    assert satellite.position == (1.5e11, 384400.0, 0.0)
    assert satellite.radius == 1737.4


def test_solar_system_initializer_spacecraft():
    initializer = SolarSystemInitializer()
    solar_system = initializer.get_solar_system()

    spacecraft = solar_system.get_spacecraft()
    assert spacecraft is not None
    assert spacecraft.name == "Mars Explorer"
    assert spacecraft.fuel == 5000.0
    assert spacecraft.status == "idle"
    assert spacecraft.mass == 1000.0
    assert spacecraft.position == (0.0, 0.0, 0.0)
    assert spacecraft.radius == 2.0


def test_solar_system_initializer_total_bodies():
    initializer = SolarSystemInitializer()
    solar_system = initializer.get_solar_system()

    all_bodies = solar_system.get_all_bodies()
    assert len(all_bodies) == 13

    body_names = {body.name for body in all_bodies}
    expected_names = {
        "Sun", "Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune",
        "Halley's Comet", "Ceres", "Moon", "Mars Explorer"
    }
    assert body_names == expected_names