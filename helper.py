import os
import time
import sys


class Helper(object):

    def __init__(self):
        self.realPath = lambda fileReference: "/".join(
            os.path.realpath(__file__).split("/")[:-1]
        ) + "/" + fileReference

    def printer(self, message):
        notice = "[CWR] NOTICE <%s>: %s." %\
            (time.strftime("%H:%M:%S"), message)

        print(notice, "\n", sys.stderr)

        with open(self.realPath("log"), "a") as log:
            log.writelines(notice + "\n")
