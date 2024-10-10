import nltk
from nltk import CFG
from nltk.tree import Tree

# Print the version of nltk
print(nltk.__version__)

# Define the grammar
grammar = CFG.fromstring("""
    S -> NP VP
    VP -> V NP | V NP PP
    PP -> P NP
    V -> "saw" | "ate" | "walked"
    NP -> "John" | "Mary" | "Bob" | Det N | Det N PP
    Det -> "a" | "an" | "the" | "my"
    N -> "man" | "dog" | "cat" | "telescope" | "park" | "Moon" | "Terrace"
    P -> "in" | "on" | "by" | "with" | "From"
""")

# Create a parser
parser = nltk.ChartParser(grammar)

# Parse a sentence
sentence = "John saw the man in the park".split()
for tree in parser.parse(sentence):
    print(tree)
    tree.pretty_print()
