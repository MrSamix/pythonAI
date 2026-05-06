import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams

rcParams['font.size'] = 10
rcParams['axes.labelsize'] = 11
rcParams['axes.titlesize'] = 12
rcParams['xtick.labelsize'] = 10
rcParams['ytick.labelsize'] = 10

DAYS = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

TEMP = [27, 28, 30, 28, 20, 18, 18]

HUMIDITY = [23, 24, 18, 29, 49, 56, 37]

fig, ax = plt.subplots(figsize=(12,4))

x = np.arange(len(DAYS))

ax.plot(x, TEMP, marker='o', linewidth=2, label='Temperature')
ax.plot(x, HUMIDITY, marker='o', linewidth=2, label='Humidity')

ax.set_title('Temperature and Humidity by Day of the Week')
ax.set_xlabel('Days')
ax.set_ylabel('Values')

ax.set_xticks(x)
ax.set_xticklabels(DAYS, rotation=45, ha='right')
ax.grid(True, linestyle='--', alpha=0.4)
ax.legend()

plt.tight_layout()
plt.show()