"""Word Finder: finds random words from a dictionary."""

import random

class WordFinder:
#     ...

    def __init__(self, location="words.txt", data="r"):
        """gather all the words from the file and counts them up"""
        filepath = open(location)
        self.chosen_word = self.convert(filepath)
        print(f"there is {len(self.chosen_word)+1} words to read from")            

        
    def convert(self, filepath):
        """Convert the list of words in the file into a list"""

        return [word.strip() for word in filepath]
    
    def random(self):
        """Return a random word from the list"""
        return random.choice(self.chosen_word)
    

        
class SpecialWordFinder(WordFinder):

    def convert(self, filepath):
        """Convert the list of words in the file into a list without blanks nor comments"""

        return [word.strip() for word in filepath if word.strip() and not word.startswith("#") and not word.startswith("/")]