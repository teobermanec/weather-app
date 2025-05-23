import requests
def get_location():
    try:
        response = requests.get("http://ip-api.com/json/")
        if response.status_code == 200:
            data = response.json()
            return {
                "city": data.get("city"),
                "lat": data.get("lat"),
                "lon": data.get("lon"),
                "country": data.get("country")
            }, None
        else:
            return None, "Failed to fetch location info."
    except Exception as e:
        return None, str(e)