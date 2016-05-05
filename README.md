# Cloud Wallpaper Rotator (CWR)
### Google Drive Only (for now)!

CWR, downloads a single wallpaper from a designated Google Drive folder randomly and then through the use of scripts can set the Wallpaper on your desktop.

### Version
0.1

### Installation
To use this w/ Google Drive, you need the following:
  - A client_secrets.json file (https://developers.google.com/drive/v2/web/auth/web-server).
  - PyDrive module.
  - Python 2.7.x

Install PyDrive for Python 2:
```sh
$ pip2 install PyDrive
```
Set up a google developer account, and acquire the client secrets file. Place this in the root of the folder with the .py script and name it "client_secrets.json".

Change the "settings.json" file to your liking. History is a boolean for on and off, it will keep track of the last wallpaper that was used. OrderBy is the sorting order of the folder (doesn't really affect it, since it's randomly selected) more on it can be found [here](https://developers.google.com/drive/v2/reference/files/list#parameters). CacheAge is in days and it will update after that many days has passed since last cache update. The script only stores the new wallpaper id's from gdrive when the cache reaches this.
```json
{
	"folderId": "enter your GDrive folder ID here",
	"history": 1,
	"orderBy": "recency",
	"cacheAge": 2
}
```

### Scripts
Sample script to enable use on Gnome-based Desktop Environments. Make it executable and run it after the startup of the DE.
```sh
#!/bin/bash

#
# cwr.py bool bool
# First bool argument (get next/last background):
#    1 - Retrieve next random background.
#    0 - Retrieve last background, if any.
# Second bool argument (update wallpaper list):
#    1 - Force cache update.
#    0 - Skip cache update, wait for cacheAge for the update..

screen_width=1366 # your current screen resolution's width
interval="900" # frequency of wallpaper changes (in seconds)

# change "set/path/to" to corresponding paths of the respective files
while true; do
	python2 set/path/to/cwr.py 1 0
	gsettings set org.gnome.desktop.background picture-uri file://set/path/to/wallpaper.png
	echo "Sleeping $interval seconds till the next change..."
	sleep $interval
done

```

### Todos

 - Write more detailed README.
 - Improve code.
 - Add Code Comments.
 - UI?
 - Support for other Cloud Storage Services.
