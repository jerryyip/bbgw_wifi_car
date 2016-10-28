import mraa
import time

#rr gpio14 mraa70
#rl gpio15 mraa72
#ll gpio31 mraa57
#lr gpio30 mraa59

lr = mraa.Gpio(59)
ll = mraa.Gpio(57)
rr = mraa.Gpio(70)
rl = mraa.Gpio(72)

ll.dir(mraa.DIR_IN)
lr.dir(mraa.DIR_IN)
rr.dir(mraa.DIR_IN)
rl.dir(mraa.DIR_IN)

#Output 1 when detect line
def detectLine():
    _ll=ll.read()
    _lr=lr.read()
    _rl=rl.read()
    _rr=rr.read()
    if _ll and _lr and _rl and _rr:
        return 5
    if _lr and _rl:
        return 0
    if _ll==1:
        return 1
    if _lr==1:
        return 2
    if _rl==1:
        return 3
    if _rr==1:
        return 4
    else:
        return 0
        
if __name__ == "__main__":
    while True:
        detectLine()
        time.sleep(.1)
