# creating lexicon of words
lexicon = {('direction','North'),
		   ('direction','South'),
		   ('direction','East'),
		   ('direction','West'),
		   ('direction','up'),
		   ('direction','down'),
		   ('direction','left'),
	       ('direction','right'),
		   ('direction','back'),
		   
		   ('verb','go'),
		   ('verb','stop'),
		   ('verb','kill'),
		   ('verb','eat'),
		   
		   ('stop','the'),
		   ('stop','in'),
		   ('stop','of'),
		   ('stop','from'),
		   ('stop','at'),
		   ('stop','it'),
		   
		   ('noun','door'),
		   ('noun','bear'),
		   ('noun','princess'),
		   ('noun','cabinet'),
		   
		   ('number','0'),
		   ('number','1'),
		   ('number','2'),
		   ('number','3'),
		   ('number','4'),
		   ('number','5'),
		   ('number','6'),
		   ('number','7'),
		   ('number','8'),
		   ('number','9'),
}


def scan(stuff):
	words = stuff.lower().split(' ')
	pairs = []
	
	for word in words:
		word_type = lexicon[word]
		tupes = (word, word_type)
		pair.append(tupes)
	return pairs
	

		   
