from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os
import json
import random
import platform

# custom management imports
import manager.history as History
import manager.cache as Cache
import manager.settings as Settings


class Background(object):

    def __init__(self):
        self.realpath = "/".join(
            str(os.path.realpath(__file__)).split("/")[:-1]
        ) + "/"

        self.output = self.realpath + "wallpaper.png"

        with open(self.realpath + "settings.json", "r") as settings:
            self.settings = json.load(settings)

        self.cache = Cache(self.realpath + ".cache")

        self.history = History(self.settings)
        if self.history.status() is True:
            self.history.setHistoryFile(".history")

        self.folderId = str(self.settings["folderId"])
        self.orderBy = str(self.settings["orderBy"])
        self.cacheAge = ((int(self.settings["cacheAge"]) * 24) * 60) * 60

        self.credentials = self.realpath + ".credentials"

        self.gauth = GoogleAuth()
        self.gauth.LoadCredentialsFile(self.credentials)

        if self.gauth.credentials is None:
            self.gauth.LocalWebserverAuth()
        elif self.gauth.access_token_expired:
            self.gauth.Refresh()
        else:
            self.gauth.Authorize()
        self.gauth.SaveCredentialsFile(self.credentials)

        self.drive = GoogleDrive(self.gauth)

        # writing back to settings file
        # with open(self.realpath+"/settings.json", "w+") as settings:
        # 	self.settings = json.dump(self.settings, settings)

    def cacheFileList(self, force=False):
        if self.cache.cache_age >= self.cacheAge or force is True:
            self.drive_files = self.drive.ListFile({
                'orderBy': self.orderBy,
                'q': "'" +
                self.folderId +
                "' in parents and trashed=false"
            }).GetList()
            print("Caching wallpaper list...")
            self.cache.preserve([files['id'] for files in self.drive_files])

    def retrieveFile(self, imageId):
        print("Downloading wallpaper...")
        self.drive.CreateFile({'id': imageId}).GetContentFile(self.output)

    def nextWallpaper(self):
        print("Retrieving next wallpaper...")
        self.wallpaper = random.choice(self.cache.retrieveList())
        if self.history.status() is True:
            self.history.preserve(self.wallpaper)
        self.retrieveFile(self.wallpaper)

    def previousWallpaper(self):
        print("Retrieving previous wallpaper...")
        if self.history.status() is True:
            imageList = self.history.retrieve()
            self.retrieveFile(imageList[-2])

    def setWindowsBackground(self, wallpaper):
        import ctypes
        SPI_SETDESKWALLPAPER = 20
        ctypes.windll.user32.SystemParametersInfoA(
            SPI_SETDESKWALLPAPER,
            0,
            wallpaper,
            0
        )

    def setLinuxBackground(self, wallpaper):
        print("linux")

    def main(self, x, cache):
        background = self
        background.cacheFileList(cache)

        if x == 0:
            background.previousWallpaper()

        if x == 1:
            background.nextWallpaper()

        if platform.system() == "Windows":
            self.setWindowsBackground(background.wallpaper)

        if platform.system == "Linux":
            self.setLinuxBackground(background.wallpaper)


if __name__ == '__main__':
    import sys
    try:
        x, cache = int(sys.argv[1]), bool(int(sys.argv[2]))
        Background.main(x, cache)
    except:
        raise AttributeError("Invalid arguments.")
