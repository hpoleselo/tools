#!/bin/bash
if [[ "$1" = *.mp4* ]]
then
    ffmpeg -y -i $1 -c:v libx264 -c:a aac -strict experimental -tune fastdecode -pix_fmt yuv420p -b:a 192k -ar 48000 output_file.mp4
else
    echo "[INFO]: Please provide a file with .mp4 extension as argument of the shell script."
fi
