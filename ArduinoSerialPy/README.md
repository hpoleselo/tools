# ArPyPlot
Receives any analog reading (one dimensional) from the serial communication with baudrate of 9600 bps and plots
the data in real time using Matplotlib.

## Installation

Needed packages in order to the script to work:

``` $ sudo pip3.6 install serial ```

``` $ sudo pip3.6 install matplotlib ```

``` $ sudo pip3.6 install multiprocess ```

## Tested setup
I used the following setup:

![setup](https://user-images.githubusercontent.com/24254286/66364417-fb5f4300-e95f-11e9-9979-39f50a5b9c39.jpg)

Upload the code to your Arduino using Arduino IDE or command line

After uploading run the python program:

```$ python dataReceiver.py ```