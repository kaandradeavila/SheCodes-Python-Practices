# Exercise 1
weather = {
    "city": "Lisbon",
    "country": "Portugal",
    "temperature": 17.94,
    "humidity": 77
}

# Display the weather in Lisbon such as:
# It is 18ºC (64ºF) in Lisbon, Portugal, the humidity level is 77%.
def convert_to_fahr(cels):
    return (cels * 1.8) + 32


celsius = round(weather['temperature'])
fahrenheit = round(convert_to_fahr(celsius))
city = weather['city']
country = weather['country']
humidity = weather['humidity']

print(
    f"It is {celsius}ºC ({fahrenheit}ºF) in {city}, {country}, the humidity level is {humidity}%."
)

# Exercise 2
forecast = {
    "city": "Lisbon",
    "country": "Portugal",
    "daily": [17.76, 13.08, 12.14, 11.25, 14.29]
}

# Display the forecast in Lisbon such as:
# The forecast for Lisbon, Portugal for the next 5 days is:
# Day 1: 18ºC
# Day 2: 13ºC
# Day 3: 12ºC
# Day 4: 11ºC
# Day 5: 14ºC

forecast_city = forecast['city']
forecast_country = forecast['country']
forecast_temperature = None

print(
    f"The forecast for {forecast_city}, {forecast_country} for the next 5 days is:"
)

count = 0
daily = forecast['daily']
for temperature in daily:
    count += 1
    print(f"Day {count}: {round(temperature)}ºC")
