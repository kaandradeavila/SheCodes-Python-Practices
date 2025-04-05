temperatures = [
  {'city': "Paris", 'continent': "Europe", "temperature": "12"},
  {'city': "Los Angeles", 'continent': "North America", "temperature": "22"},
  {'city': "Tokyo", 'continent': "Asia", "temperature": "18"},
  {'city': "New York", 'continent': "North America", "temperature": "14"},
  {'city': "Sao Paulo", 'continent': "South America", "temperature": "25"},
  {'city': "Toronto", 'continent': "North America", "temperature": "2"}
]

# Given the list of temperatures, calculate and print the average temperature of north American cities

north_american_cities_count = 0
total_temperature = 0

for temperature in temperatures:
    if temperature['continent'] == "North America":
        total_temperature += float(temperature['temperature'])
        north_american_cities_count += 1

average_temp = round(total_temperature / north_american_cities_count, 2)

print(f"Average temperature in North America is {average_temp} degrees.")