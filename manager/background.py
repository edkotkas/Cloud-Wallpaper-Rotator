# import random
# import platform


class Background(object):

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
        print("linux")
