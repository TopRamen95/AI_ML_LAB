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
    NP -> "John" | "Mary" | "Bob" | Det N | Det N PP | "Rahil" | "Moon" | "terrace"
    Det -> "a" | "an" | "the" | "my" | "his"
    N -> "man" | "dog" | "cat" | "telescope" | "park" | "Moon" | "terrace"
    P -> "in" | "on" | "by" | "with" | "from"
""")

# Create a parser
parser = nltk.ChartParser(grammar)

# Parse a sentence
sentence = "Rahil saw the Moon with the telescope from his terrace".split()
for tree in parser.parse(sentence):
    print(tree)
    tree.pretty_print()
