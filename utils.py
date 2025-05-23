from datetime import datetime
from colorama import Fore, Style, init
from collections import defaultdict

# Only needed once in the whole app
init(autoreset=True)

def format_grouped_forecast(data):
    result = f"\n{Fore.LIGHTCYAN_EX}5-Day Forecast Summary:{Style.RESET_ALL}\n"
    forecast_by_day = defaultdict(list)

    for entry in data['list']:
        dt = datetime.strptime(entry['dt_txt'], "%Y-%m-%d %H:%M:%S")
        day = dt.strftime("%A, %b %d")
        temp = int(entry['main']['temp'])
        desc = entry['weather'][0]['description']
        forecast_by_day[day].append((dt, temp, desc))

    for day, entries in list(forecast_by_day.items())[:5]:
        result += f"\n{Fore.LIGHTCYAN_EX}{day}:{Style.RESET_ALL}\n"
        for dt, temp, desc in entries:
            time = dt.strftime("%H:%M")
            result += f"  {Fore.LIGHTYELLOW_EX}{time}{Style.RESET_ALL} -> {temp}°, {desc.title()}\n"

    return result

def format_weather(data):
    name = data['name']
    temp = int(data['main']['temp'])
    desc = data['weather'][0]['description']
    humidity = data['main']['humidity']
    wind = int(data['wind']['speed']*3.6)

    return (
        f"\n{Fore.LIGHTYELLOW_EX}Weather in {name}:{Style.RESET_ALL}\n"
        f"{Fore.LIGHTWHITE_EX}Temperature: {temp}°{Style.RESET_ALL}\n"
        f"{Fore.LIGHTWHITE_EX}Condition: {desc.title()}{Style.RESET_ALL}\n"
        f"{Fore.LIGHTWHITE_EX}Humidity: {humidity}%{Style.RESET_ALL}\n"
        f"{Fore.LIGHTWHITE_EX}Wind Speed: {wind} km/h{Style.RESET_ALL}\n"
    )

def format_forecast(data):
    forecast_list = data['list'][:5]
    result = f"\n{Fore.LIGHTYELLOW_EX}5 Upcoming Forecasts:{Style.RESET_ALL}\n"
    for entry in forecast_list:
        dt_txt = entry['dt_txt']
        dt = datetime.strptime(dt_txt, "%Y-%m-%d %H:%M:%S")
        formatted_time = dt.strftime("%A, %b %d – %H:%M")

        temp = int(entry['main']['temp'])
        desc = entry['weather'][0]['description']

        result += (
            f"{Fore.LIGHTWHITE_EX}{formatted_time} -> {Style.RESET_ALL} "
            f"{Fore.LIGHTWHITE_EX}{temp}°{Style.RESET_ALL}, "
            f"{Fore.LIGHTWHITE_EX}{desc.title()}{Style.RESET_ALL}\n"
        )
    return result