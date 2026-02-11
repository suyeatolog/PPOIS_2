import pytest
from src.planet import Planet
from exceptions.custom_exceptions import InvalidMassError, InvalidPositionError, InvalidRadiusError

def test_planet_creation():
    planet = Planet(
        name="Earth",
        mass=5.97e24,
        position=(0.0, 0.0, 0.0),
        radius=6371.0,
        atmosphere="Nitrogen, Oxygen",
        has_rings=False
    )
    assert planet.name == "Earth"
    assert planet.mass == 5.97e24
    assert planet.position == (0.0, 0.0, 0.0)
    assert planet.radius == 6371.0
    assert planet.atmosphere == "Nitrogen, Oxygen"
    assert planet.has_rings is False

def test_planet_move():
    planet=Planet(
        name="Earth",
        mass=5.97e24,
        position=(0.0, 0.0, 0.0),
        radius=6371.0
        
    )
    planet.move(dt=10)
    assert planet.position[0] == 1.0

def test_planet_get_surface_info():
    planet = Planet(
        name="Venus",
        mass=4.86e24,
        position=(0.0, 0.0, 0.0),
        radius=6052.0
    )
    result = planet.get_surface_info()
    assert "Venus" in result

def test_planet_invalid_mass():
    with pytest.raises(InvalidMassError):
        Planet(
            name="Fake",
            mass=-100,
            position=(0.0, 0.0, 0.0),
            radius=1000.0
        )

def test_planet_invalid_position():
    with pytest.raises(InvalidPositionError):
        Planet(
            name="Fake",
            mass=100,
            position=(0.0, 0.0),
            radius=1000.0
        )

def test_planet_invalid_radius():
    with pytest.raises(InvalidRadiusError):
        Planet(
            name="Fake",
            mass=100,
            position=(0.0, 0.0, 0.0),
            radius=-10.0
        )