# Cloud Wallpaper Rotator (CWR) *Google Drive only right now, Scripts run on Linux w/ Gnome based DEs!*

CWR, downloads a single wallpaper from a designated Google Drive folder randomly and then through the use of scripts can set the Wallpaper on your desktop.

### Version
0.1

### Installation
To use this, you need the following:
  - Linux Distribution with Gnome based DE (edit the script files if you can for any other DE).
  - A client_secrets.json file (https://developers.google.com/drive/v2/web/auth/web-server).
  - PyDrive module.
  - Python 2.7.x

You need PyDrive installed for Python 2:
```sh
$ pip2 install PyDrive
```
Set up a google developer account, and acquire the client secrets file. Place this in the root of the folder with the .py script.

Change the "settings.json" file to your liking. History is a boolean for on and off, it will keep track of the last wallpaper that was used. OrderBy is the sorting order of the folder (doesn't really affect it, since it's randomly selected) more on it can be found [here](https://developers.google.com/drive/v2/reference/files/list#parameters). CacheAge is in days and it will update after that many days has passed since last cache update. The script only stores the new wallpaper id's from gdrive when the cache reaches this.
```json
{
	"folderId": "enter your GDrive folder ID here", 
	"history": 1, 
	"orderBy": "recency", 
	"cacheAge": 2
}
```

### Todos

 - Write more detailed README.
 - Improve code.
 - Add Code Comments.
 - UI?
 - Support for Windows/Other DEs.
