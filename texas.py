#
# TEXAS :: Text Annotation Schema
# Author : Hegler Tissot
# Version: 0.0.3
# Date   : 2020-06-19
#

import sys
import json
import urllib.parse
import urllib.request
import uuid

# (DEPRECATED)
# TEXAS_VALID_TYPES = ["corpus","document","section","paragraph","sentence","label","question","answer","list","view","token"]

TX_ATTRIBUTE_UUID = "id"
TX_ATTRIBUTE_TYPE = "type"
TX_ATTRIBUTE_META = "meta"
TX_ATTRIBUTE_TEXT = "text"
TX_ATTRIBUTE_BITS = "bits"
TX_ATTRIBUTE_ANNS = "anns"
TX_ANNS_VIEW_TYPE = "type"
TX_ATTRIBUTE_PARENT = "parent"

#==================================================
''' creators '''
#==================================================

def createTexas(text,type="document",id=""):
	newTexas = Texas(type)
	if not id is None and id != "": 
		newTexas.setID(id)
	newTexas.setText(text)
	return newTexas

def createCorpus(text,id=""):
	newTexas = Corpus()
	if not id is None and id != "": 
		newTexas.setID(id)
	newTexas.setText(text)
	return newTexas
def createDocument(text,id=""):
	newTexas = Document()
	if not id is None and id != "": 
		newTexas.setID(id)
	newTexas.setText(text)
	return newTexas
def createSection(text,id=""):
	newTexas = Section()
	if not id is None and id != "": 
		newTexas.setID(id)
	newTexas.setText(text)
	return newTexas
def createParagraph(text,id=""):
	newTexas = Paragraph()
	if not id is None and id != "": 
		newTexas.setID(id)
	newTexas.setText(text)
	return newTexas
def createSentence(text,id=""):
	newTexas = Sentence()
	if not id is None and id != "": 
		newTexas.setID(id)
	newTexas.setText(text)
	return newTexas
def createQuestion(text,id=""):
	newTexas = Question()
	if not id is None and id != "": 
		newTexas.setID(id)
	newTexas.setText(text)
	return newTexas
def createAnswer(text,id=""):
	newTexas = Answer()
	if not id is None and id != "": 
		newTexas.setID(id)
	newTexas.setText(text)
	return newTexas

#==================================================
''' parsers '''
#==================================================

def parseJSON(strJSON):
	dict = json.loads(strJSON)
	return parseDICT(dict)

def parseDICT(dict):
	if not TX_ATTRIBUTE_TYPE in dict:
		raise Exception("dict does not have 'type' entry")
	_pseudoSelf = Texas(dict[TX_ATTRIBUTE_TYPE])
	for jentry in dict:
		if jentry == TX_ATTRIBUTE_TYPE:
			None 
			#if _pseudoSelf.getType() != dict[jentry]:
			#	raise Exception("'"+"<"+_pseudoSelf.getType()+">"+_pseudoSelf.getID()+"' does not match JSON type '"+dict[jentry]+"'")
		elif jentry == TX_ATTRIBUTE_UUID:
			_pseudoSelf.setID(dict[jentry])
		elif jentry == TX_ATTRIBUTE_TEXT:
			_pseudoSelf.setText(dict[jentry])
		elif jentry == TX_ATTRIBUTE_META:
			meta = dict[jentry]
			if type(meta).__name__ != 'dict':
				raise Exception("'meta' is expected to be a dictionary in '"+"<"+_pseudoSelf.getType()+">"+_pseudoSelf.getID()+"'")
			for metaEntry in meta:
				_pseudoSelf.setMeta(metaEntry,meta[metaEntry])
		elif jentry == TX_ATTRIBUTE_BITS:
			bits = dict[jentry]
			if type(bits).__name__ != 'list':
				raise Exception("'bits' is expected to be a list in '"+"<"+_pseudoSelf.getType()+">"+_pseudoSelf.getID()+"'")
			for bit in bits:
				# (ToDo) MISSING: what if bit["type"] does not exist?
				# print (bit["type"])
				# newBit = Texas(bit["type"])
				newBit = parseDICT(bit)
				_pseudoSelf.add(newBit)
		elif jentry == TX_ATTRIBUTE_ANNS:
			anns = dict[jentry]
			if type(anns).__name__ != 'list':
				raise Exception("'anns' is expected to be a list in '"+"<"+_pseudoSelf.getType()+">"+_pseudoSelf.getID()+"'")
			for ann in anns:
				# (ToDo) MISSING: what if bit["type"] does not exist?
				# print (bit["type"])
				# newAnn = Texas(ann["type"])
				newAnn = parseDICT(ann)
				_pseudoSelf.add(newAnn)
		else:
			raise Exception("Unrecognized attribute '"+jentry+"' in '"+"<"+_pseudoSelf.getType()+">"+_pseudoSelf.getID()+"'")
	return _pseudoSelf

