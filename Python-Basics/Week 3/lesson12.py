""" 
1. Fork this Repl
2. Create a function that returns the Fahrenheit value of a Celsius temperature.
3. Display the following and use the function to calculate the Fahrenheit value:
    > It is currently 15ºC (59ªF) in London.
"""

def convert_celsius_to_fahrenheit(celsius):
    """Converts Celsius to Fahrenheit."""
    return (celsius * 1.8) + 32


def display_temperature(city, celsius):
    """Displays the temperature in Celsius and Fahrenheit."""
    fahrenheit = round(convert_celsius_to_fahrenheit(celsius))
    return f"It is currently {celsius}ºC ({fahrenheit}ºF) in {city}."


message = display_temperature("London", 15)
print(message)