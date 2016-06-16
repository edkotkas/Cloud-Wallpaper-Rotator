class Store(object):

    def __init__(self, fileName):
        self.fileName = fileName

    def preserve(self, *fileIds):
        with open(self.fileName, "w+") as f:
            f.writelines(fileId + "\n" for fileId in fileIds)

    def retrieveList(self):
        with open(self.file, "r") as f:
            return [
                str(imageId).strip()
                for imageId in f.readlines()
            ]
