# импорт библиотек
import RPi.GPIO as GPIO
import time
import matplotlib.pyplot as plt

# настройка работы пинов 
GPIO.setmode(GPIO.BCM)

leds = [9, 10, 22, 27, 17, 4, 3, 2]
dac = [8, 11, 7, 1, 0, 5, 12, 6]
comp = 14
troyka = 13
maxVolt = 3.3
minVolt = 0
data_exp = []
start_time = 0
stop_time = 0

GPIO.setup(leds, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(dac, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(comp, GPIO.IN)
GPIO.setup(troyka, GPIO.OUT, initial=GPIO.LOW)

# описание функции перевода в двоичный код
def tobin(N):

    return[int(i) for i in bin(N)[2:].zfill(8)]

# описание функции вывода информации ЦАП
def num2dac(value):

    signal = tobin(value)
    GPIO.output(dac, signal)

    return signal

# описание функции преобразования информации с тройки
def adc():

    Volt=0

    for step in range (8):

        buff = 2**(7-step)
        GPIO.output(dac,num2dac(Volt+buff))
        time.sleep(0.005)
        compValue = GPIO.input(comp)
        GPIO.output(leds,tobin(Volt))  

        if compValue == 0:

            Volt += buff 
    troyka_volt = 3.3/256*Volt
    return(troyka_volt )

# начало исполнительной программы
try:
        # подача питания на конденсатор и фиксация времени начала эксперемента
        GPIO.output(troyka,1)
        start_time = time.time()

        # блок заряда конденсатора
        while adc() < 3:

            print("ВНИМАНИЕ!!! ИДЁТ ЗАРЯДКА КОНДЕНСАТОРА!")
            print("Текущее значение заряда = ",adc(),"В")
            data_exp.append(int(adc()))

        # отключение питания конденсатора
        GPIO.output(troyka,0)
            
        # блок разряда конденсатора
        while adc() > 0.27:

            print("ВНИМАНИЕ!!! ИДЁТ РАЗРЯДКА КОНДЕНСАТОРА!")
            print("Текущее значение заряда = ",adc(),"В")
            data_exp.append(int(adc()))

        # фиксация времени конца эксперемента
        stop_time = time.time()

        # перевод значений напряжения в строку для записи в файл
        data_exp_str = [str(item) for item in data_exp]
        data_f_str = str(len(data_exp_str)/(stop_time - start_time))
        data_t_str = str((stop_time - start_time)/len(data_exp_str))
        # запись данный во внешний файл
        with open('data_file','w') as outfile:
            outfile.write("\n".join(data_exp_str))
            outfile.write("\n")
            outfile.write("шаг квантования:")
            outfile.write(data_t_str)
            outfile.write("\n")
            outfile.write("часота дискретизации:")
            outfile.write(data_f_str)

        # вывод общего времени эксперемента
        print("время эксперемента = ",stop_time - start_time,"сек")

        # вывод графика данных
        plt.plot(data_exp)
        plt.show()

# наведение порядка
finally:

    GPIO.output(dac, 0)
    GPIO.output(leds, 0)
    GPIO.cleanup()