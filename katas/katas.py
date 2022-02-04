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

# Learnings: numpy does this: "from numpy import mean as find_average" 

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