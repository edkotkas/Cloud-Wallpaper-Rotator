import time

# custom management imports
from manager import Manager, Helper


class CloudWallpaperRotator(Manager):

    def service(self):
        Helper().printer("Starting [CWR] Service")
        while True:
            self.getNext()
            self.background.setLinuxBackground(self.outputFile)
            time.sleep(self.updateFrequency())

if __name__ == '__main__':
    CloudWallpaperRotator().service()
