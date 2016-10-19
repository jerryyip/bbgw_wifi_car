import MotorBridge
import time
import mraa
from mylinefinder import detectLine

MotorLeft        = 1
MotorRight       = 4
ClockWise        = 1
CounterClockWise = 2
PwmDutyRight     = 30
PwmDutyLeft      = 30
Frequency        = 700

x=mraa.Gpio(69)
x.dir(mraa.DIR_OUT)
motor = MotorBridge.MotorBridgeCape()
motor.DCMotorInit(MotorLeft,Frequency)
motor.DCMotorInit(MotorRight,Frequency)


def goFront():
    time.sleep(0.1)
    motor.DCMotorMove(MotorRight,ClockWise,PwmDutyRight)
    motor.DCMotorMove(MotorLeft,CounterClockWise,PwmDutyLeft)


def goBack():
    time.sleep(0.1)
    motor.DCMotorMove(MotorLeft,ClockWise,PwmDutyLeft)
    motor.DCMotorMove(MotorRight,CounterClockWise,PwmDutyRight)
    

def turnLeft():
    motor.DCMotorMove(MotorLeft,CounterClockWise,PwmDutyLeft)
    motor.DCMotorMove(MotorRight,ClockWise,PwmDutyRight-5)
    #motor.DCMotorStop(MotorLeft)
    
def turnRight():
    #motor.DCMotorStop(MotorRight)
    motor.DCMotorMove(MotorRight,ClockWise,PwmDutyRight)
    motor.DCMotorMove(MotorLeft,CounterClockWise,PwmDutyLeft-5)

def stop():
    motor.DCMotorStop(MotorLeft)    
    motor.DCMotorStop(MotorRight)

def spin():
    motor.DCMotorMove(MotorRight,ClockWise,PwmDutyRight-20)
    motor.DCMotorMove(MotorLeft,ClockWise,PwmDutyLeft-20)

def patrol():
    while True:
        a=detectLine()
        if a==3:
            goFront()
        if a==2:
            turnRight()
        if a==1:
            turnLeft()
        if a==0:
            spin()

    

if __name__ == '__main__':
    i=0
    while False:
        goFront()
        print(i)
        i=i+1
        time.sleep(2)
        goBack()
        print(i)
        i=i+1
        time.sleep(2)
        stop()
        print(i)
        i=i+1
        time.sleep(1)
    while False:
        goFront()
        time.sleep(2)
        turnLeft()
        time.sleep(1)
    while True:
        stop()
        time.sleep(100)


