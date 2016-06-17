import os
# import time


class Helper(object):

    def __init__(self):
        self.realPath = lambda f: "/".join(
            str(os.path.realpath(__file__)).split("/")[:-1]
        ) + "/" + f

    def printer(self, message):
        # print("[CWR] NOTICE <%s>: %s."
        # % (time.strftime("%H:%M:%S"), message))

        return
