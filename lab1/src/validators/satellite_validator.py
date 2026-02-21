from exceptions.custom_exceptions import InvalidOrbitedPlanetError, InvalidOrbitalPeriodError, InvalidDistanceError
from src.validators.validator import Validator
class SatelliteValidator(Validator):
    @staticmethod
    def validate_orbited_planet(planet: str):
        if not isinstance(planet, str) or not planet.strip():
            raise InvalidOrbitedPlanetError("Planet name mustn't be empty string")
        valid_planets = {"Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"}
        if planet not in valid_planets:
            raise InvalidOrbitedPlanetError(f"{planet} doesn't exist in Solar System")

    @staticmethod
    def validate_orbital_period(period: float):
        if period <= 0:
            raise InvalidOrbitalPeriodError("Orbital period must be positive")

    @staticmethod
    def validate_distance(distance: float):
        if distance <= 0:
            raise InvalidDistanceError("Distance must be positive")