# test_listFunctions.py

import pytest

from listFunctions import onlyEvenIntegers

def test_onlyEvenIntegers_1():
    assert onlyEvenIntegers([2,5,7,4])==[2,4]

def test_onlyEvenIntegers_2():
    assert onlyEvenIntegers([5,7,9])==[]

def test_onlyEvenIntegers_3():
    assert onlyEvenIntegers([5,7,9,"potato",True,4,1])==[4]
