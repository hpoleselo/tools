# Spotify
curl -sS https://download.spotify.com/debian/pubkey.gpg | sudo apt-key add - 
echo "deb http://repository.spotify.com stable non-free" | sudo tee /etc/apt/sources.list.d/spotify.list

# Jupyter Notebook
sudo -H pip3 install --upgrade pip
sudo -H pip3 install virtualenv
mkdir ~/py_venv
cd ~/py_venv
virtualenv py_venv_env
source py_venv_env/bin/activate
pip install jupyter

# Skype
sudo apt install apt-transport-https
curl https://repo.skype.com/data/SKYPE-GPG-KEY | sudo apt-key add -
echo "deb https://repo.skype.com/deb stable main" | sudo tee /etc/apt/sources.list.d/skypeforlinux.list
sudo apt update
sudo apt install skypeforlinux