""" 
1. Create a new Repl
2. Create a function that has 3 parameters (a city temperature and humidity level) and display the following message:
    > The temperature in London is 7 degrees with a humidity of 40%
3. If the humidity isn't provided, display the following message:
    > The temperature in New York is 10 degrees
4. Call this function twice. one time with humidity and one time without
"""
def display_weather_data(city, temperature, humidity=""):
    """Displays the weather data for a given city."""
    if humidity:
        humidity = int(humidity)
        output = f"The temperature in {city} is {temperature} degrees with a humidity of {humidity}%."
    else:
        output = f"The temperature in {city} is {temperature} degrees."

    print(output)


display_weather_data("London", 5, "40")
display_weather_data("New York", 5)