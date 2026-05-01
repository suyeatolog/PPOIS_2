
from solar_system_simulator import SolarSystemInitializer

initializer = SolarSystemInitializer()
ss = initializer.get_solar_system()

print("Planets:", [p.name for p in ss.get_planets()])
print("Sun:", ss.sun.name)