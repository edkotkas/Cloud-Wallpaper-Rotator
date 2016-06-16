from store import Store


class Cache(Store):

    def __init__(self, cacheFile):
        Store.__init__(self, cacheFile)

    def cacheFileList(self, drive, folderId):
        driveFiles = drive.ListFile({
            'orderBy': self.orderBy,
            'q': "'" +
            folderId +
            "' in parents and trashed=false"
        }).GetList()
        print("Caching [%d] wallpapers..." % len(driveFiles))

        self.preserve([files['id'] for files in driveFiles])
