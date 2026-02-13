from exceptions.custom_exceptions import InvalidOrbitedPlanetError, InvalidOrbitalPeriodError, InvalidDistanceError
from src.validators.validator import Validator
class SatelliteValidator(Validator):
    @staticmethod
    def validate_orbited_planet(planet: str):
        if not isinstance(planet, str) or not planet.strip():
            raise InvalidOrbitedPlanetError("Планета должна быть непустой строкой")
        valid_planets = {"Меркурий", "Венера", "Земля", "Марс", "Юпитер", "Сатурн", "Уран", "Нептун"}
        if planet not in valid_planets:
            raise InvalidOrbitedPlanetError(f"Не существует планеты {planet} в Солнечной системе")

    @staticmethod
    def validate_orbital_period(period: float):
        if period <= 0:
            raise InvalidOrbitalPeriodError("Орбитальный период должен быть положительным")

    @staticmethod
    def validate_distance(distance: float):
        if distance <= 0:
            raise InvalidDistanceError("Расстояние до планеты должно быть положительным")