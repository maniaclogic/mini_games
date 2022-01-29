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

####################################################
# Given an array, find the index N where the sum of the 
# integers to the left of N is equal to the sum of the integers 
# to the right of N. If there is no index that would make this happen, return -1

def index_equal_sum(arr):
    result = [i for i, _ in enumerate(arr) if sum(arr[i:]) == sum(arr[:i + 1 ])]
    return result[0] if result else -1

########################################################################
# Write a function which calculates the average of the numbers in a given list.

def find_average(arr):
    return 0 if not arr else sum(arr)/len(arr)

# Learnings: numpy does this: "from numpy import mean as find_average" 

#################################################################
# Given an array of integers, return a new array with each value doubled.

def double_array(arr):
    return [i * 2 for i in arr]
