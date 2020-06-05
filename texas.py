import json

TEXAS_VALID_TYPES = ["corpus","document","section","paragraph","sentence"]

#==================================================
class Texas():
#==================================================

	def __init__(self, type):
		if type not in TEXAS_VALID_TYPES:
			raise Exception("invalid type '"+type+"': not in "+str(TEXAS_VALID_TYPES))
		self._uuid = None
		self._type = type
		self._meta = {}
		self._text = None
		self._bits = []
    
	def getType(self):
		return self._type

	def setID(self, id):
		self._uuid = id

	def getID(self):
		return self._uuid

	def setText(self, text):
		self._text = text

	def getText(self):
		return self._text

	def setMeta(self, property, value):
		if (value == "" or value is None) and property in self._meta:
			self._meta.pop(property)
		else:
			self._meta[property] = value

	def getMeta(property):
		return self._meta[property]

	def getMetaAll():
		return self._meta

	def add(self, texas):
		if texas is None:
			return
		if not isinstance(texas, Texas):
			raise Exception("'"+"<"+texas.__class__.__name__+">"+texas.__name__+"' is not a Texas object")
		print ("adding(a)..." + texas.__class__.__name__)
		print ("adding(b)..." + type(texas).__name__)

	def getDICT(self):
		d = {}
		d["type"] = self._type
		if self._uuid is not None and self._uuid != "":
			d["id"] = self._uuid
		if self._meta:
			d["meta"] = self._meta
		if self._uuid is not None:
			d["text"] = self._text
		return d

	def getJSON(self):
		return json.dumps(self.getDICT())

#==================================================
class Corpus(Texas):
#==================================================
	def __init__(self):
		self._type = type
		super().__init__("corpus")

#==================================================
class Document(Texas):
#==================================================
	def __init__(self):
		self._type = type
		super().__init__("document")

#==================================================
class Section(Texas):
#==================================================
	def __init__(self):
		self._type = type
		super().__init__("section")

#==================================================
class Paragraph(Texas):
#==================================================
	def __init__(self):
		self._type = type
		super().__init__("paragraph")

#==================================================
class Sentence(Texas):
#==================================================
	def __init__(self):
		self._type = type
		super().__init__("sentence")


