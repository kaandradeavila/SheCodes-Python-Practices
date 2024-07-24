""" 
1. Create a new Repl
2. Ask for the user’s name
3. Ask what city the user is
4. Ask the user what temperature it is currently (in Celsius)
5. Display this sentence: Hi Matt, you are in Lisbon, and it is currently 12ºC or 30ºF).
6. Then display: I predict that tonight, the temperature will reach 2ºC or 12ºF).
7. Finally, display: Have a good day!
"""
name = input("What is your name? ")
city = input("What city do you live in? ")
temp_celsius = int(input("What is the temperature in Celsius? "))
temp_fahr = round((temp_celsius * 1.8) + 32)
temp_celsius_night = temp_celsius - 10
temp_fahr_night = round((temp_celsius_night * 1.8) + 32)

print(f"Hi {name}, you are in {city}, and it is currently {temp_celsius}ºC or {temp_fahr}ºF.")
print(f"I predict that tonight, the temperature will reach {temp_celsius_night}ºC or {temp_fahr_night}ºF.")
print(f"Have a good day!")
