""" 
1. Define a class called User, which receives the first name and the year of birth
2. Create a method called "Welcome" which should display "Welcome Name, you were during the 20th century" or 21st is the user was born after 2000
3. Welcome 2 users to test this out
"""
class User:

    def __init__(self, name, year_of_birth):
        self.name = name
        self.year_of_birth = year_of_birth

    def welcome(self):
        if self.year_of_birth >= 2000:
            print(f"Welcome {self.name}, you were both in the 21st century")
        else:
            print(f"Welcome {self.name}, you were both in the 20th century")


nancy = User("Nancy", 1996)
nancy.welcome()

greicel = User("Greicel", 2001)
greicel.welcome()