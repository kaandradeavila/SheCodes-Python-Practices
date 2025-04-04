temperatures = [10, 12, 14, 15]

# Print the list
print(temperatures)

# Modify an existing temperature
temperatures[3] = 9

# Print the modified item
print(temperatures[3])

# Add a temperature to the list
temperatures.append(17)

# Print the the newly added item
print(temperatures[4])

forecast = {
  "Monday": { "temperature": 21, "condition": "Rainy"},
  "Tuesday": { "temperature": 20, "condition": "Sunny"},
  "Wednesday": { "temperature": 23, "condition": "Cloudy"},
  "Thursday": { "temperature": 24, "condition": "Sunny"},
}

# Print the dictionary
print(forecast)

# Modify Wednesdays temperature to 25 and Sunny
forecast["Wednesday"][temperature] = 23

# Print Wednedays temperature

# Add forecast for Friday, 27, Cloudy

# Print Friday temperature such as "Friday's temperature will be 27 degrees and cloudy