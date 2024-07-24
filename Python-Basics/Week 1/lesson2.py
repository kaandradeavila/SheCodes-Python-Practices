"""
Create a new Repl and print the city where you are, the current temperature in Celsius, and the current temperature in Fahrenheit.
Bonus: Calculate the temperature from Celsius to Fahrenheit using math.
"""
city = "Baltimore"
temperature_celsius = 21
temperature_fahrenheit = (temperature_celsius * 1.8) + 32

print("What city are you in? " + city)
print("What is the temperature in Celsius? " + str(temperature_celsius) + "ºC")
print("This is the temperature in Fahrenheit: " + str(round(temperature_fahrenheit)) + "ºF")