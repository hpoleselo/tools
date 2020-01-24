# Tools



## Telegram Bot Tide Checker ([``` /SurfBot ```](https://github.com/hpoleselo/tools/tree/master/SurfBot))

Telegram bot that sends a message to a channel in Telegram from a python web-scrapped page about tides levels from Vilas do Atlântico.

## Simple Webpage Scraping with Python ([``` surfForecast.py ```](https://github.com/hpoleselo/tools/blob/master/surfForecast.py))

Gets the tides levels from the website by scraping it with ``` requests ``` and ``` BeautifulSoup ```.

## .bag to .csv Converter ([``` convert.sh ```](https://github.com/hpoleselo/tools/blob/master/convert.sh))

Copy the file to the folder you want to convert.

``` $ ./convert.sh YOURBAGFILE.bag THENAMEOFTHEOUTPUTFILE```

## Automated login to Raspberry Pi ([``` pipass.py ```](https://github.com/hpoleselo/tools/blob/master/pipass.py))

Logins in to the RPi with aid of SSH, the script just opens the file which contains the password in form of text. It was pretty annoying at the time because i always forgot the IP and too tired for typing password in.

## Simple Telegram Bot ([``` helloTelegram.py ```](https://github.com/hpoleselo/tools/blob/master/helloTelegram.py))

Simple Telegram bot to get the feeling of using Telegram's API.

## Quaternion Tester ([``` quaternionTester.py ```](https://github.com/hpoleselo/tools/blob/master/quaternionTester.py))

Useful for working with pose probe on RVIZ. Takes an actual pose (given inside the program) and changes rotation by given axis.

## Parameters passing ROS ([``` /cmd_line_rosparam ```](https://github.com/hpoleselo/tools/tree/master/cmd_line_rosparam))

Pass arguments from command line to rosparam and then extracting it in a Python script, example:

``` $ roslaunch cmd_line_rosparam pass_args.launch arg1:="henrique.gcode" ```

## CR Character error ([``` crCharactersConvert.py ```](https://github.com/hpoleselo/tools/blob/master/crCharactersConvert.py))

When getting this error: ``` env: python\r: No such file or directory ``` using the shebang on the beginning of your Python code CAN (rarely) be caused because of CR characters, which are line breakers from Java (\r). I really don't know why this happenned, but this script when ran, replaces all ```\r``` for empty. (MAKE SURE TO MAKE A BACKUP OF YOUR CODE) 

**You have to edit the opened file to be your python script.**

## Extension Searcher ([``` search_extension.py ```](https://github.com/hpoleselo/tools/blob/master/search_extension.py))

Place this program to the directory you want to check for Python files. It just checks all the files in the directory which has the .py extension. The goal is to use that to the automated printing process, which will take a parameter from the user and check if that parameter (file to be printed, gcode), exists. 

## .png to .jpg ([``` convert.py ```](https://github.com/hpoleselo/tools/blob/master/convert.py))

Drag this file to the wished folder and just run it, it will do the conversion automatically.

## Simple Thread Program ([``` thread_example.py ```](https://github.com/hpoleselo/tools/blob/master/convert.py))

Simple reminder of how to initialize a thread in Python

## Arduino Python Plotter ([``` /ArduinoSerialPy ```](https://github.com/hpoleselo/tools/tree/master/ArduinoSerialPy))

Plots two vectors in real time using Python and Arduino. Check inside the folder for the Readme better instructions

## Kazam mp4 Video Converter ([``` /convertVideo ```](https://github.com/hpoleselo/tools/tree/master/convertVideo))

When screencording with Kazam although the output video is in ``` .mp4 ```, sending in to WhatsApp directly or editing in Sony Vegas/Adobe Premiere is not possible, with this small program everything's solved:

``` $ ./convertmp4.sh THENAMEOFYOURVIDEO.mp4 ```