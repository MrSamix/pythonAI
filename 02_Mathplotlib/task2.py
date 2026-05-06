import random
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams

rcParams['font.size'] = 10
rcParams['axes.labelsize'] = 11
rcParams['axes.titlesize'] = 12
rcParams['xtick.labelsize'] = 10
rcParams['ytick.labelsize'] = 10


age = [random.randint(0, 100) for _ in range(100)]

fig, ax = plt.subplots(figsize=(10, 6))
ax.hist(age, bins=10, edgecolor='black', alpha=0.7)
ax.set_xlabel('Age')
ax.set_ylabel('Frequency')

age_mean = np.mean(age)
ax.add_line(plt.axvline(age_mean, color='red', linestyle='dashed', linewidth=1, label=f'Mean: {age_mean:.2f}'))

ax.set_title('Distribution of Ages')
plt.show()