from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os
import json
import random
import time

class History(object):

	def __init__(self, settings):
		self.settings = settings
		self.history_file = None

	def setHistoryFile(self, history_file):
		self.history_file = history_file

	def preserve(self, fileId):
		if self.status() is True:
			with open(self.history_file, "a") as history_file:
				history_file.write(fileId+"\n")

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

class Cache(object):

	def __init__(self, cache_file):
		self.cache_file = cache_file
		self.cache_age = int(time.time() - os.path.getmtime(self.cache_file))

	def preserve(self, imageList):
		with open(self.cache_file, "w+") as cache:
			cache.writelines(i+"\n" for i in imageList)

	def retrieveList(self):
		with open(self.cache_file, "r") as cache:
			return [str(imageId).strip() for imageId in cache.readlines()]


class Background(object):

	def __init__(self):
		self.realpath = "/".join(
			str(os.path.realpath(__file__)).split("/")[:-1]
		) + "/"

		self.output = self.realpath+"wallpaper.png"
		self.wallpaper = None

		with open(self.realpath+"settings.json", "r") as settings:
			self.settings = json.load(settings)

		self.cache = Cache(self.realpath+".cache")

		self.history = History(self.settings)
		if self.history.status() is True:
			self.history.setHistoryFile(".history")

		self.folderId = str(self.settings["folderId"])
		self.orderBy = str(self.settings["orderBy"])
		self.cacheAge = ((int(self.settings["cacheAge"])*24)*60)*60


		self.credentials = self.realpath+".credentials"

		self.gauth = GoogleAuth()
		self.gauth.LoadCredentialsFile(self.credentials)

		if self.gauth.credentials is None:
		    self.gauth.LocalWebserverAuth()
		elif self.gauth.access_token_expired:
		    self.gauth.Refresh()
		else:
		    self.gauth.Authorize()
		self.gauth.SaveCredentialsFile(self.credentials)

		self.drive = GoogleDrive(self.gauth)

		# writing back to settings file
		# with open(self.realpath+"/settings.json", "w+") as settings:
		# 	self.settings = json.dump(self.settings, settings)

	def cacheFileList(self, force=False):
		if self.cache.cache_age >= self.cacheAge or force is True:
			self.drive_files = self.drive.ListFile({
				'orderBy': self.orderBy,
				'q': "'" + \
				self.folderId + \
				"' in parents and trashed=false"
			}).GetList()
			print("Caching wallpaper list...")
			self.cache.preserve([files['id'] for files in self.drive_files])

	def retrieveFile(self, imageId):
		print("Downloading wallpaper...")
		self.drive.CreateFile({'id': imageId}).GetContentFile(self.output)

	def nextWallpaper(self):
		print("Retrieving next wallpaper...")
		self.wallpaper = random.choice(self.cache.retrieveList())
		if self.history.status() is True:
			self.history.preserve(self.wallpaper)
		self.retrieveFile(self.wallpaper)

	def previousWallpaper(self):
		print("Retrieving previous wallpaper...")
		if self.history.status() is True:
			imageList = self.history.retrieve()
			self.retrieveFile(imageList[-2])

if __name__ == '__main__':
	import sys
	try:
		x, cache = int(sys.argv[1]), bool(int(sys.argv[2]))
		Background().cacheFileList(cache)
		if x == 0:
			Background().previousWallpaper()
		if x == 1:
			Background().nextWallpaper()
	except:
		raise AttributeError("Invalid arguments.")
