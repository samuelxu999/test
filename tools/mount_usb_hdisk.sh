#!/bin/bash

#First check your external usb hard driver
sudo fdisk -l

EXTERNAL_PATH="/media/external"

# The new dir to mount driver
if [ ! -d $EXTERNAL_PATH ]; then
	echo "Create Directory $EXTERNAL_PATH."
	sudo mkdir /media/external	
else
	echo "Directory $EXTERNAL_PATH exists."
fi

# Unmount driver to avoid duplicate mount
echo "unmount $EXTERNAL_PATH."
sudo umount -l /dev/sdg1

# The mount hard driver to your folder
echo "mount $EXTERNAL_PATH to external driver."
sudo mount -t ntfs-3g /dev/sdg1 /media/external
