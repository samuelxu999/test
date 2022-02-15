#!/bin/bash

## readin parameters
OPERATION=$1
Hdisk_name=$2
Media_folder=$3

## set local mount folder path
DISK_PATH=/dev/$Hdisk_name
MOUNT_PATH=/media/$Media_folder

## check hdisk information
if  [ "check" == "$OPERATION" ] ; then
	echo "List all connected disk!"
	sudo fdisk -l
# mount hdisk to local folder		
elif [ "add" == "$OPERATION" ] ; then
	## parameter validation
	if [ -z $Hdisk_name ]; then
		echo "Error: hard disk path is not input."
		exit 0
	fi

	if [ -z $Media_folder ]; then
		echo "Error: media folder path is not input."
		exit 0
	fi

	# Verify if Media_folder is existed. 
	if [ ! -d $MOUNT_PATH ]; then
		echo "Create Directory $MOUNT_PATH."
		sudo mkdir $MOUNT_PATH
	else
		echo "Directory $MOUNT_PATH exists."
	fi

	## mount hard driver to your local file system
	echo "Mount $DISK_PATH to $MOUNT_PATH"
	sudo mount -t ntfs-3g $DISK_PATH $MOUNT_PATH

	## show mount status:
	echo "Mount status:"
	df | grep $DISK_PATH	
elif [ "remove" == "$OPERATION" ] ; then
	## parameter validation
	if [ -z $Hdisk_name ]; then
		echo "Error: hard disk path is not input."
		exit 0
	fi

	## unmount hard driver from your local file system
	echo "Unmount $DISK_PATH"
	sudo umount -l $DISK_PATH

	## show mount status:
	echo "Mount status:"
	df | grep $DISK_PATH	
else
	echo "Usage $0 check|add|remove| -disk_name -local_media_folder!"
fi