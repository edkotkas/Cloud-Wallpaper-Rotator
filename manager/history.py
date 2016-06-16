from store import Store


class History(Store):

    def __init__(self, historyFile):
        Store.__init__(self, historyFile)
