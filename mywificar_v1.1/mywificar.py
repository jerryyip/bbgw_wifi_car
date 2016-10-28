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
    motor.DCMotorMove(MotorLeft,ClockWise,PwmDutyLeft-10)
    motor.DCMotorMove(MotorRight,CounterClockWise,PwmDutyRight-10)
    

def turnLeft():
    motor.DCMotorMove(MotorLeft,CounterClockWise,PwmDutyLeft-7)
    motor.DCMotorMove(MotorRight,ClockWise,PwmDutyRight)

def turnRight():
    motor.DCMotorMove(MotorRight,ClockWise,PwmDutyRight-7)
    motor.DCMotorMove(MotorLeft,CounterClockWise,PwmDutyLeft)

def stop():
    motor.DCMotorStop(MotorLeft)    
    motor.DCMotorStop(MotorRight)

def spin():
    motor.DCMotorMove(MotorRight,ClockWise,PwmDutyRight-10)
    motor.DCMotorMove(MotorLeft,ClockWise,PwmDutyLeft-10)

def patrol():
    PwmDutyRight     = 17
    PwmDutyLeft      = 17
    while True:
#detectline() rr=4 rl=3 lr=2 ll=1 none=0
        a=detectLine()
        if a==5:
            #spin
            motor.DCMotorMove(MotorRight,ClockWise,PwmDutyRight-7)
            motor.DCMotorMove(MotorLeft,ClockWise,PwmDutyLeft-7)

        if a==4:
            #turnRight()
            motor.DCMotorMove(MotorRight,CounterClockWise,PwmDutyRight-5)
            motor.DCMotorMove(MotorLeft,CounterClockWise,PwmDutyLeft)
        if a==3:
            #turnRight()
            motor.DCMotorMove(MotorRight,ClockWise,PwmDutyRight-2)
            motor.DCMotorMove(MotorLeft,CounterClockWise,PwmDutyLeft)
        if a==2:
            #turnLeft()
            motor.DCMotorMove(MotorLeft,CounterClockWise,PwmDutyLeft-2)
            motor.DCMotorMove(MotorRight,ClockWise,PwmDutyRight)
        if a==1:
            #turnLeft()
            motor.DCMotorMove(MotorLeft,ClockWise,PwmDutyLeft-5)
            motor.DCMotorMove(MotorRight,ClockWise,PwmDutyRight)
        if a==0:
            motor.DCMotorMove(MotorRight,ClockWise,PwmDutyRight-3)
            motor.DCMotorMove(MotorLeft,CounterClockWise,PwmDutyLeft-3)

    

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
    while True:
        goFront()
        time.sleep(1)
        stop()
        #turnLeft()
        time.sleep(1)
    while False:
        stop()
        time.sleep(100)


