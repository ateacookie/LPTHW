from nose.tools import *
from ex49 import parser

def parse_sentence_test():
    x = parse_sentence([('verb', 'run'), ('direction', 'north')])
    assert_equal(x.subject, 'player')
    assert_equal(x.verb, 'run')
    assert_equal(x.object, 'north')
