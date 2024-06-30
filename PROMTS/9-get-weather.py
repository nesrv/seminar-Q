# get weather


def get_weather(city="Moscov"):
    """
    This function simulates getting the weather.
    """
    return "sunny"


import requests
import os

# Replace with your OpenWeatherMap API key
API_KEY = os.environ.get('OPENWEATHERMAP_API_KEY')

def get_weather(city):
    """
    Fetches the current weather data for a given city using the OpenWeatherMap API.
    """
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "appid=" + API_KEY + "&q=" + city
    response = requests.get(complete_url)
    data = response.json()

    if data["cod"] != "404":
        weather, temperature = data["main"]["temp"]
        return f"Weather in {city}: {weather}, Temperature: {temperature}°C"
    else:
        return "City not found."

# Example usage
city_name = "London"
weather_data = get_weather(city_name)
print(weather_data)
