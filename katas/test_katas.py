import pytest 
from katas import divisors

def test_divisors():
    assert divisors(1) == 1
    assert divisors(4) == 3
    assert divisors(5) == 2
    assert divisors(12) == 6
    assert divisors(30) == 8
    assert divisors(4096) == 13