from exceptions.custom_exceptions import InvalidFuelError, InvalidStatusError
from src.validators.validator import Validator

class SpacecraftValidator(Validator):
    @staticmethod
    def validate_fuel(fuel: float):
        if fuel < 0:
            raise InvalidFuelError("Fuel must be positive")

    @staticmethod
    def validate_status(status: str):
        valid_statuses = {"idle", "traveling", "researching", "returning"}
        if status not in valid_statuses:
            raise InvalidStatusError(f"Unknown status: {status}")