#==================================================
class Texas():
#==================================================

	def __init__(self, type):
		# if type not in TEXAS_VALID_TYPES:
		# 	raise Exception("invalid type '"+type+"': not in "+str(TEXAS_VALID_TYPES))
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
		if isinstance(text, str):
			self._text = text
		else:
			raise Exception("invalid type '"+type(text).__name__+"' for the string 'text' argument")

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

	def addAnnotationView(self, view):
		if view is None:
			return
		if not isinstance(view, AnnotationView):
			raise Exception("'"+"<"+view.__class__.__name__+">"+view.__name__+"' is not a View object")
		view.__setParent__(self)
		self._anns.append(view)
		return None

	def getAnnotationView(self, view_id):
		for view in self._anns:
			if view.getID() == view_id and (view.getType() == TX_ANNS_VIEW_TYPE):
				return view
		return None

	def getAllAnnotationViews(self):
		return self._anns

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

#==================================================
class ListOf(Texas):
#==================================================
	def __init__(self,type, named=""):
		super().__init__("list")
		if named == "": named = type+"_list"
		self.setAsListOf(type,named)

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
# AnnotationView
#==================================================
class AnnotationView(Texas):
	def __init__(self,view_name,view_type,generator=""):
		super().__init__("view")
		self.setMeta("view_name",view_name)
		self.setMeta("view_type",view_type)
		if generator != "":
			self.setMeta("generator",generator)
		self.setAsListOfAny()
	def setViewType(self,view_type):
		self.setMeta("view_type",view_type)
	def setGenerator(self,generator):
		self.setMeta("generator",generator)
	def setScore(self,score):
		self.setMeta("score",score)

#==================================================
# Annotation Constituents
#==================================================
class Annotation(Texas):
	def __init__(self,type):
		super().__init__(type)
	def setStart(self,start):
		self.setMeta("start",start)
	def setEnd(self,end):
		self.setMeta("end",end)
	
class AnnToken(Annotation):
	def __init__(self,token,start,end):
		super().__init__("token")
		self.setMeta("string",token)
		self.setMeta("start",start)
		self.setMeta("end",end)

class AnnSentence(Annotation):
	def __init__(self,text,start,end):
		super().__init__("sentence")
		self.setMeta("text",text)
		self.setMeta("start",start)
		self.setMeta("end",end)

class AnnNER(Annotation):
	def __init__(self,text,label,start,end):
		super().__init__("entity")
		self.setMeta("string",text)
		self.setMeta("label",label)
		self.setMeta("start",start)
		self.setMeta("end",end)

#==================================================
# Text preprocessing
#==================================================

def getCogcompJSON(view,text):
	# https://docs.python.org/3/howto/urllib2.html
	baseURL = 'https://cogcomp.seas.upenn.edu/mn4001/annotate' 
	params = {'views': view, 'text': text}
	url_POS = baseURL + "?" + urllib.parse.urlencode(params)
	with urllib.request.urlopen(url_POS) as response:
		json_str = response.read()
	try: 
		rdoc = json.loads(json_str)
	except ValueError as e: 
		raise Exception("URL {"+baseURL+"}?"+view+" result is not JSON format: "+str(json_str))
	return rdoc

