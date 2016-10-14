import mraa

x=mraa.Gpio(69)
x.dir(mraa.DIR_OUT)
x.write(0)



