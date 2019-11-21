# ArPyPlot
Receives any analog reading (one dimensional) from the serial communication with baudrate of 9600 bps and plots
the data in real time using Matplotlib.

![show](https://user-images.githubusercontent.com/24254286/69362534-7446ff80-0c6d-11ea-945a-8ebca799163c.gif)

## Installation

The program was mainly designed for Linux, an adaptation is welcome for Windows. The needed packages in order to the script to work:

``` $ pip3.6 install serial ```

``` $ pip3.6 install matplotlib ```

## Tested setup
I used the following setup:

![setup](https://user-images.githubusercontent.com/24254286/69362707-cdaf2e80-0c6d-11ea-9f6f-5ea44a958eea.jpg)

Upload the code to your Arduino using Arduino IDE or command line

After uploading run the Python program:

```$ python dataPlotter.py -s True -r 300 ```

Where the flags:
- s "True" means the values plotted will be saved on a txt file in the same directory as the python script
- r "300" means every 300ms the graph will be updated
