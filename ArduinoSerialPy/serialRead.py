import serial

class MeasurementReader(object):
    def __init__(self):
        self.connected = False
        # Arduino is set always in linux to /dev/ttyUSB0, baudrate matches Arduino's
        self.ser = serial.Serial('/dev/ttyACM0', 9600)
        print("Using port: %s") %self.ser.name
        self.checkConnectivity()

    def checkConnectivity(self):
        try:
            while True:
                self.connected = True
                # Reads until it gets a carriage return. MAKE SURE THERE IS A CARRIAGE RETURN OR IT READS FOREVER
                data = self.ser.readline()
                # Splits string into a list at the tabs   
                separate = data.split()
                print(separate)
                        
        except:
            self.ser.close()

MeasurementReader()