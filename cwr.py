import time

# custom management imports
from mgr import Manager
from helper import Helper


class CloudWallpaperRotator(Manager):

    def service(self):
        Helper().printer("Starting [CWR] Service")
        self.updateWallpaperCache()
        while True:
            self.getNextBackround()
            self.background.setBackground(self.outputFile)
            time.sleep(self.updateFrequency())


if __name__ == '__main__':
    CloudWallpaperRotator().service()
