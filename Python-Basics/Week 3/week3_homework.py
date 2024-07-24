""" 
1. Create a new Repl
2. Ask for the name of the city
3. Ask the temperature in Celsius
4. Display the following message
    > It is currently 15ºC (59ªF) in London.
5. You should use at least 2 functions, one displaying the message and 1 calculating the Fahrenheit value.
"""
def convert_celsius_to_fahrenheit(celsius):
    """Converts Celsius to Fahrenheit."""
    return (celsius * 1.8) + 32


def display_temperature(city, celsius):
    """Displays the temperature in Celsius and Fahrenheit."""
    fahrenheit = round(convert_celsius_to_fahrenheit(celsius))
    return f"It is currently {celsius}ºC ({fahrenheit}ºF) in {city}."


def handle_data():
    """Asks the user for the city and temperature and returns a message."""
    city = input("Enter the name of the city: ")
    temperature = input(f"Enter the temperature in {city}: ")
    if city and temperature:
        temperature = float(temperature)
        temperature = round(temperature)
        message = display_temperature(city, temperature)
    else:
        message = "Please enter a valid city and temperature."
        return message
    return message


message_weather = handle_data()
print(message_weather)
