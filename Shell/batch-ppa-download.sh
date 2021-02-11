# KDEnlive
echo "## Preping KDEnlive ##"
sudo add-apt-repository ppa:kdenlive/kdenlive-stable

# Spotify
echo "## Preping Spotify ##"
curl -sS https://download.spotify.com/debian/pubkey_0D811D58.gpg | sudo apt-key add - 
echo "deb http://repository.spotify.com stable non-free" | sudo tee /etc/apt/sources.list.d/spotify.list

# Typora
echo "## Preping Typora ##"
wget -qO - https://typora.io/linux/public-key.asc | sudo apt-key add -
sudo add-apt-repository 'deb https://typora.io/linux ./'

# Libreoffice
echo "## Preping Libreoffice ##"
sudo add-apt-repository ppa:libreoffice

# Update
echo "Updating"
sudo apt-get update

# Install everything
sudo apt-get install spotify-client typora libreoffice kdenlive