import mraa
import time
#GPIO_50=mraa60
s=mraa.Gpio(60)
s.dir(mraa.DIR_IN)


def isSwitchOn():
    return s.read()
    
    
    
if __name__ == "__main__":
    while True:
        time.sleep(1)
        print(isSwitchOn())
