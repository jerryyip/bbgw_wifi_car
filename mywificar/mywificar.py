import MotorBridge
import time
import mraa

MotorLeft        = 1
MotorRight       = 4
ClockWise        = 1
CounterClockWise = 2
PwmDutyRight     = 20
PwmDutyLeft      = 20
Frequency        = 500

x=mraa.Gpio(69)
x.dir(mraa.DIR_OUT)
motor = MotorBridge.MotorBridgeCape()
motor.DCMotorInit(MotorLeft,Frequency)
motor.DCMotorInit(MotorRight,Frequency)


def goFront():
    motor.DCMotorMove(MotorRight,ClockWise,PwmDutyRight)
    motor.DCMotorMove(MotorLeft,CounterClockWise,PwmDutyLeft)

def goBack():
    motor.DCMotorMove(MotorLeft,ClockWise,PwmDutyLeft)
    motor.DCMotorMove(MotorRight,CounterClockWise,PwmDutyRight)

def turnLeft():
    motor.DCMotorMove(MotorRight,ClockWise,PwmDutyRight-30)
    motor.DCMotorStop(MotorLeft)
    
def turnRight():
    motor.DCMotorMove(MotorLeft,CounterClockWise,PwmDutyLeft-30)
    motor.DCMotorStop(MotorRight)

def stop():
#    x.write(0)

    motor.DCMotorStop(MotorLeft)    
    motor.DCMotorStop(MotorRight)
    time.sleep(0.1)
    motor.DCMotorStop(MotorLeft)    
    motor.DCMotorStop(MotorRight)

if __name__ == '__main__':
    goFront()
    time.sleep(2)
 #   goBack()
 #   time.sleep(2)
 #   stop()
 #   time.sleep(1) 