''' CogComp '''
class CogComp:

	def annotate(texas):
		''' is Texas? '''
		if texas is None or not isinstance(texas, Texas):
			return
		text = texas.getText()
		if text is None or text.strip() == "":
			return
			
		anns = []

		''' TOKENS '''
		# rDOC = getCogcompJSON("POS",text)
		rDOC = getCogcompJSON("LEMMA",text)
		rNER = getCogcompJSON("NER_ONTONOTES",text)
		# rMEN = getCogcompJSON("MENTION",text)

		''' annotation sets '''
		theTokenAnns = AnnotationView(view_name="TOKENS",view_type="cogcomp")
		theTokenAnns.setID("cogcomp.TOKENS")
		sentenceEndPositions = rDOC["sentences"]["sentenceEndPositions"]
		theSentAnns = AnnotationView(view_name="SENTENCES",view_type="cogcomp")
		theSentAnns.setID("cogcomp.SENTENCES")

		''' pos / lemma '''
		pos_labels = []
		lemma_labels = []
		for view in rDOC["views"]:
			# print(view["viewName"])
			if view["viewName"] == "POS":
				constituents = view["viewData"][0]["constituents"]
				for pos in constituents:
					pos_labels.append(pos["label"])
			if view["viewName"] == "LEMMA":
				constituents = view["viewData"][0]["constituents"]
				for lemma in constituents:
					lemma_labels.append(lemma["label"])
				
		tokenidx = 0
		offset = 0
		token_labels = []
		for rtoken in rDOC["tokens"]:
			token = AnnToken(rtoken,0,0)
			token.setID(tokenidx)
			start = text.find(rtoken,offset)
			offset = start+len(rtoken)
			token.setStart(start)
			token.setEnd(offset)
			token_labels.append({"start":start, "end":offset})
			flags = []
			if (tokenidx+1) in sentenceEndPositions: flags.append("SENTENCE_END") 
			if tokenidx == 0 or tokenidx in sentenceEndPositions: flags.append("SENTENCE_START") 
			token.setMeta("pos",pos_labels[tokenidx])
			token.setMeta("lemma",lemma_labels[tokenidx])
			'''
			if not rtoken.lemma_ is None: token.setMeta("lemma",rtoken.lemma_)
			if not rtoken.tag_ is None: token.setMeta("tag",rtoken.tag_)
			if not rtoken.dep_ is None: token.setMeta("dep",rtoken.dep_)
			if not rtoken.ent_iob_ is None and rtoken.ent_iob_ != '': token.setMeta("iob",rtoken.ent_iob_)
			'''
			if len(flags) > 0:
				token.setMeta("flags",flags)
			theTokenAnns.add(token)
			tokenidx = tokenidx + 1
		anns.append(theTokenAnns)
		
		for view in rDOC["views"]:
			if view["viewName"] == "SENTENCE":
				constituents = view["viewData"][0]["constituents"]
				sentidx = 0
				for rsent in constituents:
					start = rsent["start"]
					end = rsent["end"]
					start_char = token_labels[start]["start"]
					end_char = token_labels[end-1]["end"]
					sent = AnnSentence(text[start_char:end_char],start,end)
					sent.setID(sentidx)
					sent.setMeta("start_char",start_char)
					sent.setMeta("end_char",end_char)
					theSentAnns.add(sent)
					sentidx = sentidx + 1
				anns.append(theSentAnns)
					
		''' NER '''
		theNERAnns = AnnotationView(view_name="NER",view_type="cogcomp")
		theNERAnns.setID("cogcomp.NER")
		entityidx = 0
		for view in rNER["views"]:
			if view["viewName"] == "NER_ONTONOTES":
				constituents = view["viewData"][0]["constituents"]
				sentidx = 0
				for rsent in constituents:
					start = rsent["start"]
					end = rsent["end"]
					start_char = token_labels[start]["start"]
					end_char = token_labels[end-1]["end"]
					entity = AnnNER(text[start_char:end_char],rsent["label"],start,end)
					entity.setID(entityidx)
					entity.setMeta("start_char",start_char)
					entity.setMeta("end_char",end_char)
					theNERAnns.add(entity)
					entityidx = entityidx + 1
				anns.append(theNERAnns)
		
		''' resulting annotations '''
		return anns

