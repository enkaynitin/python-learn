from nose.tools import *
from ex49 import parser

def test_parse_subject():

	testsentence = "princess go east"
	result = lexicon.scan(testsentence)
	Sent = parse_sentence(result)
	ResultSent = Sentence(('subject', 'princess'),
					('verb', 'go'),
					('object', 'east'))

	print ResultSent.subject
	print ResultSent.verb
	print ResultSent.object
	print Sent.subject
	print Sent.verb
	print Sent.object
	assert_equal(Sent, ResultSent)
		

import unittest

class A:
	
	def __init__(self, num):
		self.num = num
	
	def __eq__(self,other):
		return self.num == other.num
		
class Test(unittest.TestCase):

	def test(self):
		a1 = A(1)
		a12 = A(1)
		a2 = A(2)
		
		self.assertEqual(a1, a1, 'a1 !=a1')
		self.assertEqual(a1, a12, 'a1 != a12')
		self.assertEqual(a1, a2, 'a1 != a2')
		
def main():
	unittest.TestRunner(Test())
	
if __name__ == '__main__':
	unittest.main()
