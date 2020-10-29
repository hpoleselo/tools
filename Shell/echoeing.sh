# Using functions in bashrc
#cd ~ | sleep 2 | echo "runVirtualEnv() { export WORKON_HOME=/home/henrivis/.virtualenvs ; source /usr/local/bin/virtualenvwrapper.sh ; workon cv ; }" >> ~/.bashrc | echo "ros() { source /opt/ros/kinetic/setup.bash ; }" >> ~/.bashrc | echo "run_octoprint() { sudo chmod +666 /dev/ttyACM0 ; octoprint serve ; }" >> ~/.bashrc | echo "PATH=$PATH:~/catkin_ws/src/octoROS/src" >> ~/.bashrc | echo "reiniciar_placa_rede() { sudo service network-manager restart ; }" >> ~/.bashrc | echo "matlab() { cd /usr/local/MATLAB/R2017a/bin ; ./matlab ; }" >> ~/.bashrc | echo "surfbot() { cd ~/Documents/Codigos/SurfBot/ ; python3.5 telegramInterface.py ; }" >> ~/.bashrc | echo "ws() { source ~/catkin_ws/devel/setup.bash ; }" >> ~/.bashrc | echo "exportarIp() { export ROS_MASTER_URI='http://192.168.13.150:11311' ; }" >> ~/.bashrc | echo "ur5() { cd ~/InstalledPrograms/ursim-3.12.1.90940 ; ./start-ursim.sh ;}" >> ~/.bashrc  

# Using aliases (better because one can list the aliases!)
echo "alias runVirtualEnv ='export WORKON_HOME=/home/henrivis/.virtualenvs ; source /usr/local/bin/virtualenvwrapper.sh ; workon cv ;'" >> ~/.bashrc \
| echo "alias ros='source /opt/ros/melodic/setup.bash ;'" >> ~/.bashrc \
| echo "alias run_octoprint='sudo chmod +666 /dev/ttyACM0 ; octoprint serve ; '" >> ~/.bashrc \
| echo "PATH=$PATH:~/catkin_ws/src/octoROS/src" >> ~/.bashrc \
| echo "alias reiniciar_placa_rede='sudo service network-manager restart ;'" >> ~/.bashrc \
| echo "alias matlab='cd /usr/local/MATLAB/R2017a/bin ; ./matlab ;'" >> ~/.bashrc \
| echo "alias surfbot='cd ~/Documents/Codigos/SurfBot/ ; python3.6 telegramInterface.py ;'" >> ~/.bashrc \
| echo "alias ws='source ~/catkin_ws/devel/setup.bash ;'" >> ~/.bashrc \
| echo "alias ws2='source ~/lar_ws/devel/setup.bash ;'" >> ~/.bashrc \
| echo "alias exportarIp='export ROS_MASTER_URI='http://192.168.13.150:11311' ;'" >> ~/.bashrc \
| echo "alias ur5='cd ~/InstalledPrograms/ursim-3.9.0.64176 ; ./start-ursim.sh &'" >> ~/.bashrc \
| echo "alias webb='cd ~/Documents/Codigos/Webpage ; code . ;'" >> ~/.bashrc \
| echo "alias prog='cd ~/Documents/Codigos ; ls ;'" >> ~/.bashrc \
| echo "alias scp-example='echo Example: scp archive_to_be_sent.py  TARGET_USER@TARGET_IP:~/Desktop'" >> ~/.bashrc \
| echo "alias ex-ffmpeg='echo Example: ffmpeg -i filename.mkv -c:v libx264 -profile:v main -level:v 4.0 -c:a aac -strict -2 output.mp4 ;'" >> ~/.bashrc \
| echo "alias s3d='LD_PRELOAD=/opt/Simplify3D-3.1.1/Interface.so /opt/Simplify3D-3.1.1/Simplify3D &'" >> ~/.bashrc \
| echo "alias lar='cd ~/Documents/LaR ; ls ;'" >> ~/.bashrc \
| echo "alias vidconv='cd ~/Documents/Codigos/convertVideo/ ; python3.6 convert_videos.py ;'" >> ~/.bashrc \
| echo "alias pyenv='source ~/Documents/Codigos/py-env/bin/activate ;'" >> ~/.bashrc \
| echo "alias deslig='sudo shutdown -P +35'" >> ~/.bashrc \
| echo "alias rfcaster='python ~/Documents/Codigos/telegramForecaster/src/telegram-interface.py'" >> ~/.bashrc \
| echo "alias comprimir='echo 7z-Example: 7z a filename.7z -p pwd -mhe folder/files'" >> ~/.bashrc 