''' Spacy '''
class Spacy:

	_model = None
	_spDefaultModel = 'en_core_web_sm' 
	
	def annotate(texas):
		''' is Texas? '''
		if texas is None or not isinstance(texas, Texas):
			return
		text = texas.getText()
		if text is None or text.strip() == "":
			return
		
		''' load spacy '''
		if "spacy" not in sys.modules:
			print('Importing spacy...')
			import spacy
		if Spacy._model is None:
			print("Loading spacy language model...")
			Spacy._model = spacy.load(Spacy._spDefaultModel)
		print("Spacy preprocessing...")

		anns = []

		''' TOKENS '''
		rdoc = Spacy._model(text)
		theTokenAnns = AnnotationView(view_name="TOKENS",view_type="spacy")
		theTokenAnns.setID("spacy.TOKENS")
		# texas.addAnnotationView(theTokenAnns)
		tokenidx = 0
		offset = 0
		for rtoken in rdoc:
			# print(token.text, token.lemma_, token.pos_, token.is_sent_start, token.tag_, token.dep_, token.shape_, token.is_alpha, token.is_stop)
			token = AnnToken(rtoken.text,0,0)
			token.setID(tokenidx)
			start = text.find(rtoken.text,offset)
			offset = start+len(rtoken.text)
			token.setStart(start)
			token.setEnd(offset)
			if not rtoken.lemma_ is None: token.setMeta("lemma",rtoken.lemma_)
			if not rtoken.pos_ is None: token.setMeta("pos",rtoken.pos_)
			if not rtoken.tag_ is None: token.setMeta("tag",rtoken.tag_)
			if not rtoken.dep_ is None: token.setMeta("dep",rtoken.dep_)
			if not rtoken.ent_iob_ is None and rtoken.ent_iob_ != '': token.setMeta("iob",rtoken.ent_iob_)
			entity_id = None
			entityidx = 0
			for rentity in rdoc.ents:
				if tokenidx >= rentity.start and tokenidx < rentity.end:
					entity_id = entityidx
				entityidx = entityidx + 1
			if not entity_id is None: token.setMeta("entity_id",entity_id)
			if not rtoken.ent_type_ is None and rtoken.ent_type_ != '': token.setMeta("entity_type",rtoken.ent_type_)
			flags = []
			if rtoken.is_alpha      : flags.append("ALPHA") 
			if rtoken.is_bracket    : flags.append("BRACKET") 
			if rtoken.is_currency   : flags.append("CURRENCY") 
			if rtoken.is_digit      : flags.append("DIGIT") 
			if rtoken.is_left_punct : flags.append("LEFT_PUNCT") 
			if rtoken.is_lower      : flags.append("LOWER") 
			if rtoken.is_punct      : flags.append("PUNCT") 
			if rtoken.is_quote      : flags.append("QUOTE") 
			if rtoken.is_right_punct: flags.append("RIGHT_PUNCT") 
			if rtoken.is_sent_start : flags.append("SENTENCE_START") 
			if rtoken.is_sent_end   : flags.append("SENTENCE_END") 
			if rtoken.is_space      : flags.append("SPACE") 
			if rtoken.is_stop       : flags.append("STOP_WORD") 
			if rtoken.is_title      : flags.append("TITLE") 
			if rtoken.is_upper      : flags.append("UPPER") 
			if len(flags) > 0:
				token.setMeta("flags",flags)
			theTokenAnns.add(token)
			tokenidx = tokenidx + 1
		anns.append(theTokenAnns)

		''' SENTENCES '''
		theSentAnns = AnnotationView(view_name="SENTENCES",view_type="spacy")
		theSentAnns.setID("spacy.SENTENCES")
		sentidx = 0
		for rsent in rdoc.sents:
			sent = AnnSentence(rsent.text,rsent.start,rsent.end)
			sent.setID(sentidx)
			sent.setMeta("start_char",rsent.start_char)
			sent.setMeta("end_char",rsent.end_char)
			theSentAnns.add(sent)
			sentidx = sentidx + 1
		anns.append(theSentAnns)
		
		''' NER '''
		theNERAnns = AnnotationView(view_name="NER",view_type="spacy")
		theNERAnns.setID("spacy.NER")
		entityidx = 0
		for rentity in rdoc.ents:
			entity = AnnNER(rentity.text,rentity.label_,rentity.start,rentity.end)
			entity.setID(entityidx)
			entity.setMeta("start_char",rentity.start_char)
			entity.setMeta("end_char",rentity.end_char)
			theNERAnns.add(entity)
			entityidx = entityidx + 1
		anns.append(theNERAnns)

		''' resulting annotations '''
		return anns
