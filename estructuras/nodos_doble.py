class nodo:
	def setinfo(self,informa):
		self.sig = None
		self.ante = None
		self.info = informa
	def getsig(self):
		return self.sig

	def getante(self):
		return self.ante

	def getinfo(self):
		return self.info

	def setsig(self, informacion):
		self.sig = informacion

	def setante(self, informacion):
		self.ante = informacion

