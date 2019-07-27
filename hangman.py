import random

words = open('words.txt', 'r').readlines()
words = [word.replace('\n', ' ').replace('\"', ' ').strip() for word in words]

def play_hangman():
    
