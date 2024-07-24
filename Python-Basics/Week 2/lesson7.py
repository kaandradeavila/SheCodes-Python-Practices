""" 
1. Create a new Repl
2. Ask what the current temperature is
3. If the temperature is more than 20, output:
    > Enjoy a sunny day
4. If the temperature is less than 20, output:
    > Don't forget your jacket
"""
temperature = int(input("What temperature is outside right now? "))

if temperature > 20:
    print("Enjoy a sunny day")
else:
    print("Don't forget your jacket")