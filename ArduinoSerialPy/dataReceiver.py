import serial
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import numpy as np
# To send data to our matplotlib graph while hearing the infinite loop function readSerial
from multiprocessing import Queue
import threading

# Arduino is set always in linux to /dev/ttyUSB0, baudrate matches Arduino's
#ser = serial.Serial('/dev/ttyUSB0', 9600)
ser = serial.Serial('/dev/ttyACM0', 9600)
print("Using port: %s") %ser.name

# Setup for plotting in Matplotlib
style.use('fivethirtyeight')
xs = []
ys = []
fig = plt.figure()
# Um plot 1x1 e o plot eh o numero 1
ax1 = fig.add_subplot(1,1,1)

dataFromSerial = 0

def readFromSerial():
    try:
        # Reads until it gets a carriage return. MAKE SURE THERE IS A CARRIAGE RETURN OR IT READS FOREVER
        data = ser.readline()
        # Splits string into a list at the tabs   
        separatedData = data.split()
        return separatedData
    except(KeyboardInterrupt):
        ser.close()

def plotData(i):
    global xs, ys    
    data = readFromSerial()
    #if len(data) > 1:
    # Extract the element from the list
    strToSplit = data[0]
    # Separate the time and sensor data
    x, y = strToSplit.split(',')
    # The data must me plotted as float not as a string!
    xs.append(float(x))
    ys.append(float(y))
    # Clean everything before we plot
    ax1.clear()
    ax1.plot(xs,ys)

def saveData():
    global xs,ys
    # Combines lists together
    rows = zip(xs, ys)

    # Creates array from list
    row_arr = np.array(rows)

    # Saves data in file (load w/np.loadtxt())
    np.savetxt(".", row_arr)

def main():
    animt = animation.FuncAnimation(fig, plotData, interval=500)
    plt.show()

if __name__ == "__main__":
    main()
