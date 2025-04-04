# Change the styling to your liking

import matplotlib.pyplot as plt

lisbon_temperatures = [25, 26, 28, 24, 22]
new_york_temperatures = [15, 17, 12, 20, 22]
sydney_temperatures = [10, 12, 11, 8, 7]

days = ['Monday', 'Tuesday', 'Wednesday', "Thursday", 'Friday']

plt.style.use('seaborn-v0_8')

plt.plot(days,
         lisbon_temperatures,
         label="Lisbon",
         color='b',
         marker='o',
         linestyle='-.',
         linewidth=2)
plt.plot(days, new_york_temperatures, label="New York", color='r', marker='.')
plt.plot(days,
         sydney_temperatures,
         label="Sydney",
         color='g',
         linestyle='--',
         linewidth=2)

plt.grid(True)
plt.legend()

plt.xlabel("Days")
plt.ylabel("Temperatures (in celcius)")

plt.title("Weather forecast")

plt.show()
