from user_5 import User


class FrenchUser(User):

    def greet(self):
        """Redefining greet method"""
        print(f"Bonjour - {self.name}")
        