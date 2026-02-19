from exceptions.custom_exceptions import InvalidCompositionError, InvalidOrbitTypeError
from src.validators.validator import Validator

class AsteroidValidator(Validator):
    @staticmethod
    def validate_composition(composition: str):
        valid_compositions = {"rocky", "metallic", "carbonaceous"}
        if composition not in valid_compositions:
            raise InvalidCompositionError(f"Недопустимый состав: {composition}")

    @staticmethod
    def validate_orbit_type(orbit_type: str):
        valid_orbits = {"main belt", "near-earth", "trojan", "centaur", "trans-neptunian"}
        if orbit_type not in valid_orbits:
            raise InvalidOrbitTypeError(f"Недопустимый тип орбиты: {orbit_type}")