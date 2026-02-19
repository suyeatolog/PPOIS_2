import pytest
from src.planet import Planet
from src.satellite import Satellite
from exceptions.custom_exceptions import (
    InvalidMassError,
    InvalidPositionError,
    InvalidRadiusError,
    InvalidSurfaceError,
)


def test_planet_creation():
    planet = Planet(
        atmosphere="Nitrogen, Oxygen",
        has_rings=False,
        surface="Rocky"
    )
    planet.name = "Earth"
    planet.mass = 5.97e24
    planet.position = (0.0, 0.0, 0.0)
    planet.radius = 6371.0
    assert planet.name == "Earth"
    assert planet.mass == 5.97e24
    assert planet.position == (0.0, 0.0, 0.0)
    assert planet.radius == 6371.0
    assert planet.atmosphere == "Nitrogen, Oxygen"
    assert planet.surface == "Rocky"
    assert planet.has_rings is False
    assert planet.satellites == []


def test_planet_move():
    planet = Planet()
    planet.name = "Mars"
    planet.mass = 6.39e23
    planet.position = (0.0, 0.0, 0.0)
    planet.radius = 3389.5
    planet.move(dt=10)
    assert planet.position[0] == 1.0


def test_planet_get_surface_info():
    planet = Planet()
    planet.name = "Venus"
    planet.mass = 4.86e24
    planet.position = (0.0, 0.0, 0.0)
    planet.radius = 6052.0
    planet.atmosphere = "Nitrogen"
    planet.surface = "Icy"
    result = planet.get_surface_info()
    assert "Venus" in result
    assert "Nitrogen" in result
    assert "Icy" in result


def test_planet_invalid_mass():
    planet = Planet()
    with pytest.raises(InvalidMassError):
        planet.mass = -100


def test_planet_invalid_position():
    planet = Planet()
    with pytest.raises(InvalidPositionError):
        planet.position = (0.0, 0.0)


def test_planet_invalid_radius():
    planet = Planet()
    with pytest.raises(InvalidRadiusError):
        planet.radius = -10.0


def test_planet_surface_validation():
    planet = Planet()
    with pytest.raises(InvalidSurfaceError):
        planet.surface = "idk"


def test_planet_set_atmosphere():
    planet = Planet()
    planet.name = "Earth"
    planet.mass = 1.0
    planet.position = (0.0, 0.0, 0.0)
    planet.radius = 1.0
    planet.atmosphere = "CO2, N2"
    assert planet.atmosphere == "CO2, N2"


def test_planet_set_has_rings():
    planet = Planet()
    planet.name = "Earth"
    planet.mass = 1.0
    planet.position = (0.0, 0.0, 0.0)
    planet.radius = 1.0
    planet.has_rings = True
    assert planet.has_rings is True


def test_planet_add_satellite():
    planet = Planet()
    planet.name = "Earth"
    satellite = Satellite()
    satellite.name = "Moon"
    planet.add_satellite(satellite)
    assert len(planet.satellites) == 1
    assert planet.satellites[0].name == "Moon"


def test_planet_remove_satellite():
    planet = Planet()
    planet.name = "Earth"
    satellite = Satellite()
    satellite.name = "Moon"
    planet.add_satellite(satellite)
    assert len(planet.satellites) == 1
    planet.remove_satellite(satellite)
    assert len(planet.satellites) == 0


def test_planet_set_satellites_list():
    planet = Planet()
    planet.name = "Earth"
    satellite1 = Satellite()
    satellite1.name = "Moon"
    satellite2 = Satellite()
    satellite2.name = "Phobos"
    planet.satellites = [satellite1, satellite2]
    assert len(planet.satellites) == 2
    assert planet.satellites[0].name == "Moon"
    assert planet.satellites[1].name == "Phobos"