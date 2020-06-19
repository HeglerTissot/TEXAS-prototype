import texas as tx

def example_01_corpus():
	print(">> example_01_corpus:")
	myCorpus = tx.Corpus()
	print ( "type = " + myCorpus.getType() )
	print ( "JSON = " + myCorpus.getJSON() )
	myCorpus.setID("9j3nb94d")
	print ( "JSON = " + myCorpus.getJSON() )
	myCorpus.setMeta("DCT","2020-06-04")
	print ( "JSON = " + myCorpus.getJSON() )
	myCorpus.setMeta("DCT",None)
	print ( "JSON = " + myCorpus.getJSON() )
	myCorpus.setMeta("DCT","2020-06-04")
	myCorpus.setMeta("name","TexAS_Example_Corpus")
	myCorpus.setText("What is the sense of having a text for a corpus?")
	print ( "JSON = " + myCorpus.getJSON() )
	
def example_02_document():
	print(">> example_02_document:")
	myDoc = tx.Document()
	myDoc.setID("2409jgv0")
	print ( "type = " + myDoc.getType() )
	print ( "myDoc.JSON = " + myDoc.getJSON() )

def example_03_documents():
	print(">> example_03_documents:")
	myCorpus = tx.Corpus()
	myCorpus.setID("98hn4g4i")
	myCorpus.setDCT("2020-06-05")
	myDoc1 = tx.Document()
	myDoc1.setID("b4kijfg9")
	myDoc2 = tx.Document()
	myDoc2.setID("pd873jf6")
	myDoc3 = tx.Document()
	myDoc3.setID("sk93jf23")
	myCorpus.add(myDoc1)
	myCorpus.add(myDoc2)
	myCorpus.add(myDoc3)
	print ( "type = " + myCorpus.getType() )
	print ( "myCorpus.JSON = " + myCorpus.getJSON() )
	
	
def example_04_parse_setences():
	print(">> example_04_parse_setences:")
	myJSON= '{"type": "list", "id": "d9jrjg3q", "meta": {"dct": "2020-06-05", "authors": ["hegler", "tissot"]}, "bits": [{"type": "sentence", "id": "s1", "meta": {"status": "deprecated", "list_id": "d9jrjg3q"}, "text": "Do you have anything else to say?"}, {"type": "sentence", "id": "s2", "meta": {"status": "active", "list_id": "d9jrjg3q"}, "text": "This is my last comment.", "bits": [{"type": "corpus", "id": "98hn4g4i", "meta": {"dct": "2020-06-05", "sentence_id": "s2"}, "bits": [{"type": "document", "id": "b4kijfg9", "meta": {"corpus_id": "98hn4g4i"}}, {"type": "document", "id": "pd873jf6", "meta": {"corpus_id": "98hn4g4i"}}, {"type": "document", "id": "sk93jf23", "meta": {"corpus_id": "98hn4g4i"}}]}]}]}'
	mySents = tx.ListOf("sentence","sentences")
	mySents.setUUID()
	mySents.parseJSON(myJSON)
	print ( "mySents.JSON = " + mySents.getJSON() )
	print("---")


def example_05_annotations():
	print(">> example_05_annotations:")
	myDoc = tx.Document()
	myDoc.setUUID()
	myDoc.setText("Barack Obama served as the 44th president of the United States from 2009 to 2017.")

	theSentences = tx.SentenceView()
	theSentences.add( tx.Sentence("Barack Obama served as the 44th president of the United States from 2009 to 2017.",0,81) )
	
	theTokens = tx.TokenView()
	theTokens.add( tx.Token("Barack",0,6) )
	theTokens.add( tx.Token("Obama",7,12) )
	theTokens.add( tx.Token("served",13,19) )
	theTokens.add( tx.Token("as",20,22) )
	theTokens.add( tx.Token("the",23,26) )
	theTokens.add( tx.Token("44th",27,31) )
	theTokens.add( tx.Token("president",32,41) )
	theTokens.add( tx.Token("of",42,44) )
	theTokens.add( tx.Token("the",45,48) )
	theTokens.add( tx.Token("United",49,55) )
	theTokens.add( tx.Token("States",46,62) )
	theTokens.add( tx.Token("from",63,67) )
	theTokens.add( tx.Token("2009",68,72) )
	theTokens.add( tx.Token("to",73,75) )
	theTokens.add( tx.Token("2017",76,80) )
	theTokens.add( tx.Token(".",80,81) )
	
	myDoc.addAnnotationView(theSentences)
	myDoc.addAnnotationView(theTokens)
	
	print ( "myDoc.JSON = " + myDoc.getJSON() )
	# print ( "theTokens.JSON = " + theTokens.getJSON() )
	print("---")


if __name__ == "__main__":
	# example_01_corpus()
	# example_02_document()
	# example_03_documents()
	# example_04_parse_setences()
	example_05_annotations()
	