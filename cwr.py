from pydrive.drive import GoogleDrive

# custom management imports
import manager.Helper as Helper
import manager.Manager as Manager


class CloudWallpaperRotator(object):

    def __init__(self):
        self.outputFile = Helper.realPath("wallpaper.png")

        self.manager = Manager(Helper.realPath("config.json"))

        self.drive = GoogleDrive(
            self.manager.googleAuthenticator()
        )

    def retrieveFile(self, imageId):
        print("Downloading wallpaper...")
        self.drive.CreateFile({'id': imageId}).GetContentFile(self.wallpaper)
