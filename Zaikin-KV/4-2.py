import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
dac = [8, 11, 7, 1, 0, 5, 12, 6]
GPIO.setup(dac, GPIO.OUT)

def tobin(N):

    return[int(i) for i in bin(N)[2:].zfill(8)]
print("Пожалуйста,введите длительность сигнала (сек)")

a = input()
T = int(a) / (512*8)
volt = 0

try:
    n=0
    while n<1:

        for i in range (0, 256):

            for j in range (len(dac)):

                GPIO.output(dac[j], int(tobin(i)[j])) 
                time.sleep(T)
            volt = 0+i*(3.3/256)
            print("Уровень сигнала =",volt,"В" ) 

        for i in range (254, 0, -1):

            for j in range (len(dac)):
                GPIO.output(dac[j], int(tobin(i)[j]))
                time.sleep(T) 
            volt = (3.3-(3.3/256))-(255-i)*(3.3/256)
            print("Уровень сигнала =",volt, "В" ) 
        n=1   
        
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()