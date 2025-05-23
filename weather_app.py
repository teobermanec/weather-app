import requests
from config import API_KEY, BASE_URL_CURRENT, BASE_URL_FORECAST

def get_current_weather(city, units='metric'):
    params = {
        'q': city,
        'appid': API_KEY,
        'units': units
    }
    try:
        response = requests.get(BASE_URL_CURRENT, params=params)
        data = response.json()
        if response.status_code != 200:
            return None, data.get("message", "Unknown error")
        return data, None
    except Exception as e:
        return None, str(e)

def get_forecast(city, units='metric'):
    params = {
        'q': city,
        'appid': API_KEY,
        'units': units
    }
    try:
        response = requests.get(BASE_URL_FORECAST, params=params)
        data = response.json()
        if response.status_code != 200:
            return None, data.get("message", "Unknown error")
        return data, None
    except Exception as e:
        return None, str(e)
