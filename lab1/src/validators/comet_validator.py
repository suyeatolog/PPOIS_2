from exceptions.custom_exceptions import InvalidCoreDiameterError, InvalidPeriodError, InvalidTailLengthError
from src.validators.validator import Validator

class CometValidator(Validator):
    @staticmethod
    def validate_core_diameter(core_diameter: float):
        if core_diameter <= 0:
            raise InvalidCoreDiameterError("Радиус ядра кометы должен быть положительной")
        
    @staticmethod
    def validate_period(period: float):
        if period <= 0:
            raise InvalidPeriodError("Период кометы должен быть положительной")
        
    @staticmethod
    def validate_eccentricity(eccentricity: float):
        if eccentricity < 0 or eccentricity > 1:
            raise InvalidPeriodError("Эксцентриситет орбиты кометы должен быть в пределах от 0 до 1")
    
    @staticmethod
    def validate_tail_length(tail_length: float):
        if tail_length < 0:
            raise InvalidTailLengthError("Длина хвоста планеты не может быть меньше 0")