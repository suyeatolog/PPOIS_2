from src.solar_system_initializer import SolarSystemInitializer
from src.asteroid import Asteroid
from src.comet import Comet
from src.satellite import Satellite


def show_main_menu():
    print("\n--- Solar System Simulator ---")
    print("1. Show all celestial bodies")
    print("2. Add/remove celestial bodies")
    print("3. Control spacecraft")
    print("4. Exit")
    print("-----------------------------")


def show_manage_bodies_menu():
    print("\n--- Manage Celestial Bodies ---")
    print("1. Add asteroid")
    print("2. Add comet")
    print("3. Add satellite")
    print("4. Remove asteroid")
    print("5. Remove comet")
    print("6. Remove satellite")
    print("7. Back to main menu")
    print("------------------------------")


def show_control_spacecraft_menu():
    print("\n--- Control Spacecraft ---")
    print("1. Launch spacecraft")
    print("2. Travel to a celestial body")
    print("3. Collect data from current object")
    print("4. Back to main menu")
    print("-------------------------")


def get_valid_float(prompt: str) -> float:
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Please enter a valid number.")


def get_valid_positive_float(prompt: str) -> float:
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Value must be positive.")
                continue
            return value
        except ValueError:
            print("Please enter a valid number.")


def get_valid_string(prompt: str, valid_options: set = None) -> str:
    while True:
        value = input(prompt).strip()
        if not value:
            print("Value cannot be empty.")
            continue
        if valid_options and value not in valid_options:
            print(f"Invalid option. Valid options: {', '.join(valid_options)}")
            continue
        return value


