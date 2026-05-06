import random
import matplotlib.pyplot as plt
from matplotlib import rcParams


rcParams['font.size'] = 10
rcParams['axes.labelsize'] = 11
rcParams['axes.titlesize'] = 12
rcParams['xtick.labelsize'] = 10
rcParams['ytick.labelsize'] = 10


group_1 = [random.randint(0, 100) for _ in range(15)]
group_2 = [random.randint(0, 100) for _ in range(15)]
group_3 = [random.randint(0, 100) for _ in range(15)]

fig, ax = plt.subplots(figsize=(10, 6))
ax.boxplot([group_1, group_2, group_3], labels=['Group 1', 'Group 2', 'Group 3'])
ax.set_xlabel('Groups')
ax.set_ylabel('Values')
ax.set_title('Comparison of Three Groups')
plt.show()