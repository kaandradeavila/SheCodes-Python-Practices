""" 
1. Display 2 subplots next to each other
2. The first one should display the temperature deviation using a linear plot.
3. The second one should display the CO2 deviation using a bar chart
4. Save the result inside an image
5. Make the plots look nice and readable
"""
import matplotlib.pyplot as plt

years = [2000, 2005, 2010, 2015, 2020]
temp_anomalies = [0.8, 0.9, 1.0, 1.2, 1.3]  # °C deviation from a baseline
co2_emissions = [25, 30, 35, 40, 45]  # in billions of metric tons

fig, (ax1, ax2) = plt.subplots(2, 1)

ax1.plot(years, temp_anomalies, marker='o', color = '#42b883')
ax1.set_title("Global Temperature Anomalies")
ax1.set_xlabel("Year")
ax1.set_ylabel("Temperature Anomaly (in °C)")
ax1.grid(True)
ax1.set_xticks(years)
ax1.set_yticks([0.8, 1.0, 1.2])

ax2.bar(years, co2_emissions, color = '#ff7e67')
ax2.set_title("Global CO2 Emissions")
ax2.set_xlabel("Year")
ax2.set_ylabel("CO2 Emissions (billions of metric tons)")
ax2.grid(True)

plt.tight_layout()
plt.savefig("output_w3.png")
plt.show()