""" 
1. Display the current weather humidity in Tokyo, such as:    
    > It is currently 10ºC in Tokyo, Japan and the humidity level is 40%
"""
import requests
from rich import print

city = "Tokyo"
api_key = "424369doa037d0347bft3cfcc8cef956"
api_url = f"https://api.shecodes.io/weather/v1/current?query={city}&key={api_key}&units=metric"

response = requests.get(api_url)
response_json = response.json()

temperature = round(response_json["temperature"]["current"])
country = response_json["country"]
humidity = response_json["temperature"]["humidity"]

print(
    f"It is currently {temperature}ºC in {city}, {country} and the humidity level is {humidity}%"
)