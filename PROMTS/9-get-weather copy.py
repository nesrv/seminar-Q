import os
import requests

def get_weather_data(city, api_key):
    """
    Fetches weather data for a given city from OpenWeatherMap.org API.
    
    Args:
        city (str): The name of the city for which to fetch weather data.
        api_key (str): The API key for OpenWeatherMap.org API.
        
    Returns:
        dict: A dictionary containing the weather data for the specified city.
    """
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}appid={api_key}&q={city}"
    
    response = requests.get(complete_url)
    response.raise_for_status()  # Raise an exception for non-2xx status codes
    
    weather_data = response.json()
    
    if weather_data["cod"] != 200:
        error_message = weather_data["message"]
        raise ValueError(f"Error fetching weather data: {error_message}")
    
    return weather_data

# Example usage
api_key = os.environ.get("OPENWEATHERMAP_API_KEY")
if not api_key:
    raise ValueError("OPENWEATHERMAP_API_KEY environment variable not set")

city = "London"
weather = get_weather_data(city, 'f9f9c8c9c1f6f7c6f8b6d8b6f9b6f9b6')
print(f"Weather in {city}: {weather['weather'][0]['description']}")
print(f"Temperature: {weather['main']['temp']} K")
