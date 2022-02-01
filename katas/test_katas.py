import pytest 
from katas import divisors, index_of_median, pangram, index_equal_sum, find_average, double_array, dig_pow

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


def test_pangram():
    assert pangram("The quick brown fox jumps over the lazy dog") == True
    assert pangram("Cwm fjord bank glyphs vext quiz is a pangram") == True
    assert pangram("Hello World") == False

def test_index_equal_sum():
    assert index_equal_sum([1,2,3,4,3,2,1]) == 3
    assert index_equal_sum([1,100,50,-51,1,1]) == 1
    assert index_equal_sum([1,2,3,4,5,6]) == -1
    assert index_equal_sum([20,10,30,10,10,15,35]) == 3

def test_find_average():
    assert find_average([1, 2, 3]) == 2
    assert find_average([1, 3, 5]) == 3

def test_double_array():
    assert double_array([1, 2, 3]) == [2, 4, 6]
    assert double_array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
    assert double_array([0, 0, 0]) == [0, 0, 0]

def test_dig_power():
    assert dig_pow(89, 1) == 1
    assert dig_pow(92, 1) == -1
    assert dig_pow(695, 2) == 2
    assert dig_pow(46288, 3) == 51