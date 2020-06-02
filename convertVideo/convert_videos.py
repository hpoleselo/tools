import sys


# Based on the code from Otávio Miranda
# https://www.youtube.com/watch?v=wtlnvpVpAf4

# Objetivo: conversão para videos gravados em .mkv no Vokoscreen para serem editados no Adobe Premiere

# Comando de referência:
# ffmpeg -i filename.mkv -c:v libx264 -profile:v main -level:v 4.0 -c:a aac -strict -2 output.mp4



if sys.platform == "linux":
    command = "ffmpeg"
else:
    comando = r"ffmpeg\ffmpeg.exe"


codec_video = '-c:v libx264'


os.system(command)