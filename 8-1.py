#МАКЕТ ГРАФИКА
import numpy as np #библиотека массивов
import matplotlib.pyplot as plt #библиотека графиков
from textwrap import wrap #бибилиотека текстредактора

#файла на чтение
with open("data.txt","r") as f:
    data_array=np.array(f.read().split(), dtype=int) # Чтение данных из файлов data.txt

with open("settings.txt","r") as f:
    data_settings=np.array(f.read().split(), dtype=float) # Чтение данных из файлов settings.txt

data_time=np.linspace(0,data_settings[0]*1000,data_array.size) # Перевод номеров отсчётов в секунды

data_array=data_array*data_settings[1] # Перевод показаний АЦП в Вольты

#создание графика
fig,ax = plt.subplots(figsize=(16,12),dpi=100)

ax.grid(which='major',color='gray') # Главная сетка

ax.minorticks_on()
ax.grid(which='minor',color='gray',linestyle=':') # Дополнительная сетка

ax.scatter(data_time[0:data_time.size:15],data_array[0:data_array.size:15],marker='o',c='red',s=100) # Настройка маркеров

ax.plot(data_time,data_array,label="Зависимость напряжения от времени",color='blue',linewidth=1.5) # Пострение линии графика

ax.legend(fontsize=14) # Создание легенды

plt.xlim(data_time.min(), data_time.max() + 0.2) # Настройка максимума и минимума оси X
plt.ylim(data_array.min(), data_array.max() + 0.1) # Настройка максимума и минимума оси Y

ax.set_title("/n".join(wrap('Процесс зарядки и разрядки конденсатора в RC цепи',60))) # Название графика
ax.set_ylabel("напряжение,В") # Название оси Y
ax.set_xlabel("время,с") # Название оси X

# Вывод текста в области графика
plt.text( data_time.max() / 2 + 3.33, data_array.max()/ 2 + 0.25, 'Время заряда: 6,432 сек.' , size='large', color='black') 
plt.text(data_time.max() / 2 + 3.33, data_array.max()/ 2 + 0.35, 'Время разряда: 5.568 cек.' , size='large', color='black')

plt.show() # Отображение графика
fig.savefig('graph.svg') # Сохранение графика в файл в формате .svg
fig.savefig('graph.png') # Сохранение графика в файл в формате .png
