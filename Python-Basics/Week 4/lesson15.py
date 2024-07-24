# Create a dictionary of 3 countries you’d like to visit as a key and their capital city a value
countries = {"Japan": "Tokyo", "Ecuador": "Quito", "Germany": "Berlin"}

# Print out the dictionary
print(countries)

# Remove your least favorite country from the dictionary
del countries["Germany"]

# Print out the dictionary
print(countries)

# Add another country you'd like to visit
countries["Spain"] = "Madrid"

# Print out the dictionary
print(countries)

# Display the capital of each country (one at a time, don't use a loop)
print(f"The capital of Japan is {countries['Japan']}")
print(f"The capital of Ecuador is {countries['Ecuador']}")
print(f"The capital of Spain is {countries['Spain']}")