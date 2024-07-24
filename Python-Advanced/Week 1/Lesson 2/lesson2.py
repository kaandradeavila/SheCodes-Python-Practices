""" 
1. Define a class User who receives 2 attributes in the initializer, a first name, and a last name.
2. Create a method called full_name, which returns the user's full name
3. Create 2 users with 2 different names and print their full name
4. Change the first name of the first object and print the full name again
"""
class User:

    def __init__(self, first_name, last_name):
        """Initialiaze the user"""
        self.first_name = first_name
        self.last_name = last_name

    def display_full_name(self):
        """Display full name of the user"""
        print(f"{self.first_name} {self.last_name}")


leo = User("Leo", "Rodriguez")
kyre = User("Kyrenia", "Andrade")

leo.display_full_name()
kyre.display_full_name()

leo.first_name = "Leonardo"
leo.display_full_name()
