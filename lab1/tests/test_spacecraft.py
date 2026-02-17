import pytest
from src.spacecraft import Spacecraft
from src.planet import Planet
from exceptions.custom_exceptions import InvalidFuelError, InvalidStatusError, LaunchError


def test_spacecraft_creation():
    spacecraft = Spacecraft(
        fuel=5000.0,
        status="idle"
    )

    spacecraft.name = "Mars Rover"
    spacecraft.mass = 1000.0
    spacecraft.position = (0.0, 0.0, 0.0)
    spacecraft.radius = 2.0

    assert spacecraft.name == "Mars Rover"
    assert spacecraft.mass == 1000.0
    assert spacecraft.position == (0.0, 0.0, 0.0)
    assert spacecraft.radius == 2.0
    assert spacecraft.fuel == 5000.0
    assert spacecraft.status == "idle"


def test_spacecraft_travel_to():
    spacecraft = Spacecraft(fuel=1000.0)
    planet = Planet()
    planet.name = "Марс"
    planet.position = (1e11, 0.0, 0.0)
    spacecraft.travel_to(planet)
    assert spacecraft.position == planet.position
    assert spacecraft.status == "idle"


def test_spacecraft_collect_data():
    spacecraft = Spacecraft()
    planet = Planet()
    planet.name = "Земля"
    planet.mass = 5.97e24
    data = spacecraft.collect_data(planet)
    assert data["object_name"] == "Земля"
    assert data["mass"] == 5.97e24


def test_spacecraft_launch():
    spacecraft = Spacecraft(fuel=1000.0)
    spacecraft.launch()
    assert spacecraft.status == "traveling"


def test_spacecraft_launch_no_fuel():
    spacecraft = Spacecraft(fuel=0.0)
    with pytest.raises(LaunchError):
        spacecraft.launch()


def test_spacecraft_invalid_fuel():
    spacecraft = Spacecraft()
    with pytest.raises(InvalidFuelError):
        spacecraft.fuel = -100.0


def test_spacecraft_invalid_status():
    spacecraft = Spacecraft()
    with pytest.raises(InvalidStatusError):
        spacecraft.status = "invalid_status"