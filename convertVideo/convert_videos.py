import sys
import os


# Based on the code from Otávio Miranda: https://www.youtube.com/watch?v=wtlnvpVpAf4

# Objetivo: conversão para videos gravados em .mkv no Vokoscreen para serem editados no Adobe Premiere

# Comando de referência:
# ffmpeg -i filename.mkv -c:v libx264 -profile:v main -level:v 4.0 -c:a aac -strict -2 output.mp4

#TODO: join path

if sys.platform == "linux":
    ffmpeg_command = "ffmpeg"
else:
    ffmpeg_comando = r"ffmpeg\ffmpeg.exe"


codec_video = '-c:v libx264'
profile_video = '-profile:v main'
level_video = '-level:v 4.0'
codec_audio = '-c:a aac'
codec_audio_enable = '-strict -2'

# Split do nome do arquivo dps join com o mp4 output
output_video = 'teste.mp4'

# Get user id from linux

# Assumes you have vokoscreen folder, handle exception!
path = '/home/henrivis/Videos/vokoscreen'

# os.walk always return those 3 variables
# CHECAR VERSAO PYTHON E DEPENDENDO DA VERSAO USAR NAO USAR f'string
for dirpath, dirnames, filenames in os.walk(path):
    for archive in filenames:
        if archive.endswith('.mkv'):
            input_video = archive
            #talvez tenha que colocar como string
            command = f'{ffmpeg_command} -i  {input_video} {codec_video} {profile_video}' \
                f' {level_video} {codec_audio} {codec_audio_enable} {output_video} '
            os.system(command)