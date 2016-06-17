# Cloud Wallpaper Rotator (CWR)

## Google Drive Only (for now)!

CWR, downloads a single wallpaper from a designated Google Drive folder randomly and sets the wallpaper on your machine.

## Version

1.1

## Installation

To use this w/ Google Drive, you need the following:

- A client_secrets.json file (<https://developers.google.com/drive/v2/web/auth/web-server>).
- PyDrive module.
- Python 2.7.x

Install PyDrive for Python 2:

```sh
$ pip2 install PyDrive
```

Set up a google developer account, and acquire the client secrets file. Place this in the root of the folder with the cwr.py script and name it "client_secrets.json".

Change the "config.json" located in the manager folder to fit your needs. [{orderBy}](https://developers.google.com/drive/v2/reference/files/list#parameters)

```text
{
    "folderId": "place your folder ID here, where the wallpapers are located at",
    "history": 1 (boolean 1 or 0, to keep history or not),
    "orderBy": "recency" (follow link above for more options),
    "rotationFrequency": "15m" (d/h/m/s for day/hour/minute/second),
    "cachePeriod": 2 (this is in days only)
}
```

## TODO

- Write more detailed README.
- Improve code.
- Add Code Comments.
- UI?
- Support for other Cloud Storage Services.
