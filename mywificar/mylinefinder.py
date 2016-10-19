import mraa
import time

#gpio_30-mraa57 gpio_31-mraa_59

left = mraa.Gpio(57)
right = mraa.Gpio(59)

left.dir(mraa.DIR_IN)
right.dir(mraa.DIR_IN)

def detectLine():
    r=1-right.read()
    l=1-left.read()
    if (l and r):
        return 3    #no line, gofront
    if l:
        return 2    #line on right, turn right
    if r:
        return 1    #line on left, turn left
    else:
        return 0    #line on both, spin

if __name__ == "__main__":
    
    print(detectLine())
    time.sleep(1)