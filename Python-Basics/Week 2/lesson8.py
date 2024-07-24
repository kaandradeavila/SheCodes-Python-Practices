""" 
1. Create a new Repl,
2. Ask what the current temperature is and if it's rainy
3. If the temperature is more than 20 and it's not raining, output:
    > Enjoy a sunny day
4. If the temperature is more than 20 and it's raining, output:
    > Don't forget your umbrella
5. If the temperature is less than 20 and it's not raining, output:
    > Don't forget your jacket
6. If the temperature is less than 20 and it's raining output
    > Don't forget your umbrella and your jacket
"""
temperature = input("What's the temperature outside? ")
temperature = int(temperature)

if temperature > 30: 
  print("It's warm")
elif temperature >= 20:
  print("It's nice")
elif temperature >= 10:
  print("It's chilly")
else:
  print("It's cold")