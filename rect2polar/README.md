By default Python 3.6  comes with Ubuntu, so this uses Python3 under the hood. Make sure to install numpy module before:

`$ pip3 install numpy`

Add this repo to the PATH so it can recognize the custom terminal command.

`$ PATH=$PATH:~/Documents/Codigos/rect2polar >> ~/.bashrc`

To run the program, just give the following command from any path:

`$ r2p 1 0`

Program should return:

```
Módulo: 1.0 
Ângulo: 0.0 graus.
```