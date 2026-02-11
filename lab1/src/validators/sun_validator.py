from exceptions.custom_exceptions import InvalidTemperatureError, InvalidLuminosityError
from src.validators.validator import Validator

class SunValidator(Validator):
    @staticmethod
    def validate_temperature(temperature: float):
        if temperature <= 0:
            raise InvalidTemperatureError("Температура должна быть положительной")
        
    @staticmethod
    def validate_luminosity(luminosity: float):
        if luminosity <= 0:
            raise InvalidLuminosityError("Светимость Солнца должна быть положительной")