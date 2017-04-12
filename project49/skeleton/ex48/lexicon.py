vocabulary = {
	'direction': 'north south east west up down left right back'.split(),
	'noun': 'bear princess door cabinet'.split(),
	'stop': 'the in of from at it'.split(),
	'verb': 'go kill eat stop'.split()
}

'''
This creates a lookup using a dictionary-comprehension:
{'at': 'stop'
#[...]
'up':'direction'
'west':'direction'
'''
classification = {i:k for k,v in vocabulary.iteritems() for i in v}

def classify(word):
	try:
		return 'number', int(word)
	except ValueError:
		return classification.get(word, 'error'), word


def scan(words):
	return [classify(word) for word in words.split()]
