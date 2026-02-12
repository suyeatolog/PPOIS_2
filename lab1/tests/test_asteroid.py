import pytest
from src.asteroid import Asteroid
from exceptions.custom_exceptions import InvalidCompositionError, InvalidOrbitTypeError


def test_asteroid_creation():
    asteroid = Asteroid(composition="rocky", orbit_type="main belt")
    asteroid.name = "Ceres"
    asteroid.mass = 9.39e20
    asteroid.position = (2.77e11, 0.0, 0.0)
    asteroid.radius = 473.0
    asteroid.composition = "rocky"
    asteroid.orbit_type = "main belt"

    assert asteroid.name == "Ceres"
    assert asteroid.mass == 9.39e20
    assert asteroid.position == (2.77e11, 0.0, 0.0)
    assert asteroid.radius == 473.0
    assert asteroid.composition == "rocky"
    assert asteroid.orbit_type == "main belt"


def test_asteroid_move():
    asteroid = Asteroid()
    initial_x = asteroid.position[0]
    asteroid.move(dt=10)
    expected_x = initial_x + 0.05 * 10
    assert asteroid.position[0] == expected_x


def test_asteroid_set_composition():
    asteroid = Asteroid()
    asteroid.composition = "metallic"
    assert asteroid.composition == "metallic"


def test_asteroid_set_orbit_type():
    asteroid = Asteroid()
    asteroid.orbit_type = "near-earth"
    assert asteroid.orbit_type == "near-earth"


def test_asteroid_invalid_composition():
    asteroid = Asteroid()
    with pytest.raises(InvalidCompositionError):
        asteroid.composition = "unknown composition"


def test_asteroid_invalid_orbit_type():
    asteroid = Asteroid()
    with pytest.raises(InvalidOrbitTypeError):
        asteroid.orbit_type = "invalid orbit"
