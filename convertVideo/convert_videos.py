#!/usr/bin/env python3

import sys
import os
from getpass import getuser
from pathlib import Path

""" 
@brief: Based on the code from Otávio Miranda: https://www.youtube.com/watch?v=wtlnvpVpAf4
@goal: conversion from .mkv videos recorded on Vokoscreen so they can be edited in Adobe Premiere
@command_reference: ffmpeg -i filename.mkv -c:v libx264 -profile:v main -level:v 4.0 -c:a aac -strict -2 output.mp4
"""

# TODO: move converted files to /converted folder
# TODO: CHECAR VERSAO PYTHON E DEPENDENDO DA VERSAO USAR NAO USAR f'string

if sys.platform == "linux":
    ffmpeg_command = "ffmpeg"
else:
    ffmpeg_comando = r"ffmpeg\ffmpeg.exe"

# ffmpeg settings
codec_video = '-c:v libx264'
profile_video = '-profile:v main'
level_video = '-level:v 4.0'
codec_audio = '-c:a aac'
codec_audio_enable = '-strict -2'
output_video_format = '.mp4'

# Get user id from linux
initial_path = '/home/' + getuser()

try:
    file_path = initial_path + '/Videos/vokoscree/'
    # Change working directory to be not where the program is executed, but in the file_path
    os.chdir(file_path)
except(OSError):
    print("No vokoscreen folder was found, creating a new one in /Videos...")
    new_path = initial_path + '/Videos/'
    os.chdir(new_path)
    new_folder = "pastona"
    os.system("mkdir " + new_folder)
    file_path = new_path + new_folder + "/"

try:
    # os.walk return those 3 variables
    for dirpath, dirnames, filenames in os.walk(file_path):
        # Only filenames are of our interest in this case
        for filename in filenames:
            if filename.endswith('.mkv'):
                # Supply whole path including filename in order to slice only the file name without extension
                path_with_file = file_path + filename

                # We slice it by using Path.stem() but the whole path has to be given
                filename_wout_extension = Path(path_with_file).stem

                # Update output_video_name so we don't overwrite other files
                output_video_name = filename_wout_extension + output_video_format
                command = f'{ffmpeg_command} -i  {filename} {codec_video} {profile_video}' \
                    f' {level_video} {codec_audio} {codec_audio_enable} {output_video_name} '
                os.system(command)

except(KeyboardInterrupt):
    print("Keyboard Interruption.")