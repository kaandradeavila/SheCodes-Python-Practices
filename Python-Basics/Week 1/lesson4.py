""" 
1. Create a new replit
2. Ask the user what temperature it is in Celsius
3. Display the temperature in Fahrenheit
"""
temperature = input("What is your current temperature in Celsius? ")
temp_fah = (int(temperature) * 1.8) + 32

print(f"Currently, it is {temperature}ºC or {round(temp_fah)}ºF outside.")