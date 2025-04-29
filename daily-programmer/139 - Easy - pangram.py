"""
Challenge #139  [Easy] Pangrams

Description

Wikipedia has a great definition for Pangrams: "A pangram or holoalphabetic sentence for a given alphabet is a sentence using every letter of the alphabet at least once." A good example is the English-language sentence "The quick brown fox jumps over the lazy dog"; note how all 26 English-language letters are used in the sentence.

Your goal is to implement a program that takes a series of strings (one per line) and prints either True (the given string is a pangram), or False (it is not).

Solution
Solution by Sebastian David Lees (sebastian@incerto.net)
"""

def isPangram(phrase):
    phrase = phrase.lower()
    phrase = set(phrase) - {".",",",":",";"," ","  ","\n","-","%","&","~","#",
                            "/","?"}
    alphabet = {"a","b","c","d","e","f","g","h","i","j","k","l","m","n","o",
                "p","q","r","s","t","u","v","w","x","y","z"}
                
    return phrase == alphabet

#Test
print isPangram("How do you do")
print isPangram("The quick brown fox jumps over the lazy dog")
