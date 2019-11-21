## Installation

``` $ sudo apt-get install ros-kinetic-multimaster-fkie ```

## Network Configuration

Be sure you're connected to a network and you have your IP set as static.
Some routers allow you to set your own IP when connecting to the network.

After connected to the network that you have your IP static:

``` $ ifconfig ```

``` $ export ROS_MASTER_URI='http://YOURIPADDRESS:11311' ```

To make this change permanent go to your bashrc and add the command:

``` cd ~/ ```

``` $ echo export ROS_MASTER_URI='http://YOURIPADDRESS:11311' >> .bashrc ```

Add the computers you want to see on multimaster (i don't think this is really needed)

``` $ sudo nano /etc/hosts ```

When inside the file, add to the end of the file: (the ip adresses from other pcs and the user)

``` 193.175.12.43 hpoleselo ```

## Enable Multicast

If this command returns 0 then the multicast is enabled on your PC:

``` $ cat /proc/sys/net/ipv4/icmp_echo_ignore_broadcasts ```

To permanently enable the multicast feature, go to the /etc/sysctl.conf and add to the end of the file

``` net.ipv4.icmp_echo_ignore_broadcasts=0 ```

``` $ sudo service procps restart ```

To test if the multicast is indeed available:

``` $ ping 224.0.0.1 ```

You could run this command from any computer and it would return all the computers on the common network


## Usage

To run multimaster:

``` $ rosrun master_sync_fkie master_sync ```

``` $ rosrun master_discovery_fkie master_discovery _mcast_gruop:=224.0.0.1 ```

``` $ rosservice call /master_discovery/list_masters ```

