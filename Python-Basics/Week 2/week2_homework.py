""" 
1. Create a new Repl
2. Ask for a city name
3. Ask the user what temperature it is currently (in Celsius)
4. If the temperature is greater than 20ºC, display this sentence:     
    > It is currently warm in Lisbon with a temperature of 20ºC
5. If the temperature is greater than 10ºC, display this sentence:
    > It is currently chilly in Lisbon with a temperature of 15ºC 
6. If the temperature is less than 10ºC, display this sentence:
    > It is currently cold in Lisbon with a temperature of 5ºC
7. If the user didn't enter a city and temperature
    > Please try again and enter a city and temperature
"""
city = input("Enter the name of a city: ")
temperature = input(f"Enter the temperature in {city}: ")

if not (city) or not (temperature):
    print("Please try again and enter a city and temperature")
    exit()

temperature = int(temperature)

if temperature > 20:
    print(f"It is currently warm in {city} with a temperature of {temperature}ºC")
elif temperature > 10:
    print(f"It is currently chilly in {city} with a temperature of {temperature}ºC")
elif temperature < 10:
    print(f"It is currently cold in {city} with a temperature of {temperature}ºC")