import texas as tx

def anns_01():
	print(">> anns_01:")
	myDoc = tx.Document()
	myDoc.setText("The patient is a 73-year-old female who was referred to Medical Center's Outpatient Rehabilitation Department for skilled speech therapy secondary to cognitive linguistic deficits. Based on the initial evaluation completed 12/29/08, the patient had mild difficulty with generative naming and auditory comprehension and recall. The patient's skilled speech therapy was recommended for three times a week for 8 weeks to improve her overall cognitive linguistic abilities. At this time, the patient has accomplished all 5 of her short-term therapy goals. She is able to complete functional mass tasks with 100% accuracy independently. She is able to listen to a narrative and recall the main idea plus at least five details after a 10 minute delay independently.")
	print ( "myDoc = " + myDoc.getJSON() )
	myDocAnns = tx.Spacy.annotate(myDoc)
	# myDocAnns.setID("spacy.doc.1")
	for annView in myDocAnns:
		myDoc.addAnnotationView(annView)
	print("-------------")
	print ( "myDoc = " + myDoc.getJSON() )

	mySent = tx.Sentence()
	mySent.setText("Python doesn't have a specific function to test whether a variable is defined, since all variables are expected to have been defined before use - even if initially just assigned the None object.")
	mySentAnns = tx.Spacy.annotate(mySent)
	# mySentAnns.setID("spacy.sent.1")
	for annView in mySentAnns:
		mySent.addAnnotationView(annView)

	print("-------------")
	print ( "mySent = " + mySent.getJSON() )

def anns_02():
	print("")
	print("")
	print("#############")
	print(">> anns_02 <<")
	print("#############")
	myDoc = tx.Document()
	myDoc.setText("William Jefferson Clinton is an American politician who served as the 42nd president of the United States from 1993 to 2001.")
	spacyAnns = tx.Spacy.annotate(myDoc)
	for annView in spacyAnns:
		myDoc.addAnnotationView(annView)
	print("-------------")
	print ( "myDoc = " + myDoc.getJSON() )
	
	
