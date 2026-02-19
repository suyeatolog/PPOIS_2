import pytest
from src.satellite import Satellite
from exceptions.custom_exceptions import (
    InvalidOrbitedPlanetError,
    InvalidOrbitalPeriodError,
    InvalidDistanceError,
)


def test_satellite_creation():
    satellite = Satellite(
        orbited_planet="Earth", orbital_period=27.3, distance_from_planet=384400.0
    )
    satellite.name = "Moon"
    satellite.mass = 7.34e22
    satellite.position = (0.0, 0.0, 0.0)
    satellite.radius = 1737.4
    assert satellite.name == "Moon"
    assert satellite.mass == 7.34e22
    assert satellite.position == (0.0, 0.0, 0.0)
    assert satellite.radius == 1737.4
    assert satellite.orbited_planet == "Earth"
    assert satellite.orbital_period == 27.3
    assert satellite.distance_from_planet == 384400.0


def test_satellite_move():
    satellite = Satellite()
    initial_x = satellite.position[0]
    satellite.move(dt=10)
    expected_x = initial_x + 0.05 * 10
    assert satellite.position[0] == expected_x


def test_satellite_set_orbited_planet():
    satellite = Satellite()
    satellite.orbited_planet = "Mars"
    assert satellite.orbited_planet == "Mars"


def test_satellite_set_orbital_period():
    satellite = Satellite()
    satellite.orbital_period = 30.0
    assert satellite.orbital_period == 30.0


def test_satellite_set_distance_from_planet():
    satellite = Satellite()
    satellite.distance_from_planet = 400000.0
    assert satellite.distance_from_planet == 400000.0


def test_satellite_invalid_orbited_planet():
    satellite = Satellite()
    with pytest.raises(InvalidOrbitedPlanetError):
        satellite.orbited_planet = "Fake Planet"


def test_satellite_invalid_orbital_period():
    satellite = Satellite()
    with pytest.raises(InvalidOrbitalPeriodError):
        satellite.orbital_period = -1.0


def test_satellite_invalid_distance():
    satellite = Satellite()
    with pytest.raises(InvalidDistanceError):
        satellite.distance_from_planet = -1000.0
