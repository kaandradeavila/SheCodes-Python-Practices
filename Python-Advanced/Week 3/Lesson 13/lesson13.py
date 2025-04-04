""" 
1. Display the data as a pie chart
2. Try to add a legend to make it more readable
"""
import matplotlib.pyplot as plt

condition = ['sunny', 'rainy', 'cloudy']
days = [300, 30, 35]

plt.pie(days, labels=condition)
plt.legend(days)
plt.title("Weather in Lisbon")

plt.show()