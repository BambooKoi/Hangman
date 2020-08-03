# Play hangman

import os
import random
import sys


def start():
        print('''
    +---+
    O   |
   /|\  |
   / \  |
       ===
H _ N G M _ N
            ''')
        print('Would you like to play Hangman?\n')


def ask():
    choice = ''
    while choice.lower() != 'n':
        choice = input('(Y)es or (N)o.\n> ')
        if choice.lower() == 'y':
            break
        elif choice.lower() == 'n':
            close()
        else:
            print(f'\nSorry, I didn\'t understand "{choice}".')
    os.system('cls')

def close():
    input('\nThanks for playing! Hit enter to exit.')
    sys.exit()

def playing():
    while True:
        os.system('cls')
        print(hangman[len(guesses)])
        # '(space for space)'.join() = print w/o brackets/quotes/commas
        print(' '.join(blanks))
        print(f"\nPrevious Incorrect Guesses: {' '.join(guesses)}")
        # Print promp message:
        print(f"\n{''.join(msg)}")
        msg.clear()

        if len(guesses) == len(hangman)-2:
            guess = input('This is your LAST guess.\n> ')
        else:
            print('Enter a letter to guess.')
            guess = input('Use "solve" to give up or "quit" to exit.\n> ')
            guess = guess.lower()

        if guess == 'solve':
            os.system('cls')
            print(hangman[len(guesses)])
            print(f"\nPrevious Incorrect Guesses: {' '.join(guesses)}")
            print(' '.join(blanks))
            print(f'\nThe word was:', ''.join(answer))
            break
        elif guess == 'quit':
            close()
        elif len(guess) > 1:
            msg.append('That\'s too many characters! One at a time please.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            promp = f'"{guess}" is not a letter.'
            msg.append(promp)
        elif (guess in guesses) or (guess in blanks):
            msg.append(f'You\'ve already guessed "{guess}". Choose another one.')
        elif guess not in answer:
            promp = f'There are no letter "{guess}"s in this word.'
            msg.append(promp)
            guesses.append(guess)
        else:
            for position, letters in enumerate(answer):  # 1
                if letters in guess:  # 2
                    blanks[position] = guess  # 3
            # 1. enumerate spits out the: index position & letter/word in that position.
            # 2. for any letters in answer than match our guess,
            # 3. use enumerate's position as index in blank and replace with guess

        # checks if player ran out of guesses
        if len(guesses) == len(hangman)-1:
            os.system('cls')
            print(f'{hangman[-1]}')
            print(' '.join(blanks))
            print('\nGame Over.')
            print('Player ran out of guesses.')
            print(f"\nPrevious Incorrect Guesses: {' '.join(guesses)}")
            print(f'\nThe word was:', ''.join(answer))
            break
        # checks if player found the answer
        elif blanks == answer:
            os.system('cls')
            print(hangman[len(guesses)])
            print(' '.join(blanks))
            print(f"\nPrevious Incorrect Guesses: {' '.join(guesses)}")
            print(f'\nCongratulations! You guessed the word:', ''.join(answer))
            break
        else:
            continue


hangman = ["""
    +---+
        |
        |
        |
       ===""", """
    +---+
    O   |
        |
        |
       ===""", """
    +---+
    O   |
    |   |
        |
       ===""", """
    +---+
    O   |
   /|   |
        |
       ===""", """
    +---+
    O   |
   /|\  |
        |
       ===""", """
    +---+
    O   |
   /|\  |
   /    |
       ===""", """
    +---+
    O   |
   /|\  |
   / \  |
       ==="""]

animals = [
    'ant', 'baboon', 'badger', 'bat', 'bear', 'beaver', 'camel', 'cat',
    'clam', 'cobra', 'cougar', 'coyote', 'crow', 'deer', 'dog', 'donkey',
    'duck', 'eagle', 'ferret', 'fox', 'frog', 'goat', 'goose', 'hawk', 'lion',
    'lizard', 'llama', 'mole', 'monkey', 'moose', 'mouse', 'mule', 'newt',
    'otter', 'owl', 'panda', 'parrot', 'pigeon', 'python', 'rabbit', 'ram',
    'rat', 'raven', 'rhino', 'salmon', 'seal', 'shark', 'sheep', 'skunk',
    'sloth', 'snake', 'spider', 'stork', 'swan', 'tiger', 'toad', 'trout',
    'turkey', 'turtle', 'weasel', 'whale', 'wolf', 'wombat', 'worm', 'zebra'
    ]

guesses = []
answer = []
blanks = []
msg = []

start()
while True:
    ask()
    answer = list(random.choice(animals))
    # OR answer = [letter for letter in random.choice(animals)]
    blanks = ['_' for letter in answer]
    msg.clear()
    playing()
    guesses.clear()
    print('\nPlay again?')
