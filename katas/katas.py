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