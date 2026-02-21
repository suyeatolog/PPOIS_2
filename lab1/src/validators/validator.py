from exceptions.custom_exceptions import InvalidMassError, InvalidPositionError, InvalidRadiusError

class Validator:
    @staticmethod
    def validate_mass(mass: float) -> None:
        if mass <= 0:
            raise InvalidMassError("Mass must be positive")
        
    @staticmethod
    def validate_position(position: tuple[float, float, float]) -> None:
        if len(position) != 3:
            raise InvalidPositionError("Position must be in form (0.0, 0.0, 0.0)")
        if not all(isinstance(x, (int, float)) for x in position):
            raise InvalidPositionError("Coordinates must be numbers")
        
    @staticmethod
    def validate_radius(radius: float) -> None:
        if radius <= 0:
            raise InvalidRadiusError("Radius must be positive")
