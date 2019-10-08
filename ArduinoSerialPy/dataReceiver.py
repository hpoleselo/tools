import serial
import matplotlib.pyplot as plt
import numpy as np


class MeasurementPlotter(object):
    def __init__(self):
        self.connected = False
        # Arduino is set always in linux to /dev/ttyUSB0, baudrate matches Arduino's
        self.ser = serial.Serial('/dev/ttyUSB0', 9600)
        print("Using port: %s") %self.ser.name
        self.checkConnectivity()

    def checkConnectivity(self):
        try:
            while True:
                self.connected = True
                plt.ion()                    #sets plot to animation mode

                # How many points we want to retrieve from the readings
                self.length = 500

                # Creating the variable before we store the values to be read
                values = [0]*self.length

                #xline = plt.plot(t)
                yline, = plt.plot(values)
                plt.ylim(400,700)   # Sets the y axis limits

                # This will parse through length and read the serial values
                for i in range(len(values)):
                    print("Entrou no for")
                    # Reads until it gets a carriage return. MAKE SURE THERE IS A CARRIAGE RETURN OR IT READS FOREVER
                    data = self.ser.readline()
                    # Splits string into a list at the tabs   
                    separate = data.split()
                    print(separate)
                
                    values.append(int(separate[0]))   #add new value as int to current list
                
                    del values[0]
                
                    #xline.set_xdata(np.arange(len(x))) #sets xdata to new list length
                    yline.set_ydata(np.arange(len(values)))
                
                    plt.pause(1000)                   #in seconds
                    plt.draw()                         #draws new plot
                        
        except:
            self.ser.close()


    # ADD THIS LATER
    def saveData(self):
        # Combines lists together
        rows = zip(values, t)

        # Creates array from list
        row_arr = np.array(rows)

        # Saves data in file (load w/np.loadtxt())
        np.savetxt("C:\\Users\\mel\\Documents\\Instructables\\test_radio2.txt", row_arr)

MeasurementPlotter()
