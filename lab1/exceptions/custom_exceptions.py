class SolarSystemError(Exception): #базовое исключение для солнечной системы
    pass

class InvalidMassError(SolarSystemError): #если масса <= 0
    pass

class InvalidRadiusError(SolarSystemError): #если радиус <= 0
    pass

class InvalidPositionError(SolarSystemError): #если не 3 элемента передано в tuple для координат
    pass

class InvalidTemperatureError(SolarSystemError): #если температура Солнца <= 0
    pass

class InvalidLuminosityError(SolarSystemError): #если светимость Солнца <= 0
    pass

class InvalidCoreDiameterError(SolarSystemError): #если радиус ядра кометы <= 0
    pass

class InvalidPeriodError(SolarSystemError): #если период кометы <= 0
    pass

class InvalidEccentricityError(SolarSystemError): #если эксцентреситет орбиты кометы < 0 или > 1
    pass

class InvalidTailLengthError(SolarSystemError): #если длина хвоста кометы < 0
    pass