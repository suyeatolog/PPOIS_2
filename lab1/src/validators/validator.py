from exceptions.custom_exceptions import InvalidMassError, InvalidPositionError, InvalidRadiusError

class Validator:
    @staticmethod
    def validate_mass(mass: float) -> None:
        if mass <= 0:
            raise InvalidMassError("Масса должна быть положительной!")
        
    @staticmethod
    def validate_position(position: tuple[float, float, float]) -> None:
        if len(position) != 3:
            raise InvalidPositionError("Позиция должна быть представлена в виде 3-х координат: (x, y, z)")
        if not all(isinstance(x, (int, float)) for x in position):
            raise InvalidPositionError("Координаты должны быть числами")
        
    @staticmethod
    def validate_radius(radius: float) -> None:
        if radius <= 0:
            raise InvalidRadiusError("Радиус должен быть положительным")
