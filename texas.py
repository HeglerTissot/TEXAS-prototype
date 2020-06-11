import json
import uuid

TEXAS_VALID_TYPES = ["corpus","document","section","paragraph","sentence","label","question","answer","list"]

TX_ATTRIBUTE_UUID = "id"
TX_ATTRIBUTE_TYPE = "type"
TX_ATTRIBUTE_META = "meta"
TX_ATTRIBUTE_TEXT = "text"
TX_ATTRIBUTE_BITS = "bits"
TX_ATTRIBUTE_ANNS = "anns"
TX_ANNS_VIEW_TYPE = "type"
TX_ATTRIBUTE_PARENT = "parent"

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
		self._anns = []
		self._isListOf = None
		self._listName = TX_ATTRIBUTE_BITS
		self._parent = None
    
	def getType(self):
		if self._type is None:
			return ""
		else:
			return self._type

	def setUUID(self):
		self._uuid = str(uuid.uuid4())[-12:]

	def setID(self, id):
		self._uuid = id

	def unsetID(self):
		self._uuid = None

	def getID(self):
		if self._uuid is None:
			return ""
		else:
			return self._uuid

	def setText(self, text):
		self._text = text

	def unsetText(self):
		self._text = None

	def getText(self):
		if self._text is None:
			return ""
		else:
			return self._text

	def setMeta(self, property, value):
		if (value == "" or value is None) and property in self._meta:
			self.unsetMeta(property)
		else:
			self._meta[property] = value

	def unsetMeta(self, property):
		if property in self._meta:
			self._meta.pop(property)

	def getMeta(property):
		if property in self._meta:
			return self._meta[property]
		else:
			return None

	def getMetaAll():
		return self._meta

	def setAsListOfAny(self):
		self._isListOf = None
		self._listName = TX_ATTRIBUTE_BITS
		
	def setAsListOf(self, type, name = TX_ATTRIBUTE_BITS):
		self._isListOf = type
		# temporarilly disabled
		# self._listName = name

	def __setParent__(self,parent):
		if self._parent is not None:
			self.unsetMeta(self._parent.getType()+"_id")
			self._parent.remove(self)
		self._parent = parent
		if self._parent is not None and self._parent.getID() != "":
			self.setMeta(self._parent.getType()+"_id",self._parent.getID())
	
	def add(self, texas):
		if texas is None:
			return
		if not isinstance(texas, Texas):
			raise Exception("'"+"<"+texas.__class__.__name__+">"+texas.__name__+"' is not a Texas object")
		if self._isListOf is None or self._isListOf == texas.getType():
			texas.__setParent__(self)
			self._bits.append(texas)
		else:
			raise Exception("'"+texas.getType()+"' not allowed to be added into <"+self.getType()+">'"+self.getID()+"', which is a list of '"+self._isListOf+"'")

	def remove(self, texas):
		if texas is None:
			return
		if not isinstance(texas, Texas):
			raise Exception("'"+"<"+texas.__class__.__name__+">"+texas.__name__+"' is not a Texas object")
		texas._parent = None
		if texas in self._bits:
			self._bits.remove(texas)

	def get(self, id, type = ""):
		for bit in self._bits:
			if bit.getID() == id and (bit.getType() == type or type == ""):
				return bit
		return None

	def getAll(self):
		return self._bits

	def getAnnotationView(self, view_id):
		for view in self._anns:
			if view.getID() == view_id and (view.getType() == TX_ANNS_VIEW_TYPE):
				return view
		return None

	def getAnns(self):

	def getDICT(self):
		d = {}
		d[TX_ATTRIBUTE_TYPE] = self._type
		if self._uuid is not None and self._uuid != "":
			d[TX_ATTRIBUTE_UUID] = self._uuid
		if self._meta:
			d[TX_ATTRIBUTE_META] = self._meta
		if self._text is not None:
			d[TX_ATTRIBUTE_TEXT] = self._text
		if len(self._bits) > 0:
			d[self._listName] = []
			for bit in self._bits:
				d[self._listName].append(bit.getDICT())
		if len(self._anns) > 0:
			d[TX_ATTRIBUTE_ANNS] = []
			for view in self._anns:
				d[TX_ATTRIBUTE_ANNS].append(view.getDICT())
		return d

	def getJSON(self):
		return json.dumps(self.getDICT())

	def parseJSON(self, strJSON):
		dict = json.loads(strJSON)
		self.parseDICT(dict)

	def parseDICT(self, dict):
		for jentry in dict:
			# print(">>> " + jentry)
			if jentry == TX_ATTRIBUTE_TYPE:
				if self.getType() != dict[jentry]:
					raise Exception("'"+"<"+self.getType()+">"+self.getID()+"' does not match JSON type '"+dict[jentry]+"'")
			elif jentry == TX_ATTRIBUTE_UUID:
				self.setID(dict[jentry])
			elif jentry == TX_ATTRIBUTE_TEXT:
				self.setText(dict[jentry])
			elif jentry == TX_ATTRIBUTE_META:
				meta = dict[jentry]
				if type(meta).__name__ != 'dict':
					raise Exception("'meta' is expected to be a dictionary in '"+"<"+self.getType()+">"+self.getID()+"'")
				for metaEntry in meta:
					self.setMeta(metaEntry,meta[metaEntry])
			elif jentry == TX_ATTRIBUTE_BITS:
				bits = dict[jentry]
				if type(bits).__name__ != 'list':
					raise Exception("'bits' is expected to be a list in '"+"<"+self.getType()+">"+self.getID()+"'")
				for bit in bits:
					# (ToDo) MISSING: what if bit["type"] does not exist?
					# print (bit["type"])
					newBit = Texas(bit["type"])
					newBit.parseDICT(bit)
					self.add(newBit)
			else:
				raise Exception("Unrecognized attribute '"+jentry+"' in '"+"<"+self.getType()+">"+self.getID()+"'")

