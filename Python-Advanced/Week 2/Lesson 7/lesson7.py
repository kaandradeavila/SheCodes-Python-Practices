import csv

with open("temperatures_7.csv", mode="r") as file:
    csv_reader = csv.reader(file)

    for row in csv_reader:
        print(f"It is {row[2].lower()} and {row[1]}ºC in {row[0]}")

file.close()
