import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
dac = [8, 11, 7, 1, 0, 5, 12, 6]
GPIO.setup(dac, GPIO.OUT)

def tobin(N):

    return[int(i) for i in bin(N)[2:].zfill(8)]

try:

    try:
        while True:

            print("Желаете закончить программу? q-да;w-нет")
            Prev = str(input())

            if Prev != "q":

                print("Пожалуйста,введите любое число от 0 до 255:")
                N = int(input())

                if N > 0 and N <256:

                    for i in range (len(dac)):

                        GPIO.output(dac[i], (tobin(N)[i]))
                    print(3.3/256*N)

                elif N ==0:

                    GPIO.output(dac, 0)
        
        

            
                else:
            
                    print("Похоже вы ввели неправильное число, немедленно исправтесь!")
            else:

                print("Вы вышли из программы,хорошего дня!")
                break
    
    except ValueError:

        print("Вы ввели не число,очень плохо!") 

   
finally:

    GPIO.output(dac, 0)
    GPIO.cleanup()