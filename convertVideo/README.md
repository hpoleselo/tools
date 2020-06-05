## Convert Batch MKV Videos
Conversion from ``` .mkv ``` videos recorded on Vokoscreen so they can be edited in Adobe Premiere. Just implement some logic to use the following shell command: ``` ffmpeg -i filename.mkv -c:v libx264 -profile:v main -level:v 4.0 -c:a aac -strict -2 output.mp4 ```


### Installation and Usage

Install ffmpeg:
``` $ sudo apt-get install ffmpeg ```

Add an alias to your ``` .bashrc ``` to ease your life when converting the videos:
``` echo "alias vidconv='cd ~/Documents/Codigos/convertVideo/ ; python3.5 convert_videos.py ;'" >> ~/.bashrc ```

To convert the videos:
``` $ vidconv ```

Note that all videos located on ```~/Videos/vokoscreen ``` that have the extension ``` .mkv ``` will be converted to ``` .mp4 ```, if the folder ``` vokoscreen ``` doesn't exist the program will create it.

