import pytest
from src.sun import Sun
from exceptions.custom_exceptions import InvalidTemperatureError, InvalidLuminosityError

def test_sun_creation():
    sun = Sun(
        name="Sun",
        mass=1.989e30,
        position=(0.0, 0.0, 0.0),
        radius=696340.0,
        temperature=5778,
        luminosity=3.828e26
    )
    assert sun.name == "Sun"
    assert sun.mass == 1.989e30
    assert sun.position == (0.0, 0.0, 0.0)
    assert sun.radius == 696340.0
    assert sun.temperature == 5778
    assert sun.luminosity == 3.828e26


def test_sun_invalid_temperature():
    with pytest.raises(InvalidTemperatureError):
        Sun(
            name="Fake Sun",
            mass=1.989e30,
            position=(0.0, 0.0, 0.0),
            radius=696340.0,
            temperature=-100,
            luminosity=3.828e26
        )


def test_sun_invalid_luminosity():
    with pytest.raises(InvalidLuminosityError):
        Sun(
            name="Fake Sun",
            mass=1.989e30,
            position=(0.0, 0.0, 0.0),
            radius=696340.0,
            temperature=5778,
            luminosity=-1
        )


def test_sun_move():
    sun = Sun(
        name="Sun",
        mass=1.989e30,
        position=(0.0, 0.0, 0.0),
        radius=696340.0,
        temperature=5778,
        luminosity=3.828e26
    )
    initial_pos = sun.position
    sun.move(dt=10)
    assert sun.position == initial_pos


def test_sun_get_info():
    sun = Sun(
        name="Sun",
        mass=1.989e30,
        position=(0.0, 0.0, 0.0),
        radius=696340.0,
        temperature=5778,
        luminosity=3.828e26
    )
    info = sun.get_info()
    assert "температура=5778" in info
    assert "светимость=3.83e+26" in info
    assert "Sun" in info