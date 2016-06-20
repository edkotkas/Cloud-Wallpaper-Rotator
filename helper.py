import os
import time


class Helper(object):

    def __init__(self):
        self.realPath = lambda fileReference: os.path.realpath(fileReference)

    def printer(self, message):
        print("[CWR] NOTICE <%s>: %s." % (time.strftime("%H:%M:%S"), message))

        return
