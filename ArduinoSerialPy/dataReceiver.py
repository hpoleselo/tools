import serial
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import numpy as np


class MeasurementPlotter(object):
    def __init__(self):
        self.connected = False
        # Arduino is set always in linux to /dev/ttyUSB0, baudrate matches Arduino's
        self.ser = serial.Serial('/dev/ttyUSB0', 9600)
        print("Using port: %s") %self.ser.name

        # Setup for plotting in Matplotlib
        style.use('fivethirtyeight')
        self.xs = []
        self.ys = []


    def readFromSerial(self):
        try:
            while True:
                self.connected = True

                # This will parse through length and read the serial values
                for i in range(len(values)):
                    # Reads until it gets a carriage return. MAKE SURE THERE IS A CARRIAGE RETURN OR IT READS FOREVER
                    data = self.ser.readline()
                    # Splits string into a list at the tabs   
                    separate = data.split()
                    print(separate)
                
                    values.append(int(separate[0]))   #add new value as int to current list
        except:
            self.ser.close()


    def plotData(self,i):
        #TODO: Ver como ler a informacao da serial
        # Para esse caso o dado vem dessa forma: ['0,2', '1,4', '2,6', '3,8', '4,10', '5,12', '6,14', '7,16', '8,18', '9,20', '10,3', '11,-5', '12,-10']
        graph_data = open('example.txt' , 'r').read()
        lines = graph_data.split('\n')

        for line in lines:
            # Trim the empty lines
            if len(line)>1:
                # Assuming we're reading a file that contains commas
                x, y = line.split(',')
                # The data must me plotted as float not as a string!
                self.xs.append(float(x))
                self.ys.append(float(y))
        # Clean everything before we plot
        ax1.clear()
        ax1.plot(xs,ys)

    def saveData(self):
        # Combines lists together
        rows = zip(values, t)

        # Creates array from list
        row_arr = np.array(rows)

        # Saves data in file (load w/np.loadtxt())
        np.savetxt("C:\\Users\\mel\\Documents\\Instructables\\test_radio2.txt", row_arr)

    def main(self):
        self.readFromSerial()
        #animt = animation.FuncAnimation(fig, self.plotData, interval=500)
        #plt.show()



MeasurementPlotter()
