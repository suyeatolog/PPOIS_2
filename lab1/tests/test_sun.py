import pytest
from src.sun import Sun
from exceptions.custom_exceptions import InvalidTemperatureError, InvalidLuminosityError

def test_sun_creation():
    sun = Sun(
        temperature=5778,
        luminosity=3.828e26
    )
    sun.name = "Sun"
    sun.mass = 1.989e30
    sun.position = (0.0, 0.0, 0.0)
    sun.radius = 696340.0
    assert sun.name == "Sun"
    assert sun.mass == 1.989e30
    assert sun.position == (0.0, 0.0, 0.0)
    assert sun.radius == 696340.0
    assert sun.temperature == 5778
    assert sun.luminosity == 3.828e26


def test_sun_invalid_temperature():
    sun = Sun()
    with pytest.raises(InvalidTemperatureError):
        sun.temperature = -100


def test_sun_invalid_luminosity():
    sun = Sun()
    with pytest.raises(InvalidLuminosityError):
        sun.luminosity = -1


def test_sun_move():
    sun = Sun()
    initial_pos = sun.position
    sun.move(dt=10)
    assert sun.position == initial_pos


def test_sun_get_info():
    sun = Sun(
        temperature=5778,
        luminosity=3.828e26
    )
    sun.name = "Sun"
    info = sun.get_info()
    assert "temperature = 5778" in info
    assert "luminosity = 3.83e+26" in info
    assert "Sun" in info