#!/bin/bash

screen_width=1366 #<-- set here your screen's width dimension
interval="900" #<-- set here the seconds you want to sleep till the next update

#set "path/to/" to the correct path of this folder
while true; do
   python2 $HOME/path/to/cwr.py 1 0
   gsettings set org.gnome.desktop.background picture-uri file://$HOME/path/to/wallpaper.png
   echo "Sleeping $interval seconds till the next update..."
   sleep $interval
done
