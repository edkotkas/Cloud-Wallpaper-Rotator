from store import Store
from helper import Helper


class Cache(Store):

    def __init__(self, cacheFile):
        Store.__init__(self, cacheFile)

    def cacheWallpapers(self, drive, folderId, order):
        driveFiles = drive.ListFile({
            'orderBy': order,
            'q': "'" +
            folderId +
            "' in parents and trashed=false"
        }).GetList()

        Helper().printer("Caching [%d] wallpapers to file" % len(driveFiles))

        self.preserve(*[files['id'] for files in driveFiles])
