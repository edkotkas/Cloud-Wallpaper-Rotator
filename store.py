from helper import Helper


class Store(object):

    def __init__(self, fileName):
        self.fileName = fileName

    def preserve(self, *fileIds):
        Helper().printer("Preserving data locally")
        with open(self.fileName, "w+") as f:
            f.writelines(fileId + "\n" for fileId in fileIds)

    def retrieveList(self):
        Helper().printer("Accessing local data")
        with open(self.fileName, "r") as f:
            return [
                str(imageId).strip()
                for imageId in f.readlines()
            ]
