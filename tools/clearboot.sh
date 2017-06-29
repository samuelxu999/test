#!/bin/bash

#First check your kernel version, so you won't delete the in-use kernel image,running
uname -r

#Now run this command for a list of installed kernels:
dpkg --list 'linux-image*'

#delete the kernels you don't want/need anymore by running this:
#sudo apt-get remove linux-image-VERSION

#When you're done removing the older kernels, you can run this to remove ever packages you won't need anymore:
sudo apt-get autoremove

#finally you can run this to update grub kernel list:
sudo update-grub
