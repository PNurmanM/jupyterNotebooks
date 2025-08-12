import serial
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import FuncAnimation

print("Check 1")

fig = plt.figure()
ax = fig.add_subplot(111)

#line, = axis.plot([], [], lw=2)

#plt.style.use('fivethirtyeight')
xl = []
yl = []
xx = 0.0
yy = 0.0
x = ''
y = ''
#plt.plot(x,y)
#plt.tight_layout()
#plt.show()

ser = serial.Serial(port='COM4', baudrate=115200)

print("Check 2")

ser.flush()

while True:
    try:
        input = ser.readline()
        val = str(input, 'UTF-8')
    #try:
    #    y, x = val.split()
    #except:
    #    pass

    #print(x + " " + y)
        print(val)
        ser.flush()
    except:
        pass

def animate(i, xl, yl, ser, xx, yy):
    input = ser.readline()
    val = str(input, 'UTF-8')

    try:
        y,x = val.split()
        if float(y) < float(100):
            xx = float(x)
            yy = float(y)
    except:
        pass

    xl.append(xx)
    yl.append(yy)
    print(yy)

    ax.set_ylim([0,100])
    ax.clear()
    ax.plot(yl)
    ax.set_title("Distance Sensor")
    ax.set_ylabel("centimeters")


#ani = animation.FuncAnimation(fig, animate, frames = 500, fargs=(xl, yl, ser, xx, yy), interval = 50)

#plt.tight_layout()

#plt.show()
ser.close()