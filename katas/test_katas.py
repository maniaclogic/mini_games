import pytest 
from katas import divisors, index_of_median

def test_divisors():
    assert divisors(1) == 1
    assert divisors(4) == 3
    assert divisors(5) == 2
    assert divisors(12) == 6
    assert divisors(30) == 8
    assert divisors(4096) == 13

def test_index_of_median():
    assert index_of_median([2, 3, 1]) == 0
    assert index_of_median([2, 14, 10]) == 2
