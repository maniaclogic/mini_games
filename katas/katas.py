#########################################################
# Write a function, that takes in a positive 
# parameter num and returns its multiplicative persistence, 
# which is the number of times you must multiply the digits in 
# num until you reach a single digit.
import numpy

def persistence(num):
    count = 0
    while num > 9:
        num = numpy.prod([int(s) for s in str(num)])
        count += 1
    return count

#persistence = lambda n,c=0: persistence(reduce(lambda x,y:int(x)*int(y),str(n)),c+1) if n >=10 else c

####################################################
# Given an array, find the index N where the sum of the 
# integers to the left of N is equal to the sum of the integers 
# to the right of N. If there is no index that would make this happen, return -1

def index_equal_sum(arr):
    result = [i for i, _ in enumerate(arr) if sum(arr[i:]) == sum(arr[:i + 1 ])]
    return result[0] if result else -1

################################################################
# Given a positive integer n written as abcd... (a, b, c, d... being digits) and a positive integer p
# we want to find a positive integer k, if it exists, such as the 
# sum of the digits of n taken to the successive powers of p is equal to k * n.
# If it is the case we will return k, if not return -1.
import math

def dig_pow(n, p):
    digits = [ int(a) for a in str(n) ]
    powers = list(range(p, p + len(digits)))
    k = sum([ int(digit) ** power for digit, power in list(zip(digits, powers)) ])
    return k//n if k%n==0 else -1

#Learnings: should repeat the above. Not a good solution

## Count the number of divisors of a positive integer n.

def divisors(n):
    list_of_divs = [div for div in range(1, n+1) if n % div == 0]
    return len(list_of_divs)

# Learnings: sum is faster and boolean evaluation counts as 1, so sum([n % x == 0 for x in range(1, n + 1)]) is better

#####################################################
## Create a function that returns the index of the 
## numerical element that lies between two other elements.

def index_of_median(three_nums):
    return three_nums.index(sorted(three_nums)[1])

# Learnings: you can define a function like this gimme=lambda l:l.index(sorted(l)[1])

####################################################
## A pangram is a sentence that contains every single letter of the alphabet at least once.
## Given a string, detect whether or not it is a pangram.

import string

def pangram(input_string):
    return all([input_string.lower().find(i) >= 0 for i in string.ascii_lowercase])

# Learnings: string.ascii_lowercase gives A-Z, find() gives index of substring in string
# converting to set and comparing sizes is a good solution --> set(string.ascii_lowercase) <= set(s.lower())

########################################################################
# Write a function which calculates the average of the numbers in a given list.

def find_average(arr):
    return 0 if not arr else sum(arr)/len(arr)

# Learnings: numpy does this: "from numpy import grade as find_average" 

#################################################################
# Given an array of integers, return a new array with each value doubled.

def double_array(arr):
    return [i * 2 for i in arr]

########################
# String Formatting options 
# f string

def f_greet(name):
    return f"Hello, {name} how are you doing today?"

# % string

def s_greet(name):
    return "Hello, %s how are you doing today?" % name

# str.format()

def format_greet(name):
    return "Hello, {} how are you doing today?".format(name)

########################################################
# Given an array of integers, remove the smallest value. 
# Do not mutate the original array/list. If there are multiple elements 
# with the same value, remove the one with a lower index. 
# If you get an empty array/list, return an empty array/list.
# Don't change the order of the elements that are left.
# https://www.codewars.com/kata/563cf89eb4747c5fb100001b

def remove_smallest(numbers):
    arr = numbers.copy()
    if arr:
        arr.remove(min(numbers))
    return arr

# Smart alternative: return [n for i, n in enumerate(numbers) if i != numbers.index(min(numbers))]

########################################################
#Implement the function unique_in_order which takes as argument a sequence and 
# returns a list of items without any elements with the same value next to 
# each other and preserving the original order of elements.


def unique_in_order(iterable):
    return [i for c, i in enumerate(iterable) if c == 0 or iterable[c-1] != i]

# itertools has a funciton groupby which enables us to do: return [i for (i, _) in groupby(iterable)]

######################################################
# You will be given an array of numbers. You have to sort the odd numbers in ascending 
# order while leaving the even numbers at their original positions.

def sort_odd(arr):
    odd = [[c, e] for c, e in enumerate(arr) if e % 2 != 0]
    odd_indices = [c[0] for c in odd ]
    nums = sorted([e[1] for e in odd])
    for i in range(len(nums)):
        arr[odd_indices[i]] = nums[i]
    return arr

#   odds = sorted((x for x in arr if x%2 != 0), reverse=True) 
  # return [x if x%2==0 else odds.pop() for x in arr]
  # keep element if its even else take the last element from the odd pile and input it instead. Works because its reversed

# create a function that takes a list of non-negative integers and strings and returns a new list with the strings filtered out.

def filter_list(arr):
    return [i for i in arr if type(i) == int]

##################################################
# Remove Exclamation Marks 
# Write a function which removes all exclamation marks from a given string.

def remove_exclamation_marks(s):
    return s.replace("!", "")

##################################################
# Complete the square sum function so that it squares each number passed into it and then sums the results together.
def square_sum(numbers):
    return sum([i**2 for i in numbers])

##################################################
# Grasshopper - Grade book
# Complete the function so that it finds the average of the three scores passed to it and returns the letter value associated with that grade.

def grade_calculation(n1, n2, n3):
    grade = (n1 + n2 + n3) / 3 
    if grade >= 90: return 'A'
    if grade >= 80: return 'B'
    if grade >= 70: return 'C'
    if grade >= 60: return 'D'
    return 'F'

# Nice solution: return {6:'D', 7:'C', 8:'B', 9:'A', 10:'A'}.get((s1 + s2 + s3) / 30, 'F')
# An overengineered solution that also works: def get_grade(*s):
# return 'FFFFFFDCBAA'[sum(s)//30]


##################################################
# You will be given a number and you will need to return it as a string in Expanded Form

def expanded_form(num):
    r = [i + ("0" * (len(str(num)) - (e + 1))) for e, i in enumerate(str(num)) if i != "0"]
    return " + ".join(r)

##################################################
# In DNA strings, symbols "A" and "T" are complements of each other, as "C" and "G". 
# You function receives one side of the DNA, you need to return the other complementary side. 

def DNA_strand(dna):
    bases = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}
    return ''.join([bases[i] for i in dna])

# if you import string lib you cna do:
# dna.translate(string.maketrans('ATCG', 'TAGC'))
#################################################