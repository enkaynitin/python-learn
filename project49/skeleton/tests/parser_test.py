from nose.tools import *
from ex48 import lexicon
from ex49 import parser

def test_sentence_obj():
    s = parser.Sentence(('noun', 'bear'), ('verb', 'eat'), ('noun', 'door'))
    assert_equal(s.subject, 'bear')
    assert_equal(s.verb, 'eat')
    assert_equal(s.object, 'door')

def test_peek():
    word_list = lexicon.scan('princess')
    assert_equal(parser.peek(word_list), 'noun')
    assert_equal(parser.peek(None), None)

def test_match():
    word_list = lexicon.scan('princess')
    assert_equal(parser.match(word_list, 'noun'), ('noun', 'princess'))
    assert_equal(parser.match(word_list, 'stop'), None)
    assert_equal(parser.match(None, 'noun'), None)

def test_skip():
    word_list = lexicon.scan('bear eat door')
    assert_equal(word_list, [('noun', 'bear'), ('verb', 'eat'), ('noun', 'door')])
    parser.skip(word_list, 'noun')
    assert_equal(word_list, [('verb', 'eat'), ('noun', 'door')])

def test_parse_verb():
    word_list = lexicon.scan('it eat door')
    assert_equal(parser.parse_verb(word_list), ('verb', 'eat'))
    word_list = lexicon.scan('bear eat door')
    assert_raises(parser.ParserError, parser.parse_verb, word_list)

def test_parse_object():
    word_list = lexicon.scan('the door')
    assert_equal(parser.parse_object(word_list), ('noun', 'door'))
    word_list = lexicon.scan('the east')
    assert_equal(parser.parse_object(word_list), ('direction', 'east'))
    word_list = lexicon.scan('the it')
    assert_raises(parser.ParserError, parser.parse_object, word_list)

def test_parse_subject():
    word_list = lexicon.scan('eat door')
    subj = ('noun', 'bear')
    s = parser.parse_subject(word_list, subj)


def test_parse_sentence():
    word_list = lexicon.scan('the bear eat door')
    s = parser.parse_sentence(word_list)
    word_list = lexicon.scan('in eat door')
    s = parser.parse_sentence(word_list)
    word_list = lexicon.scan('north eat door')
    assert_raises(parser.ParserError, parser.parse_sentence, word_list)

def test_unknown_words():
    word_list = lexicon.scan('the bear eat door')
    s = parser.parse_sentence(word_list)

def test_numbers():
    word_list = lexicon.scan('the bear eat door')
    s = parser.parse_sentence(word_list)    
    
    
