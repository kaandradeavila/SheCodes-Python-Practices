""" 
1. Create a function asking for the city where you are and the current temperature and display this message:
    > You are in Lisbon and it is currently 17ºC.
2. Call this function twice.
3. Bonus point: Display an error message if the user doesn't enter a city or a temperature
"""
def say_hello_world():
    name = input("What is your name? ")
    if name:
        print(f"Hello {name.capitalize()}!")
    else:
        print("Too bad you don't have a name")


say_hello_world()
say_hello_world()