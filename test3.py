from spellchecker import SpellChecker

spell = SpellChecker()

# find those words that may be misspelled
misspelled = input("Say Something :")
misspelled=spell.unknown(misspelled.split(" "))

for word in misspelled:
    # Get the one `most likely` answer
    print(spell.correction(word))

    # Get a list of `likely` options
    print(spell.candidates(word))