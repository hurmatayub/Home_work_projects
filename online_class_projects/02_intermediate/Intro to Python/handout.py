def mars_weight():
    earth_weight = float(input("Enter a weight on Earth: "))
    mars_weight = earth_weight * 0.378
    rounded_mars_weight = round(mars_weight, 2)
    print(f"The equivalent on Mars: {rounded_mars_weight}")

def planetary_weight():
    gravity_constants = {
        "Mercury": 0.376,
        "Venus": 0.889,
        "Mars": 0.378,
        "Jupiter": 2.36,
        "Saturn": 1.081,
        "Uranus": 0.815,
        "Neptune": 1.14
    }

    earth_weight = float(input("Enter a weight on Earth: "))
    planet = input("Enter a planet: ")

    if planet in gravity_constants:
        planet_weight = earth_weight * gravity_constants[planet]
        rounded_planet_weight = round(planet_weight, 2)
        print(f"The equivalent weight on {planet}: {rounded_planet_weight}")
    else:
        print("Invalid planet name!")

def main():
    print("Welcome to the Planetary Weight Calculator!")
    print("Choose an option:")
    print("1. Calculate weight on Mars")
    print("2. Calculate weight on another planet")
    
    choice = input("Enter your choice (1 or 2): ")

    if choice == '1':
        mars_weight()
    elif choice == '2':
        planetary_weight()
    else:
        print("Invalid choice. Exiting...")

if __name__ == "__main__":
    main()
