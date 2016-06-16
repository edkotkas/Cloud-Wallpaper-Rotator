import os


class Helper(object):

    def __init__(self):
        self.realPath = lambda f: "/".join(
            str(os.path.realpath(__file__)).split("/")[:-1]
        ) + "/" + f
