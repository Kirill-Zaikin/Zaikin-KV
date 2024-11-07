import numpy as np
import matplotlib.pyplot as plt



data = np.loadtxt("Desktop/Зайкин, Васенина, Булатов/data_file_calubr.txt", dtype = int)
fig, ax = plt.subplots(figsize = (12, 8), dpi=200)
#ax.axis([data.min(), int(len(data)/2), int(-1*(len(data)/2)), data.max()])
x = [i-450 for i in range(0, len(data))]
ax.plot(x, data)
Paskal = data.max() * 0.066
plt.ylim(0, data.max())
ax.set_title("Зависимость давления от расстояния")
ax.set_ylabel("Давление, условные единицы")
ax.set_xlabel("Расстояние, условные единицы")

ax.grid(which = 'major', color = 'gray')
ax.minorticks_on()
ax.grid(which = 'major', color = 'gray', linestyle = ":")

plt.show()