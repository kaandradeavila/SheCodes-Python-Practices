class Weather:

    def __init__(self, city):
        self.city = city

    def set_weather(self, temperature, condition):
        self.temperature = temperature
        self.condition = condition

    def display_weather(self):
        print(f"City: {self.city}")
        print(f"Temperature: {self.temperature}")
        print(f"Condition: {self.condition}")