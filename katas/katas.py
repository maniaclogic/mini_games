## Count the number of divisors of a positive integer n.

def divisors(n):
    list_of_divs = [div for div in range(1, n+1) if n % div == 0]
    return len(list_of_divs)

# Learnings: sum and xrange are faster, so sum(1 for div in xrange(1, n+1) if n % div == 0) is better
# # also could have used lambda


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

def index_equal_sum(input_array):
    result = [i for i, _ in enumerate(input_array) if sum(input_array[i:]) == sum(input_array[:i + 1 ])]
    return result[0] if result else -1

########################################################################
# Write a function which calculates the average of the numbers in a given list.

def find_average(arr):
    return 0 if not arr else sum(arr)/len(arr)

# Learnings: numpy does this: "from numpy import mean as find_average" 