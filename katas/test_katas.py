import pytest 
from katas import *


def test_persistence():
    assert persistence(39) == 3
    assert persistence(999) == 4
    assert persistence(4) == 0 #return 0 upon already single digit

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

def test_f_greet():
    assert f_greet("Kat") == "Hello, Kat how are you doing today?"
def test_s_greet():
    assert s_greet("Lisa") == "Hello, Lisa how are you doing today?"
def test_format_greet():
    assert format_greet("Lola") == "Hello, Lola how are you doing today?"

def test_remove_smallest():
    assert remove_smallest([1,2,3,4,5]) == [2,3,4,5]
    assert remove_smallest([5,3,2,1,4]) == [5,3,2,4]
    assert remove_smallest([2,2,1,2,1]) == [2,2,2,1]

def test_unique_in_order():
    assert unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
    assert unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
    assert unique_in_order([1,2,2,3,3])       == [1,2,3]
    assert unique_in_order('AA')              == ['A']
    assert unique_in_order('A')               == ['A']

def test_sort_odd():
    assert sort_odd([7, 1])  ==  [1, 7]
    assert sort_odd([5, 8, 6, 3, 4])  ==  [3, 8, 6, 5, 4]
    assert sort_odd([9, 8, 7, 6, 5, 4, 3, 2, 1, 0])  ==  [1, 8, 3, 6, 5, 4, 7, 2, 9, 0]

def test_filter_list():
    assert filter_list([1,2,'a','b']) == [1,2]
    assert filter_list([1,'a','b',0,15]) == [1,0,15]
    assert filter_list([1,2,'aasf','1','123',123]) == [1,2,123]

def test_remove_exclamation_marks():
    assert remove_exclamation_marks("HALLO!") == "HALLO"
    assert remove_exclamation_marks("!Hall!o!") == "Hallo"
    assert remove_exclamation_marks("@#%!^*#") == "@#%^*#"
    assert remove_exclamation_marks("Hallo") == "Hallo"
    assert remove_exclamation_marks("!!!") == ""
    assert remove_exclamation_marks("") == ""