import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams
import random

rcParams['font.size'] = 10
rcParams['axes.labelsize'] = 11
rcParams['axes.titlesize'] = 12
rcParams['xtick.labelsize'] = 10
rcParams['ytick.labelsize'] = 10

HOURS = np.arange(24)

load = [random.randint(10, 99) for _ in range(24)]


fig, ax = plt.subplots(figsize=(12,4))

x = np.arange(len(HOURS))

ax.plot(x, load, marker='o', linewidth=2, label='Load')
# зафарбувати область під графіком
ax.fill_between(x, load, color='skyblue', alpha=0.3)

ax.set_title('Load server by hour')
ax.set_xlabel('Hour')
ax.set_ylabel('Load')

ax.set_xticks(x)
ax.set_xticklabels(HOURS, rotation=45, ha='right')
ax.grid(True, linestyle='--', alpha=0.4)
ax.legend()

plt.tight_layout()
plt.show()