def main():
    print("Welcome! Press 'Enter' to start.")
    input()

    initializer = SolarSystemInitializer()
    solar_system = initializer.get_solar_system()
    current_target = None

    while True:
        show_main_menu()
        choice = input("Enter your choice: ")

        match choice:
            case "1":
                print("\nAll celestial bodies:")
                for body in solar_system.get_all_bodies():
                    print(body.get_info())

            case "2":
                while True:
                    show_manage_bodies_menu()
                    sub_choice = input("Enter your choice: ")

                    match sub_choice:
                        case "1":
                            name = input("Enter asteroid name: ").strip()
                            composition = get_valid_string("Enter composition (rocky, metallic, carbonaceous): ",
                                                           {"rocky", "metallic", "carbonaceous"})
                            orbit_type = get_valid_string("Enter orbit type (main belt, near-earth, trojan, centaur, trans-neptunian): ",
                                                          {"main belt", "near-earth", "trojan", "centaur", "trans-neptunian"})
                            mass = get_valid_positive_float("Enter mass: ")
                            x = get_valid_float("Enter X coordinate: ")
                            y = get_valid_float("Enter Y coordinate: ")
                            z = get_valid_float("Enter Z coordinate: ")
                            radius = get_valid_positive_float("Enter radius: ")

                            asteroid = Asteroid(composition=composition, orbit_type=orbit_type)
                            asteroid.name = name
                            asteroid.mass = mass
                            asteroid.position = (x, y, z)
                            asteroid.radius = radius
                            solar_system.add_body(asteroid)
                            print(f"Asteroid '{name}' added successfully.")

                        case "2":
                            name = input("Enter comet name: ").strip()
                            core_diameter = get_valid_positive_float("Enter core diameter: ")
                            period = get_valid_positive_float("Enter orbital period: ")
                            eccentricity = get_valid_float("Enter eccentricity (0-1): ")
                            if not 0 <= eccentricity <= 1:
                                print("Eccentricity must be between 0 and 1.")
                                continue
                            mass = get_valid_positive_float("Enter mass: ")
                            x = get_valid_float("Enter X coordinate: ")
                            y = get_valid_float("Enter Y coordinate: ")
                            z = get_valid_float("Enter Z coordinate: ")
                            radius = get_valid_positive_float("Enter radius: ")

                            comet = Comet(core_diameter=core_diameter, period=period, eccentricity=eccentricity)
                            comet.name = name
                            comet.mass = mass
                            comet.position = (x, y, z)
                            comet.radius = radius
                            solar_system.add_body(comet)
                            print(f"Comet '{name}' added successfully.")

                        case "3":
                            name = input("Enter satellite name: ").strip()
                            
                            # Получаем список планет и проверяем, что введённая планета существует
                            planets = solar_system.get_planets()
                            planet_names = {p.name for p in planets}
                            while True:
                                orbited_planet = input("Enter orbited planet: ").strip()
                                if orbited_planet not in planet_names:
                                    print(f"Planet '{orbited_planet}' does not exist. Available planets: {', '.join(planet_names)}")
                                    continue
                                break

                            orbital_period = get_valid_positive_float("Enter orbital period: ")
                            distance = get_valid_positive_float("Enter distance from planet: ")
                            mass = get_valid_positive_float("Enter mass: ")
                            x = get_valid_float("Enter X coordinate: ")
                            y = get_valid_float("Enter Y coordinate: ")
                            z = get_valid_float("Enter Z coordinate: ")
                            radius = get_valid_positive_float("Enter radius: ")

                            satellite = Satellite(orbited_planet=orbited_planet, orbital_period=orbital_period, distance_from_planet=distance)
                            satellite.name = name
                            satellite.mass = mass
                            satellite.position = (x, y, z)
                            satellite.radius = radius
                            solar_system.add_body(satellite)
                            print(f"Satellite '{name}' added successfully.")

                        case "4":
                            asteroids = solar_system.get_asteroids()
                            if not asteroids:
                                print("No asteroids available to remove.")
                                continue
                            print("Available asteroids:")
                            for i, ast in enumerate(asteroids):
                                print(f"{i + 1}. {ast.name}")
                            idx = int(input("Choose asteroid by number: ")) - 1
                            if 0 <= idx < len(asteroids):
                                asteroid = asteroids[idx]
                                solar_system.remove_body(asteroid)
                                print(f"Asteroid '{asteroid.name}' removed successfully.")
                            else:
                                print("Invalid selection.")

                        case "5":
                            comets = solar_system.get_comets()
                            if not comets:
                                print("No comets available to remove.")
                                continue
                            print("Available comets:")
                            for i, comet in enumerate(comets):
                                print(f"{i + 1}. {comet.name}")
                            idx = int(input("Choose comet by number: ")) - 1
                            if 0 <= idx < len(comets):
                                comet = comets[idx]
                                solar_system.remove_body(comet)
                                print(f"Comet '{comet.name}' removed successfully.")
                            else:
                                print("Invalid selection.")

                        case "6":
                            satellites = solar_system.get_satellites()
                            if not satellites:
                                print("No satellites available to remove.")
                                continue
                            print("Available satellites:")
                            for i, sat in enumerate(satellites):
                                print(f"{i + 1}. {sat.name}")
                            idx = int(input("Choose satellite by number: ")) - 1
                            if 0 <= idx < len(satellites):
                                satellite = satellites[idx]
                                solar_system.remove_body(satellite)
                                print(f"Satellite '{satellite.name}' removed successfully.")
                            else:
                                print("Invalid selection.")

                        case "7":
                            break

                        case _:
                            print("Invalid choice. Please try again.")

            case "3":
                while True:
                    show_control_spacecraft_menu()
                    sub_choice = input("Enter your choice: ")

                    match sub_choice:
                        case "1":
                            try:
                                spacecraft = solar_system.get_spacecraft()
                                if spacecraft:
                                    spacecraft.launch()
                                    print(f"Spacecraft {spacecraft.name} launched successfully!")
                                else:
                                    print("No spacecraft found.")
                            except Exception as e:
                                print(f"Error: {e}")

                        case "2":
                            try:
                                spacecraft = solar_system.get_spacecraft()
                                if not spacecraft:
                                    print("No spacecraft found.")
                                    break

                                if spacecraft.status != "traveling":
                                    print("Spacecraft is not launched. Please launch it first.")
                                    continue

                                print("Available targets:")
                                targets = [body for body in solar_system.get_all_bodies() if body != spacecraft]
                                for i, body in enumerate(targets):
                                    print(f"{i + 1}. {body.name}")

                                target_idx = int(input("Choose target by number: ")) - 1
                                if 0 <= target_idx < len(targets):
                                    target = targets[target_idx]
                                    spacecraft.travel_to(target)
                                    current_target = target
                                    print(f"Spacecraft traveled to {target.name}")
                                else:
                                    print("Invalid selection.")
                            except Exception as e:
                                print(f"Error: {e}")

                        case "3":
                            try:
                                spacecraft = solar_system.get_spacecraft()
                                if not spacecraft:
                                    print("No spacecraft found.")
                                    continue

                                if current_target is None:
                                    print("Spacecraft hasn't traveled to any object yet.")
                                    continue

                                if hasattr(current_target, 'atmosphere') and hasattr(current_target, 'surface'):
                                    data = spacecraft.collect_atmosphere_and_surface_data(current_target)
                                    print(f"Collected planet  {data}")
                                elif hasattr(current_target, 'period') and hasattr(current_target, 'eccentricity'):
                                    data = spacecraft.collect_comet_data(current_target)
                                    print(f"Collected comet  {data}")
                                elif hasattr(current_target, 'composition') and hasattr(current_target, 'orbit_type'):
                                    data = spacecraft.collect_asteroid_data(current_target)
                                    print(f"Collected asteroid  {data}")
                                elif hasattr(current_target, 'luminosity'):
                                    print("Too hot to collect data. It is highly recommended to leave asap.")
                                else:
                                    print("Current object doesn't support data collection.")

                            except Exception as e:
                                print(f"Error: {e}")

                        case "4":
                            break

                        case _:
                            print("Invalid choice. Please try again.")

            case "4":
                print("Goodbye!")
                break

            case _:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()