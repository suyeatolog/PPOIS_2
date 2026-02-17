class SolarSystemError(Exception): # базовое исключение для солнечной системы
    pass

class InvalidMassError(SolarSystemError): # если масса <= 0
    pass

class InvalidRadiusError(SolarSystemError): # если радиус <= 0
    pass

class InvalidPositionError(SolarSystemError): # если не 3 элемента передано в tuple для координат
    pass

class InvalidTemperatureError(SolarSystemError): # если температура Солнца <= 0
    pass

class InvalidSurfaceError(SolarSystemError): # если поверхность не Каменистая, Газовая, Ледяная
    pass

class InvalidLuminosityError(SolarSystemError): # если светимость Солнца <= 0
    pass

class InvalidCoreDiameterError(SolarSystemError): # если радиус ядра кометы <= 0
    pass

class InvalidPeriodError(SolarSystemError): # если период кометы <= 0
    pass

class InvalidEccentricityError(SolarSystemError): # если эксцентреситет орбиты кометы < 0 или > 1
    pass

class InvalidTailLengthError(SolarSystemError): # если длина хвоста кометы < 0
    pass

class InvalidCompositionError(SolarSystemError): # если состав не каменный/углеродный(карбонат)/металлический
    pass

class InvalidOrbitTypeError(SolarSystemError): # если орбита астероида не: Главного пояса, Околоземная, Троянская, Кентавр, Транснептуновая
    pass

class InvalidOrbitedPlanetError(SolarSystemError): # если планеты нет в Солнечной системе, или пустая строка
    pass

class InvalidOrbitalPeriodError(SolarSystemError): # если период спутника <= 0
    pass

class InvalidDistanceError(SolarSystemError): # если дистанция от Солнца <= 0
    pass

class InvalidFuelError(SolarSystemError): # если топливо < 0 
    pass

class InvalidStatusError(SolarSystemError): # если состояние не idle, traveling, researching, returning
    pass

class LaunchError(SolarSystemError): # если невозможно запустить корабль
    pass