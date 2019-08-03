import sys
sys.path.append('C:\\Users\\K\\Desktop')
import LOTlib

from LOTlib.Grammar import Grammar

# Define a grammar object
# Defaultly this has a start symbol called 'START' but we want to call
# it 'EXPR'
grammar = Grammar(start='EXPR')

# Define some operations
grammar.add_rule('EXPR', '(%s + %s)', ['EXPR', 'EXPR'], 1.0)
grammar.add_rule('EXPR', '(%s * %s)', ['EXPR', 'EXPR'], 1.0)
grammar.add_rule('EXPR', '(float(%s) / float(%s))', ['EXPR', 'EXPR'], 1.0)
grammar.add_rule('EXPR', '(-%s)', ['EXPR'], 1.0)

# And define some numbers. We'll give them a 1/n^2 probability
for n in xrange(1, 10):
    grammar.add_rule('EXPR', str(n), None, 10.0 / n ** 2)



