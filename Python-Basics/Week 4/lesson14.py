""" 
1. Create a new Repl
2. Create a list of 3 countries you'd like to visit.
3. Loop through each country and print out the following sentence with the correct country and the correct number
    > My number 1 country is Canada
    > My number 2 country is Brazil
    > My number 3 country is Japan
"""
countries = ["Japan", "Italy", "Norway"]

for country in countries:
    print(f"My number {countries.index(country) + 1} country is {country}")
