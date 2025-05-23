from weather_app import get_current_weather, get_forecast
from utils import format_weather, format_forecast, format_grouped_forecast
from favorites import load_favorites, add_favorite, remove_favorite
import sys

def city_menu():
    print("\n--- City Selection ---")
    favorites = load_favorites()
    if favorites:
        print("Choose a city, enter a new one or quit:")
        for i, city in enumerate(favorites, 1):
            print(f"{i}. {city}")
        print("0. Enter a new city")
        print("9. Quit")
        try:
            choice = int(input("Selection: "))
            if choice == 0:
                return input("Enter new city: ").strip()
            elif 1 <= choice <= len(favorites):
                return favorites[choice - 1]
            elif choice == 9:
                print("Goodbye!")
                sys.exit()
        except ValueError:
            print("Invalid selection.")
    else:
        return input("Enter city name: ").strip()

def main():
    units = 'metric'

    while True:
        city = city_menu()
        print(f"\nSelected city: {city}")

        print("\n--- Weather App CLI ---")
        print("1. Current Weather")
        print("2. 5x Forecast")
        print("3. Add to Favorites")
        print("4. Remove from Favorites")
        print("5. Switch Units (Current: Celsius)" if units == 'metric' else "5. Switch Units (Current: Fahrenheit)")
        print("6. Grouped 5-Day Forecast")
        print("7. Export Forecast to File")
        print("8. Get weather for current location (GPS/IP)")
        print("9. Exit")

        choice = input("Select an option: ")

        if choice == '1':
            data, error = get_current_weather(city, units)
            print(f"Current Weather in {city}")
            print(format_weather(data) if not error else f"Error: {error}")

        elif choice == '2':
            data, error = get_forecast(city, units)
            print(f"Forecast for {city}")
            print(format_forecast(data) if not error else f"Error: {error}")

        elif choice == '3':
            if add_favorite(city):
                print(f"Added {city} to favorites.")
            else:
                print(f"{city} is already in favorites.")

        elif choice == '4':
            if remove_favorite(city):
                print(f"Removed {city} from favorites.")
            else:
                print(f"{city} not found in favorites.")

        elif choice == '5':
            units = 'imperial' if units == 'metric' else 'metric'
            print(f"Units switched to {'Celsius' if units == 'metric' else 'Fahrenheit'}.")

        elif choice == '6':
            data, error = get_forecast(city, units)
            print(format_grouped_forecast(data) if not error else f"Error: {error}")

        elif choice == '7':
            data, error = get_forecast(city, units)
            if error:
                print(f"Error: {error}")
            else:
                with open(f"{city}_forecast.txt", "w") as f:
                    f.write(format_grouped_forecast(data))
                print(f"Forecast exported to {city}_forecast.txt")

        elif choice == '8':
            from location import get_location
            loc, error = get_location()
            if error:
                print(f"Location error: {error}")
            else:
                print(f"\nDetected Location: {loc['city']}, {loc['country']}")
                city = loc['city']

                data, error = get_current_weather(city, units)
                if error:
                    print(f"Weather error: {error}")
                else:
                    print(format_weather(data))

                data, error = get_forecast(city, units)
                if error:
                    print(f"Forecast error: {error}")
                else:
                    print(format_grouped_forecast(data))

        elif choice == '9':
            print("Goodbye!")
            break

        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()