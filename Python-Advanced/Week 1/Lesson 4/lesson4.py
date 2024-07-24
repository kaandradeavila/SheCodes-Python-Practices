""" 
1. Move the class user into its own file
2. Import to make sure it works.
"""
from user_4 import User

nancy = User("Nancy", 1998)
print(nancy.welcome())

luiza = User("Luiza", 2005)
print(luiza.welcome())
