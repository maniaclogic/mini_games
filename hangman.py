import re

words = open('words.txt', 'r').readlines()

for w in words:
     w.replace(' ', '\t')
