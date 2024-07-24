""" 
1. Add 2 more cities with temperatures, and condition
2. Ensure the file is well formatted after you run your script
"""
with open("cities_8.csv", mode="a") as file:
    file.write("\nBaltimore,35,cloudy")
    file.write("\nQuito,11,rainy")

file.close()