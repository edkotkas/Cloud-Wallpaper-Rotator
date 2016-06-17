from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import json
import random
import os
import time

# custom management imports
from helper import Helper
from history import History
from cache import Cache
from background import Background


class Manager(object):

    def __init__(self):
        settingsFile = Helper().realPath("myconfig.json")
        with open(settingsFile, "r") as settings:
            _settings = json.load(settings)

        self.outputFile = Helper().realPath("wallpaper.png")

        self.credentials = Helper().realPath(".credentials")
        self.drive = GoogleDrive(
            self.googleAuthenticator()
        )

        self.folderId = str(_settings["folderId"])
        self.holdHistory = str(_settings["history"])
        self.orderBy = str(_settings["orderBy"])
        self.rotationFrequency = str(_settings["rotationFrequency"])
        self.cachePeriod = ((int(_settings["cachePeriod"]) * 24) * 60) * 60

        cache = Helper().realPath(".cache")
        history = Helper().realPath(".history")

        self.history = History(history)
        self.cache = Cache(cache)
        self.background = Background()

    def updateFrequency(self):
        period = int(self.rotationFrequency[:-1])

        amount = self.timeAmountConverter(
            str(self.rotationFrequency[-1])
        )

        return float(period * amount)

    def timeAmountConverter(self, amount):
        if amount == "d":
            return 24 * 60 * 60
        if amount == "h":
            return 60 * 60
        if amount == "m":
            return 60
        if amount == "s":
            return 1

    def googleAuthenticator(self):
        Helper().printer("Authenticating with Google Account.")
        gauth = GoogleAuth()
        gauth.LoadCredentialsFile(self.credentials)

        if gauth.credentials is None:
            gauth.LocalWebserverAuth()
        elif gauth.access_token_expired:
            gauth.Refresh()
        else:
            gauth.Authorize()

        gauth.SaveCredentialsFile(self.credentials)

        return gauth

    def updateWallpaperCache(self, forceUpdate=False):
        cacheAge = int(time.time() - os.path.getmtime(self.cache.fileName))

        if cacheAge >= self.cachePeriod or forceUpdate is True:
            self.cache.cacheWallpapers(
                self.drive,
                self.folderId,
                self.orderBy
            )

    def getNext(self):
        wallpaper = random.choice(self.cache.retrieveList())

        if self.holdHistory is True:
            self.history.preserve(wallpaper)

        self.retrieveFile(wallpaper)

    def getPrevious(self):
        if self.holdHistory is True:
            Helper().printer("Accessing local history")
            history = self.history.retrieveList()

            if len(history) < 2:
                return

            wallpaper = history[-2]

            self.retrieveFile(wallpaper)

    def retrieveFile(self, imageId):
        Helper().printer("Downloading wallpaper")
        self.drive.CreateFile({'id': imageId}).GetContentFile(self.outputFile)