def anns_03():
	print("")
	print("")
	print("#############")
	print(">> anns_03 <<")
	print("#############")
	_json = '{"type": "document", "text": "William Jefferson Clinton is an American politician who served as the 42nd president of the United States from 1993 to 2001.", "anns": [{"type": "view", "id": "spacy.TOKENS", "meta": {"view_name": "TOKENS", "view_type": "spacy.en_core_web_sm"}, "bits": [{"type": "token", "id": 0, "meta": {"string": "William", "start": 0, "end": 7, "lemma": "William", "pos": "PROPN", "tag": "NNP", "dep": "compound", "iob": "B", "entity_id": 0, "entity_type": "PERSON", "flags": ["ALPHA", "SENTENCE_START", "TITLE"], "view_id": "spacy.TOKENS"}}, {"type": "token", "id": 1, "meta": {"string": "Jefferson", "start": 8, "end": 17, "lemma": "Jefferson", "pos": "PROPN", "tag": "NNP", "dep": "compound", "iob": "I", "entity_id": 0, "entity_type": "PERSON", "flags": ["ALPHA", "TITLE"], "view_id": "spacy.TOKENS"}}, {"type": "token", "id": 2, "meta": {"string": "Clinton", "start": 18, "end": 25, "lemma": "Clinton", "pos": "PROPN", "tag": "NNP", "dep": "nsubj", "iob": "I", "entity_id": 0, "entity_type": "PERSON", "flags": ["ALPHA", "TITLE"], "view_id": "spacy.TOKENS"}}, {"type": "token", "id": 3, "meta": {"string": "is", "start": 26, "end": 28, "lemma": "be", "pos": "AUX", "tag": "VBZ", "dep": "ROOT", "iob": "O", "flags": ["ALPHA", "LOWER", "STOP_WORD"], "view_id": "spacy.TOKENS"}}, {"type": "token", "id": 4, "meta": {"string": "an", "start": 29, "end": 31, "lemma": "an", "pos": "DET", "tag": "DT", "dep": "det", "iob": "O", "flags": ["ALPHA", "LOWER", "STOP_WORD"], "view_id": "spacy.TOKENS"}}, {"type": "token", "id": 5, "meta": {"string": "American", "start": 32, "end": 40, "lemma": "american", "pos": "ADJ", "tag": "JJ", "dep": "amod", "iob": "B", "entity_id": 1, "entity_type": "NORP", "flags": ["ALPHA", "TITLE"], "view_id": "spacy.TOKENS"}}, {"type": "token", "id": 6, "meta": {"string": "politician", "start": 41, "end": 51, "lemma": "politician", "pos": "NOUN", "tag": "NN", "dep": "attr", "iob": "O", "flags": ["ALPHA", "LOWER"], "view_id": "spacy.TOKENS"}}, {"type": "token", "id": 7, "meta": {"string": "who", "start": 52, "end": 55, "lemma": "who", "pos": "PRON", "tag": "WP", "dep": "nsubj", "iob": "O", "flags": ["ALPHA", "LOWER", "STOP_WORD"], "view_id": "spacy.TOKENS"}}, {"type": "token", "id": 8, "meta": {"string": "served", "start": 56, "end": 62, "lemma": "serve", "pos": "VERB", "tag": "VBD", "dep": "relcl", "iob": "O", "flags": ["ALPHA", "LOWER"], "view_id": "spacy.TOKENS"}}, {"type": "token", "id": 9, "meta": {"string": "as", "start": 63, "end": 65, "lemma": "as", "pos": "SCONJ", "tag": "IN", "dep": "prep", "iob": "O", "flags": ["ALPHA", "LOWER", "STOP_WORD"], "view_id": "spacy.TOKENS"}}, {"type": "token", "id": 10, "meta": {"string": "the", "start": 66, "end": 69, "lemma": "the", "pos": "DET", "tag": "DT", "dep": "det", "iob": "O", "flags": ["ALPHA", "LOWER", "STOP_WORD"], "view_id": "spacy.TOKENS"}}, {"type": "token", "id": 11, "meta": {"string": "42nd", "start": 70, "end": 74, "lemma": "42nd", "pos": "ADJ", "tag": "JJ", "dep": "amod", "iob": "B", "entity_id": 2, "entity_type": "ORDINAL", "flags": ["LOWER"], "view_id": "spacy.TOKENS"}}, {"type": "token", "id": 12, "meta": {"string": "president", "start": 75, "end": 84, "lemma": "president", "pos": "NOUN", "tag": "NN", "dep": "pobj", "iob": "O", "flags": ["ALPHA", "LOWER"], "view_id": "spacy.TOKENS"}}, {"type": "token", "id": 13, "meta": {"string": "of", "start": 85, "end": 87, "lemma": "of", "pos": "ADP", "tag": "IN", "dep": "prep", "iob": "O", "flags": ["ALPHA", "LOWER", "STOP_WORD"], "view_id": "spacy.TOKENS"}}, {"type": "token", "id": 14, "meta": {"string": "the", "start": 88, "end": 91, "lemma": "the", "pos": "DET", "tag": "DT", "dep": "det", "iob": "B", "entity_id": 3, "entity_type": "GPE", "flags": ["ALPHA", "LOWER", "STOP_WORD"], "view_id": "spacy.TOKENS"}}, {"type": "token", "id": 15, "meta": {"string": "United", "start": 92, "end": 98, "lemma": "United", "pos": "PROPN", "tag": "NNP", "dep": "compound", "iob": "I", "entity_id": 3, "entity_type": "GPE", "flags": ["ALPHA", "TITLE"], "view_id": "spacy.TOKENS"}}, {"type": "token", "id": 16, "meta": {"string": "States", "start": 99, "end": 105, "lemma": "States", "pos": "PROPN", "tag": "NNP", "dep": "pobj", "iob": "I", "entity_id": 3, "entity_type": "GPE", "flags": ["ALPHA", "TITLE"], "view_id": "spacy.TOKENS"}}, {"type": "token", "id": 17, "meta": {"string": "from", "start": 106, "end": 110, "lemma": "from", "pos": "ADP", "tag": "IN", "dep": "prep", "iob": "O", "flags": ["ALPHA", "LOWER", "STOP_WORD"], "view_id": "spacy.TOKENS"}}, {"type": "token", "id": 18, "meta": {"string": "1993", "start": 111, "end": 115, "lemma": "1993", "pos": "NUM", "tag": "CD", "dep": "pobj", "iob": "B", "entity_id": 4, "entity_type": "DATE", "flags": ["DIGIT"], "view_id": "spacy.TOKENS"}}, {"type": "token", "id": 19, "meta": {"string": "to", "start": 116, "end": 118, "lemma": "to", "pos": "ADP", "tag": "IN", "dep": "prep", "iob": "I", "entity_id": 4, "entity_type": "DATE", "flags": ["ALPHA", "LOWER", "STOP_WORD"], "view_id": "spacy.TOKENS"}}, {"type": "token", "id": 20, "meta": {"string": "2001", "start": 119, "end": 123, "lemma": "2001", "pos": "NUM", "tag": "CD", "dep": "pobj", "iob": "I", "entity_id": 4, "entity_type": "DATE", "flags": ["DIGIT"], "view_id": "spacy.TOKENS"}}, {"type": "token", "id": 21, "meta": {"string": ".", "start": 123, "end": 124, "lemma": ".", "pos": "PUNCT", "tag": ".", "dep": "punct", "iob": "O", "flags": ["PUNCT", "SENTENCE_END"], "view_id": "spacy.TOKENS"}}]}, {"type": "view", "id": "spacy.SENTENCES", "meta": {"view_name": "SENTENCES", "view_type": "spacy.en_core_web_sm"}, "bits": [{"type": "sentence", "id": 0, "meta": {"text": "William Jefferson Clinton is an American politician who served as the 42nd president of the United States from 1993 to 2001.", "start": 0, "end": 22, "start_char": 0, "end_char": 124, "view_id": "spacy.SENTENCES"}}]}, {"type": "view", "id": "spacy.NER", "meta": {"view_name": "NER", "view_type": "spacy.en_core_web_sm"}, "bits": [{"type": "entity", "id": 0, "meta": {"string": "William Jefferson Clinton", "label": "PERSON", "start": 0, "end": 3, "start_char": 0, "end_char": 25, "view_id": "spacy.NER"}}, {"type": "entity", "id": 1, "meta": {"string": "American", "label": "NORP", "start": 5, "end": 6, "start_char": 32, "end_char": 40, "view_id": "spacy.NER"}}, {"type": "entity", "id": 2, "meta": {"string": "42nd", "label": "ORDINAL", "start": 11, "end": 12, "start_char": 70, "end_char": 74, "view_id": "spacy.NER"}}, {"type": "entity", "id": 3, "meta": {"string": "the United States", "label": "GPE", "start": 14, "end": 17, "start_char": 88, "end_char": 105, "view_id": "spacy.NER"}}, {"type": "entity", "id": 4, "meta": {"string": "1993 to 2001", "label": "DATE", "start": 18, "end": 21, "start_char": 111, "end_char": 123, "view_id": "spacy.NER"}}]}]}'
	myDoc = tx.parseJSON(_json)
	print("-------------")
	print ( "myDoc = " + myDoc.getJSON() )
	
def anns_04():
	print("")
	print("")
	print("#############")
	print(">> anns_04 <<")
	print("#############")
	''' Spacy '''
	myDoc = tx.Document()
	myDoc.setText("Barack Hussein Obama II is an American attorney and politician who served as the 44th president of the United States from 2009 to 2017. A member of the Democratic Party, he was the first African American president of the United States.")
	ccgAnns = tx.Spacy.annotate(myDoc)
	for annView in ccgAnns:
		myDoc.addAnnotationView(annView)
	print("-------------")
	print ( "myDoc = " + myDoc.getJSON().replace("{","{\n") )
	''' CogComp '''
	myDoc = tx.Document()
	myDoc.setText("Barack Hussein Obama II is an American attorney and politician who served as the 44th president of the United States from 2009 to 2017. A member of the Democratic Party, he was the first African American president of the United States.")
	ccgAnns = tx.CogComp.annotate(myDoc)
	for annView in ccgAnns:
		myDoc.addAnnotationView(annView)
	print("-------------")
	print ( "myDoc = " + myDoc.getJSON().replace("{","{\n") )

if __name__ == "__main__":
	# anns_01()
	# anns_02()
	# anns_03()
	anns_04()
	