# test_stringFunctions.py

from stringFunctions import *


def test_countVowels_Hello():
    assert computeVowelCountDict("Hello")=={'e':1, 'o':1}
 
def test_countVowels_Potato():
    assert computeVowelCountDict("Potato")=={'a':1, 'o':2}

def test_countVowels_University():
    assert computeVowelCountDict("University")=={'e': 1, 'u':1, 'i':2}

