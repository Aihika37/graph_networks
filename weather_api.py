api="eac1064f18e78227effe3f55b8383039"
import requests
API_KEY = "YOUR_API_KEY"

def get_weather(lat,lon):
    url = (
        "https://api.openweathermap.org/data/2.5/weather"
        f"?lat={lat}"
        f"&lon={lon}"
        f"&appid={api}"
        "&units=metric"
    )#making request for weather data
    response = requests.get(url)
    return response.json()
