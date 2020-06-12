#ffmpeg -i rodrigo.ogg output.mp3
import os
import sys

ffmpeg_command = "ffmpeg -i "

# Will receive from Telgram (download from bot folder)
audio = "rodrigo.ogg"
output = ""

command = ffmpeg_command + audio + output
os.system(command)