import datetime as dt

import matplotlib.pyplot as plt
import numpy as np

# генеруємо 30 дат від сьогодні назад
n_days = 30
end_date = dt.date.today()
dates = [end_date - dt.timedelta(days=i) for i in range(n_days - 1, -1, -1)] # список дат від 30 днів назад до сьогодні
idx = np.arange(n_days)

rng = np.random.default_rng(42)

# 4 набори метрик продукту на одній і тій же часовій шкалі
conversion = 2.5 + 0.03 * idx + rng.normal(0, 0.15, size=n_days)  # %
retention = 45 + 3 * np.sin(idx / 4) + rng.normal(0, 1.2, size=n_days)  # %
avg_check = 1200 + 50 * np.cos(idx / 5) + rng.normal(0, 25, size=n_days)  # грн
orders = 80 + 8 * np.sin(idx / 3) + rng.normal(0, 4, size=n_days)  # шт

fig, axes = plt.subplots(2, 2, figsize=(12, 7), sharex=True)
fig.suptitle("Метрики продукту за часом", fontsize=14)

(ax1, ax2), (ax3, ax4) = axes

ax1.plot(dates, conversion, marker="o", linewidth=1.5)
ax1.set_title("Конверсiя")
ax1.set_ylabel("%")

ax2.plot(dates, retention, marker="o", linewidth=1.5)
ax2.set_title("Утримання")
ax2.set_ylabel("%")

ax3.plot(dates, avg_check, marker="o", linewidth=1.5)
ax3.set_title("Середнiй чек")
ax3.set_ylabel("грн")

ax4.plot(dates, orders, marker="o", linewidth=1.5)
ax4.set_title("Кiлькiсть замовлень")
ax4.set_ylabel("шт")

for ax in (ax1, ax2, ax3, ax4):
	ax.grid(True, alpha=0.3)
	ax.tick_params(axis="x", rotation=45)

fig.tight_layout(rect=(0, 0, 1, 0.95))
plt.show()