# test_listFunctions.py

import pytest

from listFunctions import onlyEvenIntegers

def test_onlyEvenIntegers_1():
    assert onlyEvenIntegers([2,5,7,4])==[2,4]

def test_onlyEvenIntegers_2():
    assert onlyEvenIntegers([5,7,9])==[]

def test_onlyEvenIntegers_3():
    assert onlyEvenIntegers([5,7,9,"potato",True,4,1])==[4]

from listFunctions import squareEachInteger

def test_squareEachInteger_1():
    mylist = [2,3,4]
    squareEachInteger(mylist)
    assert mylist == [4,9,16]

def test_squareEachInteger_2():
    mylist = [2,"potato",4.5, 7]
    squareEachInteger(mylist)
    assert mylist == [4, "potato", 4.5, 49]

from listFunctions import truncateEachString

def test_truncateEachString_6():
    myList = [2,4,"Very long string that goes on and on",
              "short", "very long again way too long",
              "tiny"]
    truncateEachString(myList,6)
    assert myList==[2,4,"Very l","short","very l","tiny"]

def test_truncateEachString_1():
    myList = [2,4,"Very long string that goes on and on",
              "short", "very long again way too long",
              "tiny"]
    truncateEachString(myList,1)
    assert myList==[2,4,"V","s","v","t"]
