class History(object):

    def __init__(self, settings):
        self.settings = settings
        self.history_file = None

    def setHistoryFile(self, history_file):
        self.history_file = history_file

    def preserve(self, fileId):
        if self.status() is True:
            with open(self.history_file, "a") as history_file:
                history_file.write(fileId + "\n")

    def clear(self):
        with open(self.history_file, "w") as history_file:
            history_file.write("")

    def retrieve(self):
        with open(self.history_file, "r") as history:
            return [str(imageId).strip() for imageId in history.readlines()]

    def status(self):
        return bool(self.settings["history"])

    def disable(self):
        if self.status():
            self.settings["history"] = 0
            self.clear()
        print("Already off.")

    def enable(self):
        if not self.status():
            self.settings["history"] = 1
        print("Already on.")
