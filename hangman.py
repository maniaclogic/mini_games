import random

words = open('words.txt', 'r').readlines()
words = [word.replace('\n', ' ').replace('\"', ' ').strip() for word in words]

def play_hangman():
    hangman_word = words[random.randint(0, len(words) - 1)]
    underscore_array = ['_' for i in hangman_word]

    game_end = false

    while game_end == false:
        print(*underscore_array, sep=' ')

        player_move = input('Enter your guess! (A - Z)')

        
