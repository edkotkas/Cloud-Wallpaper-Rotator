import json
from pydrive.auth import GoogleAuth

# custom management imports
import helper.Helper as Helper
import history.History as History
import cache.Cache as Cache
import background.Background as Background


class Manager(object):

    def __init__(self, settingsFile, cache, history, drive):
        with open(Helper.realPath + settingsFile, "r") as settings:
            settings = json.load(settings)

        cache = Helper.realPath(".cache")
        history = Helper.realPath(".history")

        self.history = History(history)
        self.cache = Cache(cache)
        self.background = Background()
        self.credentials = Helper.realPath(".credentials")

        self.folderId = str(settings["folderId"])
        self.holdHistory = str(settings["history"])
        self.orderBy = str(settings["orderBy"])
        self.rotationFrequency = str(settings["rotationFrequency"])
        self.cachePeriod = ((int(settings["cachePeriod"]) * 24) * 60) * 60

    def googleAuthenticator(self):
        gauth = GoogleAuth()
        gauth.Loadself.credentials(self.credentials)

        if gauth.credentials is None:
            gauth.LocalWebserverAuth()
        elif gauth.access_token_expired:
            gauth.Refresh()
        else:
            gauth.Authorize()

        return gauth.Saveself.credentials(self.credentials)