#==================================================
class Corpus(Texas):
#==================================================
	def __init__(self):
		super().__init__("corpus")
		self.setAsListOf("document","documents")
		
#==================================================
class Document(Texas):
#==================================================
	def __init__(self):
		super().__init__("document")

	def setDCT(self, dct):
		self.setMeta("dct",dct)

	def unsetDCT(self):
		self.unsetMeta("dct")

	def getDCT():
		return self.getMeta("dct")

#==================================================
class Section(Texas):
#==================================================
	def __init__(self):
		super().__init__("section")

#==================================================
class Paragraph(Texas):
#==================================================
	def __init__(self):
		super().__init__("paragraph")

#==================================================
class Sentence(Texas):
#==================================================
	def __init__(self):
		super().__init__("sentence")

#==================================================
class Label(Texas):
#==================================================
	def __init__(self):
		super().__init__("label")

#==================================================
class Question(Texas):
#==================================================
	def __init__(self):
		super().__init__("question")

#==================================================
class Answer(Texas):
#==================================================
	def __init__(self):
		super().__init__("answer")

#==================================================
# Annotation View
#==================================================
class View(Texas):
	def __init__(self,viewName):
		super().__init__("view")
		self.setMeta("view_name",viewName)
class AnnotationView(viewName):
	def __init__(self):
		super().__init__(viewName)
class TokenizerView():
	def __init__(self):
		super().__init__("TOKENIZER")
		self.setAsListOf("token")

#==================================================
# Annotation Constituents
#==================================================
class Token(Texa):
	def __init__(self,label,start=-1,end=-1,score=-1):
		super().__init__("token")
		self.setMeta("label",label)
		self.setMeta("offset_start",start)
		self.setMeta("offset_end",end)
		self.setMeta("score",score)

#==================================================
class ListOf(Texas):
#==================================================
	def __init__(self,type, named=""):
		super().__init__("list")
		if named == "": named = type+"_list"
		self.setAsListOf(type,named)

