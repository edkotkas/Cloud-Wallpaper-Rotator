#!/bin/bash

screen_width=1366 #<-- set here your screen's width dimension

#set "path/to/" to the correct path of this folder
python2 $HOME/path/to/cwr.py 1 0 
gsettings set org.gnome.desktop.background picture-uri file://$HOME/path/to/wallpaper.png
