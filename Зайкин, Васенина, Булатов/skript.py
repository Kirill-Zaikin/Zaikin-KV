import jetFunctions as Func
import time

Func.initSpiAdc()
Func.initStepMotorGpio()

dl=5.516e-3
steps=int(4/dl)
print(steps)
list=[]
k=0
st=10

for i in range(0,steps,st):
    list.append(str(Func.getAdc())+' '+str(steps/2-i))
    time.sleep(0.5)
    Func.stepBackward(st)
    k += 1

for i in range(0,steps,st):
    Func.stepForward(st)
    k += 1


Func.deinitSpiAdc()
Func.deinitStepMotorGpio()

lists = [str(i) for i in list]
with open ('test_measure', 'w') as outf:
    outf.write("\n".join(lists))