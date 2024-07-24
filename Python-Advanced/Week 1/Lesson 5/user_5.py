class User:

    def __init__(self, name):
        """Initializing user"""
        self.name = name

    def greet(self):
        """Greeting user"""
        print(f"Welcome - {self.name}")