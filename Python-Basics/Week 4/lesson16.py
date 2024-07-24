""" 
1. Create a new Repl
2. Create a dictionary with 3 countries and their capital cities you'd like to visit
3. Loop through each country and print out the following sentence:
    "Countries I'd like to visit"
    > 1: Canada (Capital city: Ottawa)
    > 2: France (Capital city: Paris)
    > 3: Germany (Capital city: Berlin)
"""
countries = {"Greece": "Athens", "Netherlands": "Amsterdam", "Italy": "Rome"}

count = 0
print("Countries I'd like to visit:")

for country, capital in countries.items():
    count += 1
    print(f"{count}: {country} (Capital city: {capital})")
    