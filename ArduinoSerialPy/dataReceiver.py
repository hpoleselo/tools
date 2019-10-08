import serial
import matplotlib.pyplot as plt
import numpy as np


class MeasurementPlotter(object):
    def __init__(self):
        self.connected = False
        # Arduino is set always in linux to /dev/ttyUSB0
        self.ser = serial.Serial('/dev/ttyUSB0', 9600) #sets up serial connection (make sure baud rate is correct - matches Arduino)
        print("Using port: %s") %self.ser.name
        self.checkConnectivity()

    def checkConnectivity(self):
        try:
            while True:
                x = self.ser.readline()          # read one byte
                print(x)
                self.connected = True
                #self.graphSetup()
        except:
            self.ser.close()

    def graphSetup(self):
        plt.ion()                    #sets plot to animation mode

        # How many points we want to retrieve from the readings
        self.length = 500

        # Creating the variable before we store the values to be read
        values = [0]*self.length

        #xline = plt.plot(t)
        yline, = plt.plot(values)
        plt.ylim(400,700)   # Sets the y axis limits

        # This will parse through length and read the serial values
        for i in range(values):
            data = self.ser.readline()    # Reads until it gets a carriage return. MAKE SURE THERE IS A CARRIAGE RETURN OR IT READS FOREVER
            separate = data.split()      # Splits string into a list at the tabs
            #print separate
        
            values.append(int(separate[0]))   #add new value as int to current list
        
            del values[0]
        
            #xline.set_xdata(np.arange(len(x))) #sets xdata to new list length
            yline.set_ydata(np.arange(len(values)))
        
            plt.pause(0.001)                   #in seconds
            plt.draw()                         #draws new plot
        # Closes serial connection (very important to do this! if you have an error partway through the code, type this into the cmd line to close the connection)  
        #self.ser.close()


MeasurementPlotter()

def saveData(self):
    rows = zip(values, t)                  #combines lists together

    row_arr = np.array(rows)               #creates array from list
    np.savetxt("C:\\Users\\mel\\Documents\\Instructables\\test_radio2.txt", row_arr) #save data in file (load w/np.loadtxt())
