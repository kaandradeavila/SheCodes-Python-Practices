""" 
1. Display each line of the CSV file as follows
    > “It is 24 in Lisbon.”
2. Use exception handling when it's not possible to read the data
"""
import csv

with open("cities_9.csv", mode="r") as file:
    cities_reader = csv.reader(file)

    for row in cities_reader:
        try:
            city = row[0]
            temperature = row[1]
            print(f"It is {temperature} in {city}.")
        except IndexError:
            print("Not city data found")
