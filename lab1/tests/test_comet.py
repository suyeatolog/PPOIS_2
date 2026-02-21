import pytest
from src.comet import Comet
from exceptions.custom_exceptions import (
    InvalidCoreDiameterError,
    InvalidPeriodError,
    InvalidEccentricityError,
)


def test_comet_creation():
    comet = Comet(core_diameter=10.0, period=75.3, eccentricity=0.967, tail_length=0.0)
    comet.name = "Halley"
    comet.mass = 2.2e14
    comet.position = (1e12, 0.0, 0.0)
    comet.radius = 5.0

    assert comet.name == "Halley"
    assert comet.mass == 2.2e14
    assert comet.position == (1e12, 0.0, 0.0)
    assert comet.radius == 5.0
    assert comet.core_diameter == 10.0
    assert comet.period == 75.3
    assert comet.eccentricity == 0.967
    assert comet.tail_length == 0.0


def test_comet_approach_sun():
    comet = Comet()
    comet.name = "Halley"
    comet.approach_sun()
    assert comet.tail_length == 100.0
    assert comet.is_active() is True


def test_comet_get_tail_status():
    comet = Comet()
    comet.name = "Halley"
    comet.tail_length = 5000.0
    status = comet.get_tail_status()
    assert "5000.0 km" in status
    assert "Halley" in status


def test_comet_is_active():
    comet = Comet()
    assert comet.is_active() is False
    comet.tail_length = 100.0
    assert comet.is_active() is True


def test_comet_move():
    comet = Comet()
    initial_x = comet.position[0]
    comet.move(dt=10)
    expected_x = initial_x + 0.1 * 10
    assert comet.position[0] == expected_x


def test_comet_set_core_diameter():
    comet = Comet()
    comet.name = "Test"
    comet.mass = 1e10
    comet.position = (1e12, 0.0, 0.0)
    comet.radius = 1.0
    comet.core_diameter = 7.0
    assert comet.core_diameter == 7.0


def test_comet_set_period():
    comet = Comet()
    comet.name = "Test"
    comet.mass = 1e10
    comet.position = (1e12, 0.0, 0.0)
    comet.radius = 1.0
    comet.period = 50.0
    assert comet.period == 50.0


def test_comet_set_eccentricity():
    comet = Comet()
    comet.name = "Test"
    comet.mass = 1e10
    comet.position = (1e12, 0.0, 0.0)
    comet.radius = 1.0
    comet.eccentricity = 0.5
    assert comet.eccentricity == 0.5


def test_comet_invalid_core_diameter():
    comet = Comet()
    with pytest.raises(InvalidCoreDiameterError):
        comet.core_diameter = -5.0


def test_comet_invalid_period():
    comet = Comet()
    with pytest.raises(InvalidPeriodError):
        comet.period = -1.0


def test_comet_invalid_eccentricity():
    comet = Comet()
    with pytest.raises(InvalidEccentricityError):
        comet.eccentricity = -0.1
