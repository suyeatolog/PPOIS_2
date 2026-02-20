import pytest
from src.spacecraft import Spacecraft
from src.planet import Planet
from exceptions.custom_exceptions import InvalidFuelError, InvalidStatusError, LaunchError, FullFuelError
from src.comet import Comet
from src.asteroid import Asteroid
from src.satellite import Satellite

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

def test_fulfill_spaceship():
    spacecraft = Spacecraft(fuel=1000.0)
    planet = Planet()
    planet.name = "Earth"
    spacecraft.launch()
    spacecraft.travel_to(planet)
    with pytest.raises(LaunchError):
        spacecraft.launch()
    spacecraft.fuel_up_spaceship()
    with pytest.raises(FullFuelError):
        spacecraft.fuel_up_spaceship()
    spacecraft.launch()
    assert spacecraft.status == "traveling"

def test_spacecraft_collect_data():
    spacecraft = Spacecraft()
    planet = Planet()
    planet.name = "Earth"
    planet.mass = 5.97e24
    data = spacecraft.collect_data(planet)
    assert data["object_name"] == "Earth"
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

def test_spacecraft_surface_atmosphere_data_collection():
    spacecraft = Spacecraft()
    planet = Planet()
    planet.name = "Earth"
    planet.atmosphere = "Nitrogen, Oxygen"
    planet.surface = "Rocky"
    planet.has_rings = False
    data = spacecraft.collect_atmosphere_and_surface_data(planet)
    assert data["planet_name"] == "Earth"
    assert data["atmosphere"] == "Nitrogen, Oxygen"
    assert data["surface"] == "Rocky"
    assert not data["has_rings"]

def test_spacecraft_comet_data_collection():
    spacecraft = Spacecraft()
    comet = Comet()
    comet.name = "Haley"
    comet.period = 75.3
    comet.eccentricity = 0.9
    comet.tail_length = 0.0
    data = spacecraft.collect_comet_data(comet)
    assert data["comet_name"] == "Haley"
    assert data["period"] == 75.3
    assert data["eccentricity"] == 0.9
    assert data["tail_length"] == 0.0

def test_spacecraft_asteroid_data_collection():
    spacecraft = Spacecraft()
    asteroid = Asteroid()
    asteroid.name = "Ceres"
    asteroid.composition = "rocky"
    asteroid.orbit_type = "main belt"
    data = spacecraft.collect_asteroid_data(asteroid)
    assert data["asteroid_name"] == "Ceres"
    assert data["composition"] == "rocky"
    assert data["orbit_type"] == "main belt"

def test_spacecraft_satellite_data_collection():
    spacecraft = Spacecraft()
    satellite = Satellite("Earth", 27.3, 384400.0)
    satellite.name = "Moon"
    data = spacecraft.collect_satellite_data(satellite)
    assert data["orbited_planet"] == "Earth"
    assert data["orbital_period"] == 27.3
    assert data["distance_from_planet"] == 384400.0