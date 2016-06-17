import platform
import subprocess

# custom management imports
from helper import Helper


class Background(object):

    def setBackground(self, wallpaper):
        if platform.system == "Windows":
            self.setWindowsBackground(wallpaper)

        if platform.system == "Linux":
            self.setLinuxBackground(wallpaper)

    def setWindowsBackground(self, wallpaper):
        Helper().printer("Setting Windows wallpaper")
        import ctypes
        SPI_SETDESKWALLPAPER = 20
        ctypes.windll.user32.SystemParametersInfoA(
            SPI_SETDESKWALLPAPER,
            0,
            wallpaper,
            0
        )

    def setLinuxBackground(self, wallpaper):
        Helper().printer("Settings Linux wallpaper")
        subprocess.call([
            "gsettings", "set", "org.gnome.desktop.background", "picture-uri",
            "file://" + wallpaper
        ])
