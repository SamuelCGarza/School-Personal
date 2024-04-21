"""
File: recognizer.py

A grammar checker for sentences in a subset of English
defined by the following grammar rules:

sentence = nounphrase verbphrase
nounphrase = article noun
verbphrase = verb nounphrase prepositionalphrase

The parts of speech are nouns, verbs, articles,
and prepositions.

Inputs: purported sentences
Outputs: Ok, grammatically correct or
Not ok, grammatically incorrect
"""

articles = ("A", "THE")

nouns = ("BOY", "GIRL", "BAT", "BALL")

verbs = ("HIT", "SAW", "LIKED")

prepositions = ("WITH", "BY")

# sentence = nounphrase verbphrase
def sentence(words):
    """Returns True if the words form
    a sentence or False otherwise."""
    return nounPhrase(words) and verbPhrase(words)

# nounphrase = article noun
def nounPhrase(words):
    """Returns True if the first two words
    form a noun phrase or False otherwise."""
    if len(words) < 2:
        return False
    else:
        article = words.pop(0)
        noun = words.pop(0)
        return article in articles and noun in nouns

# verbphrase = verb nounphrase prepositionalphrase
def verbPhrase(words):
    """Returns True if the words form
    a verb phrase or False otherwise."""
    if len(words) == 0:
        return False
    else:
        verb = words.pop(0)
        return verb in verbs and nounPhrase(words) and \
               prepositionalPhrase(words)

# prepositionalphrase = preposition nounphrase
def prepositionalPhrase(words):
    """Returns True if the words form
    a prepositional phrase or False otherwise."""
    if len(words) == 0:
        return False
    else:
        preposition = words.pop(0)
        return preposition in prepositions and nounPhrase(words)

def main():
    """Tests inputs for grammatical correctness until the
    user presses return."""
    while True:
        userInput = input("Enter a sentence or press return to quit: ")
        if userInput == "":
            return
        else:
            words = userInput.upper().split()
            if sentence(words):
                print("Ok, grammatically correct")
            else:
                print("Not ok, grammatically incorrect")

if __name__ == "__main__":
    main()

