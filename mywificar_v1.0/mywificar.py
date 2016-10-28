import MotorBridge
import time
import mraa

MotorLeft        = 1
MotorRight       = 4
ClockWise        = 1
CounterClockWise = 2
PwmDutyRight     = 30
PwmDutyLeft      = 30
Frequency        = 700

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


