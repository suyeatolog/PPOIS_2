from exceptions.custom_exceptions import InvalidSurfaceError
from src.validators.validator import Validator

class PlanetValidator(Validator):

    @staticmethod
    def validate_surface(surface: str):
        surface_types: str = ("Rocky", "Icy", "Gas")
        if surface not in surface_types:
            raise InvalidSurfaceError("Unknown surface type. Try: Rocky/Icy/Gas")