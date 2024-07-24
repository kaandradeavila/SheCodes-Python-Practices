""" 
1. Print each line of the CSV file provided following this format:
    > It is currently 25 degrees in Paris, France
"""
import csv

filename = "weather_15.csv"

with (open(filename, 'r')) as csvfile:
    reader = csv.DictReader(csvfile)

    for line in reader:
        city = line["city"]
        country = line["country"]
        temperature = line["temperature"]
        print(f"It is currently {temperature} degrees in {city}, {country}")
