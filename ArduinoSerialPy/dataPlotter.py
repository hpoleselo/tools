# This program plots two variables in real time
# by henrivis

import serial
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import glob
import sys
from matplotlib import style
import numpy as np
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-s", "--savelog", type=bool, required=True,
	help="Want to save the data? True or False")
ap.add_argument("-r", "--refreshrate", type=int, required=True,
	help="Every x milliseconds the data will be acquired")
args = vars(ap.parse_args())

# Identifying which port is being used (Works only on Linux)
port1 = "/dev/ttyACM0"
port2 = "/dev/ttyUSB0"

if (glob.glob(port1)==[port1]): 
	ser = serial.Serial(port1, 9600)
else: 
	ser = serial.Serial(port2, 9600)

print("Using port: %s") %ser.name

# Setup for plotting in Matplotlib
style.use('fivethirtyeight')

xs = []
ys = []
fig = plt.figure()
fig.suptitle('Sensor Acquisition', fontsize=18)

# Um plot 1x1 e o plot eh o numero 1
ax1 = fig.add_subplot(1,1,1)

dataFromSerial = 0

# Store what the user gave to us
saveLog = args["savelog"]
refreshRate = args["refreshrate"]


def readFromSerial():
    """ Reads the data from the opened serial port and separates the data into a list. """
    try:
        # Reads until it gets a carriage return. MAKE SURE THERE IS A CARRIAGE RETURN OR IT READS FOREVER
        data = ser.readline()
        # Splits string into a list at the tabs   
        separatedData = data.split()
        return separatedData
    except(KeyboardInterrupt):
        ser.close()


def plotData(i):
    """ Plot the retrieved data from Arduino via serial communication using matplotlib. """
    global xs, ys    
    data = readFromSerial()
    try:
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

        # Had to set the names here because in the initialization they would not be permanent 
        ax1.set_xlabel('Time (ms)')
        ax1.set_ylabel('Sensor')
        ax1.plot(xs,ys)
    except(ValueError):
        print("Retrieved the data in a wrong manner. Run it one more time")
        sys.exit(0)


def saveData():
    """ Store the retrieved data into a txt file to the local where the script is running. """  
    global xs,ys
    outputFile = "dataAcquisition.txt"

    # Combines lists together
    rows = zip(xs, ys)

    # Creates array from list
    row_arr = np.array(rows)
    np.savetxt(outputFile, row_arr)


def main():
    """ Calls the plotData function constantly """
    animt = animation.FuncAnimation(fig, plotData, interval=refreshRate)
    plt.show()
    if saveLog:
        saveData()
        fig.savefig('graphFromSensor.jpg')

if __name__ == "__main__":
    main()
