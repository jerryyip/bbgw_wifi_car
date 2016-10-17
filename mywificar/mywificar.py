import MotorBridge
import time
import mraa

MotorLeft        = 1
MotorRight       = 4
ClockWise        = 1
CounterClockWise = 2
PwmDutyRight     = 4
PwmDutyLeft      = 4
Frequency        = 500

x=mraa.Gpio(69)
x.dir(mraa.DIR_OUT)
motor = MotorBridge.MotorBridgeCape()
motor.DCMotorInit(MotorLeft,Frequency)
motor.DCMotorInit(MotorRight,Frequency)


def goFront():
    time.sleep(0.1)
    motor.DCMotorMove(MotorRight,ClockWise,PwmDutyRight)
    motor.DCMotorMove(MotorLeft,CounterClockWise,PwmDutyLeft)
    motor.DCMotorMove(MotorRight,ClockWise,PwmDutyRight)
    motor.DCMotorMove(MotorLeft,CounterClockWise,PwmDutyLeft)

def goBack():
    time.sleep(0.1)
    motor.DCMotorMove(MotorLeft,ClockWise,PwmDutyLeft)
    motor.DCMotorMove(MotorRight,CounterClockWise,PwmDutyRight)
    motor.DCMotorMove(MotorLeft,ClockWise,PwmDutyLeft)
    motor.DCMotorMove(MotorRight,CounterClockWise,PwmDutyRight)
    

def turnLeft():
    motor.DCMotorMove(MotorRight,ClockWise,PwmDutyRight-30)
    motor.DCMotorStop(MotorLeft)
    
def turnRight():
    motor.DCMotorMove(MotorLeft,CounterClockWise,PwmDutyLeft-30)
    motor.DCMotorStop(MotorRight)

def stop():
    motor.DCMotorStop(MotorLeft)    
    motor.DCMotorStop(MotorRight)
    motor.DCMotorStop(MotorLeft)    
    motor.DCMotorStop(MotorRight)

if __name__ == '__main__':
    i=0
    while True:
        try:
            goFront()
            print(i)
            i=i+1
            time.sleep(1)
            goBack()
            print(i)
            i=i+1
            time.sleep(1)
            stop()
            print(i)
            i=i+1
            time.sleep(1)
        except Exception as err:
            print err
 #   time.sleep(1) 
