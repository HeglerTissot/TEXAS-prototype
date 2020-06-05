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
	myDoc1 = tx.Document()
	myDoc1.setID("b4kijfg9")
	myDoc2 = tx.Document()
	myDoc2.setID("pd873jf6")
	myCorpus.add(myDoc1)
	myCorpus.add(myDoc2)
	print ( "type = " + myCorpus.getType() )
	print ( "myCorpus.JSON = " + myCorpus.getJSON() )

if __name__ == "__main__":
    example_01_corpus()
    example_02_document()
    example_03_documents()
	