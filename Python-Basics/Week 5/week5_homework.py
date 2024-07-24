""" 
1. Ask for a city name
2. Display the current weather for this specific city such as:
    > It is currently 23ºC in Parrs, France
"""
import requests
from rich import print


def ask_city():
    city = input("Enter a city name: ")

    if city:
        return city
    else:
        print("You didn't enter a city name.")
        ask_city()


def handle_api_request():
    city = ask_city()
    api_key = "424369doa037d0347bft3cfcc8cef956"
    api_url = f"https://api.shecodes.io/weather/v1/current?query={city}&key={api_key}&units=metric"

    response = requests.get(api_url)
    return response.json()


def display_weather():
    weather_data = handle_api_request()
    temperature = round(weather_data["temperature"]["current"])
    city = weather_data["city"]
    country = weather_data["country"]
    print(f"It is currently {temperature}ºC in {city}, {country}")


display_weather()
