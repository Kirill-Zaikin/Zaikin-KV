# МАТЕКЫ ПОСТРОЕНИЯ ГРАФИКОВ

import numpy as np #бибилотека массивов
import matplotlib.pyplot as plt  #бибилотека графиков

#создание массивов данных
dat_array = np.loadtxt("data.txt", dtype = int)
set_array = np.loadtxt("settings.txt", dtype = float)

#преобразование напряжения и времени
N = int(dat_array.size)
volt_array = np.zeros(N)
time_array = np.zeros(N)

for i in range (0, N, 1):
    volt_array[i] = dat_array[i] * set_array[1]
    time_array[i] = i * set_array[0]

for i in range (0, N, 1):
    if volt_array[i] > minimum:
        

#print("Напряжение:",volt_array)
#print("Время:",time_array)

#создание графика
fig, ax = plt.subplots(figsize=(20, 14), dpi=800)
ax.plot(time_array, volt_array, color='green')
plt.xlabel('$Напряжение,В$') #Подпись для оси х
plt.ylabel('$Время,сек$') #Подпись для оси y
plt.title('Зарядка-разрядка конденсатора') #Название
fig.savefig("data.png")
plt.show()
