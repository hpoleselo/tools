# Tools



## .bag to .csv Converter (``` convert.sh ```)

Copy the file to the folder you want to convert.

``` $ ./convert.sh YOURBAGFILE.bag THENAMEOFTHEOUTPUTFILE```

## .png to .jpg (``` convert.py ```)

Drag this file to the wished folder and just run it, it will do the conversion automatically.

## Automated login to Raspberry Pi (``` pipass.py ```)

Logins in to the RPi with aid of SSH, the script just opens the file which contains the password in form of text. It was pretty annoying at the time because i always forgot the IP and too tired for typing password in.

## Quaternion Tester (``` quaternionTester.py ```)

Useful for working with pose probe on RVIZ. Takes an actual pose (given inside the program) and changes rotation by given axis.

## Parameters passing ROS (``` cmd_line_rosparam ```)

Pass arguments from command line to rosparam and then extracting it in a Python script, example:

``` $ roslaunch cmd_line_rosparam pass_args.launch arg1:="henrique.gcode" ```


## CR Character error (``` crCharactersConvert.py ```)

When getting this error: ``` env: python\r: No such file or directory ``` using the shebang on the beginning of your Python code CAN (rarely) be caused because of CR characters, which are line breakers from Java (\r). I really don't know why this happenned, but this script when ran, replaces all ```\r``` for empty. (MAKE SURE TO MAKE A BACKUP OF YOUR CODE) 

**You have to edit the opened file to be your python script.**


