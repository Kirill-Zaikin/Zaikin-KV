import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

leds = [9, 10, 22, 27, 17, 4, 3, 2]
dac = [8, 11, 7, 1, 0, 5, 12, 6]
comp = 14
troyka = 13
maxVolt = 3.3
Volt = 0

GPIO.setup(dac, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(comp, GPIO.IN)
GPIO.setup(troyka, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(leds, GPIO.OUT, initial = GPIO.LOW)

def tobin(N):

    return[int(i) for i in bin(N)[2:].zfill(8)]

def num2dac(value):

    signal = tobin(value)
    GPIO.output(dac, signal)

    return signal

def adc():

    Volt=0

    for step in range (8):
        buff = 2**(7-step)
        GPIO.output(dac,num2dac(Volt+buff))
        time.sleep(0.005)
        compValue = GPIO.input(comp)
        GPIO.output(dac,num2dac(Volt+buff))
        GPIO.output(leds,tobin(Volt)) 

        if compValue == 0:

            Volt += buff 

    return(Volt,3.3/256*Volt) 
try:

    while True :

        print(adc())

finally:

    GPIO.output(dac, 0)
    GPIO.cleanup()