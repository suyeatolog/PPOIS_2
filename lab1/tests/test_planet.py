import pytest
from src.planet import Planet
from exceptions.custom_exceptions import (
    InvalidMassError,
    InvalidPositionError,
    InvalidRadiusError,
    InvalidSurfaceError
)


def test_planet_creation():
    planet = Planet(atmosphere="Nitrogen, Oxygen", has_rings=False, surface="Rocky")
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
    planet.atmosphere = "Nytrogen"
    planet.surface = "Icy"
    result = planet.get_surface_info()
    assert "Venus" in result
    assert "Nytrogen" in result
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
    planet.name = "Test"
    planet.mass = 1.0
    planet.position = (0.0, 0.0, 0.0)
    planet.radius = 1.0
    planet.atmosphere = "CO2, N2"
    assert planet.atmosphere == "CO2, N2"


def test_planet_set_has_rings():
    planet = Planet()
    planet.name = "Test"
    planet.mass = 1.0
    planet.position = (0.0, 0.0, 0.0)
    planet.radius = 1.0
    planet.has_rings = True
    assert planet.has_rings is True