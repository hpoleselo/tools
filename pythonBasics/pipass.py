from subprocess import call
import re

try:
	with (open("beerpi.txt")) as filee:
		lines = filee.readlines()
		# Remove the \n in the txt file
		lines_wout_n = [s.replace('\n','') for s in lines]
		print lines_wout_n
		username = lines_wout_n[0]
		ip_address = lines_wout_n[1]
		pwd = lines_wout_n[2]
		command = "ssh" + " " + username + "@" + ip_address
		# In order to use the call function we have to pass the commands as strings from a list! Split makes that work for us.
		command = command.split()
		print command
		call(command, shell=False)

except(KeyboardInterrupt):
	print("Cancelling connection with BeerPi.")
