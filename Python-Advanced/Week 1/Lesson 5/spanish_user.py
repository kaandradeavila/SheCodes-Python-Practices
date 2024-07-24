from user_5 import User

class SpanishUser(User):

    def greet(self):
        """Redefining greet method"""
        print(f"Hola! - {self.name}")