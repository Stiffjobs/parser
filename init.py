import nltk
import sys

grammar = nltk.CFG.fromstring("""
    S -> NP VP
    S -> N VP Conj NP VP
    A -> Adj | Adv
    AP -> A | A AP 
    NP -> N | Det NP | AP NP | N PP | N PP Adv
    PP -> P NP
    VP -> V | V NP | V NP PP | V PP | Adv VP

    Adj -> "country" | "dreadful" | "enigmatical" | "little" | "moist" | "red"
    Adv -> "down" | "here" | "never"
    Conj -> "and" | "until"
    Det -> "a" | "an" | "his" | "my" | "the"
    N -> "armchair" | "companion" | "day" | "door" | "hand" | "he" | "himself"
    N -> "holmes" | "home" | "i" | "mess" | "paint" | "palm" | "pipe" | "she"
    N -> "smile" | "thursday" | "walk" | "we" | "word"
    P -> "at" | "before" | "in" | "of" | "on" | "to"
    V -> "arrived" | "came" | "chuckled" | "had" | "lit" | "said" | "sat"
    V -> "smiled" | "tell" | "were"
""")

parser = nltk.ChartParser(grammar)

def main():
    # If filename specified, read sentence from file
    if len(sys.argv) == 2:
        with open(sys.argv[1]) as f:
            s = f.read()

    # Otherwise, get sentence as input
    else:
        s = input("Sentence: ")

    # Convert input into list of words
    s = preprocess(s)
    trees = list(parser.parse(s))
    for tree in trees:
        tree.pretty_print()

def preprocess(sentence):
    return list(
        word.lower() for word in nltk.word_tokenize(sentence)
        if any(c.isalpha() for c in word)
    )

if __name__ == "__main__":
    main()