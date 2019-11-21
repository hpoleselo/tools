# ArPyPlot
Receives any analog reading (one dimensional) from the serial communication with baudrate of 9600 bps and plots
the data in real time using Matplotlib.

![show](https://user-images.githubusercontent.com/24254286/69299825-52f3fe00-0bf0-11ea-92d8-9befbe3138c1.gif)

## Installation

Needed packages in order to the script to work:

``` $ pip3.6 install serial ```

``` $ pip3.6 install matplotlib ```

## Tested setup
I used the following setup:

![setup](https://user-images.githubusercontent.com/24254286/66364417-fb5f4300-e95f-11e9-9979-39f50a5b9c39.jpg)

Upload the code to your Arduino using Arduino IDE or command line

After uploading run the python program:

```$ python dataPlotter.py -s True -r 300 ```

Where the flags:
- s "True" means the values plotted will be saved on a txt file in the same directory as the python script
- r "300" means every 300ms the graph will be updated
