import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

dac = [8, 11, 7, 1, 0, 5, 12, 6]
levels = 2 ** len(dac)
comp = 14
troyka = 13
maxVolt = 3.3

GPIO.setup(dac, GPIO.OUT)
GPIO.setup(comp, GPIO.IN)
GPIO.setup(troyka, GPIO.OUT, initial=GPIO.HIGH)

def tobin(N):

    return[int(i) for i in bin(N)[2:].zfill(8)]

def num2dac(value):

    signal = tobin(value)
    GPIO.output(dac, signal)

    return signal

try:

    while True:
           
        for value in range (0,256,1):

            signal = num2dac(value)
            voltage = value / levels * maxVolt
            time.sleep(0.001)
            compValue = GPIO.input(comp)

            if compValue == 1:

                print("Искомое число = {:^3} -> {}, входное напряжение = {:.2f}".format(value,signal,voltage))
                break

finally:

    GPIO.output(dac, 0)
    GPIO.cleanup()