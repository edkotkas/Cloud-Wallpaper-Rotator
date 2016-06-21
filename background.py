import platform
import subprocess

# custom management imports
from helper import Helper


class Background(object):

    def setBackground(self, wallpaper):
        Helper().printer("Setting wallpaper for %s" % (platform.system()))
        if platform.system() == "Windows":
            self.setWindowsBackground(wallpaper)

        if platform.system() == "Linux":
            self.setLinuxBackground(wallpaper)

        if platform.system() == "OSX":
            self.setMacBackground(wallpaper)

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
        subprocess.call([
            "gsettings", "set", "org.gnome.desktop.background", "picture-uri",
            "file://" + wallpaper
        ])

    def setMacBackground(self, wallpaper):
        print("")
