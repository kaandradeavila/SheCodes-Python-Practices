""" 
1. Create a new Repl
2. Create a function that has 2 parameters (a city and a temperature) and display the following message
    > The temperature in London is currently 7 degrees
3. Call this function twice with different arguments
4. Bonus point: Include the docstring inside the function
"""
def display_city_temperature(city, temperature):
    """Displays the temperature of a city. It receives 2 parameters: city and temperature."""
    output = f"The temperature in {city} is currently {temperature} degrees."
    print(output)


display_city_temperature("London", 7)
display_city_temperature("New York", 12)