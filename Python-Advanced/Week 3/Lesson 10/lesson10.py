""" 
1. Display 3 plot with the temperature forecast for Lisbon, New York and Sydney for the next 5 days (use random data)
2. Add legend and label
"""

import matplotlib.pyplot as plt

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
lisbon_temperatures = [12, 16, 13, 13, 19]
new_york_temperatures = [30, 28, 28, 26, 34]
sydney_temperatures = [23, 25, 19, 19, 20]

plt.plot(days, lisbon_temperatures)
plt.plot(days, new_york_temperatures)
plt.plot(days, sydney_temperatures)

plt.title("Temperature Forecast")
plt.xlabel("Days in Advance")
plt.ylabel("Temperature in Cº")

plt.legend(["Lisbon", "New York", "Sydney"])

plt.show()
