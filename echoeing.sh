# Using functions in bashrc
#cd ~ | sleep 2 | echo "runVirtualEnv() { export WORKON_HOME=/home/henrivis/.virtualenvs ; source /usr/local/bin/virtualenvwrapper.sh ; workon cv ; }" >> .bashrc | echo "ros() { source /opt/ros/kinetic/setup.bash ; }" >> .bashrc | echo "run_octoprint() { sudo chmod +666 /dev/ttyACM0 ; octoprint serve ; }" >> .bashrc | echo "PATH=$PATH:~/catkin_ws/src/octoROS/src" >> .bashrc | echo "reiniciar_placa_rede() { sudo service network-manager restart ; }" >> .bashrc | echo "matlab() { cd /usr/local/MATLAB/R2017a/bin ; ./matlab ; }" >> .bashrc | echo "surfbot() { cd ~/Documents/Codigos/SurfBot/ ; python3.5 telegramInterface.py ; }" >> .bashrc | echo "ws() { source ~/catkin_ws/devel/setup.bash ; }" >> .bashrc | echo "exportarIp() { export ROS_MASTER_URI='http://192.168.13.150:11311' ; }" >> .bashrc | echo "ur5() { cd ~/InstalledPrograms/ursim-3.12.1.90940 ; ./start-ursim.sh ;}" >> .bashrc  

# Using aliases (better because one can list the aliases!)
cd ~ | sleep 2 | echo "alias runVirtualEnv ='export WORKON_HOME=/home/henrivis/.virtualenvs ; source /usr/local/bin/virtualenvwrapper.sh ; workon cv ;'" >> .bashrc \
| echo "alias ros='source /opt/ros/kinetic/setup.bash ;'" >> .bashrc \
| echo "alias run_octoprint='sudo chmod +666 /dev/ttyACM0 ; octoprint serve ; '" >> .bashrc \
| echo "alias ros='source /opt/ros/kinetic/setup.bash ;'" >> .bashrc \
| echo "PATH=$PATH:~/catkin_ws/src/octoROS/src" >> .bashrc \
| echo "alias reiniciar_placa_rede='sudo service network-manager restart ;'" >> .bashrc \
| echo "alias matlab='cd /usr/local/MATLAB/R2017a/bin ; ./matlab ;'" >> .bashrc \
| echo "alias surfbot='cd ~/Documents/Codigos/SurfBot/ ; python3.5 telegramInterface.py ;'" >> .bashrc \
| echo "alias ws='source ~/catkin_ws/devel/setup.bash ;'" >> .bashrc \
| echo "alias exportarIp='export ROS_MASTER_URI='http://192.168.13.150:11311' ;'" >> .bashrc \
| echo "alias ur5='cd ~/InstalledPrograms/ursim-3.9.0.64176 ; ./start-ursim.sh ;'" >> .bashrc