import time
import os
import json
import datetime


class Cache(object):

    def __init__(self, cache_file):
        self.cache_file = cache_file
        self.cache_age = int(time.time() - os.path.getmtime(self.cache_file))

    def preserve(self, imageList):
        with open(self.cache_file, "w+") as cache:
            cache.writelines(i + "\n" for i in imageList)

        real_path = "/".join(
            str(os.path.realpath(__file__)).split("/")[:-1]
        ) + "/"

        cache_date = None

        with open(real_path + "settings.json", "r") as settings:
            cache_date = json.load(settings)

        cache_date["lastCacheUpdate"] = datetime.date.today()

        with open(self.realpath + "/settings.json", "w+") as settings:
            cache_date = json.dump(cache_date, settings)

    def retrieveList(self):
        with open(self.cache_file, "r") as cache:
            return [str(imageId).strip() for imageId in cache.readlines()]
