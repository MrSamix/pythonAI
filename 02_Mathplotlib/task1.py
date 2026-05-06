import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams

rcParams['font.size'] = 10
rcParams['axes.labelsize'] = 11
rcParams['axes.titlesize'] = 12
rcParams['xtick.labelsize'] = 10
rcParams['ytick.labelsize'] = 10

MONTHS = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

PLAN = [120, 150, 180, 210, 240, 270, 300, 330, 360, 390, 420, 450]

FACT = [100, 130, 160, 190, 220, 250, 280, 330, 340, 370, 400, 430]

fig, ax = plt.subplots(figsize=(12,4))

x = np.arange(len(MONTHS))

ax.plot(x, PLAN, marker='o', linewidth=2, label='Plan')
ax.plot(x, FACT, marker='o', linewidth=2, label='Fact')

ax.set_title('Planned vs Actual Sales by Month')
ax.set_xlabel('Month')
ax.set_ylabel('Sales')

ax.set_xticks(x)
ax.set_xticklabels(MONTHS, rotation=45, ha='right')
ax.grid(True, linestyle='--', alpha=0.4)
ax.legend()

plt.tight_layout()
plt.show()