# Play Hangman

import os
import random
import pickle
import sys


def start():
    os.system('cls')
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
        choice = input('(Y)es, (N)o, (EDIT) Word List, (HELP) or (QUIT).\n> ')
        choice = choice.lower()
        if choice == 'y':
            break
        elif choice == 'n':
            close()
        elif choice == 'help':
            help()
            input('\nPress (ENTER) to continue. ')
            start()
        elif choice == 'edit':
            edit()
        elif choice == 'quit':
            close()
        else:
            print(f'\nSorry, I didn\'t understand "{choice}".')
            print('Please enter one of the options provided in brackets:\n')
    os.system('cls')


def help():
    os.system('cls')
    print('\n### HELP/RULES ###')
    print('\nHangman is a game where you try to guess the letters in a secret word.')
    print('For every incorrect guess, a picture of a hanged stick man will be revealed.')
    print('When the stick man is hanged, the game is over.')
    print('To win, correctly guess the secret word and save the stick man from being hanged.')

    print('\nThis game is case-insensitive, so feel free to use all caps or lowercase.')
    print('Follow the letters or words in brackets for commands to continue.')

    print('\n### ADDING/REMOVING WORDS ###')
    print('\nYou can add or remove words before and after a new game using (EDIT).')
    print('From there you have the option of (A)dd, (R)emove or (P)eek at all the words.')
    print('Saving the word list is also available in this menu and when quitting.')
    print('New words will appear at the bottom of the list but chosen at random when playing.')

    print('\n### OTHER COMMANDS ###')
    print('\nYou can quit anytime with (QUIT)')
    print('And summon this help screen with (HELP).')


def edit():
    os.system('cls')
    print('### EDITING THE WORD LIST ###')
    print('\nWhat would you like to do?\n')
    print('(A)dd a new word to the list.')
    print('(R)emove an existing word.')
    print('(P)eek to see all current words.')
    print('(B)ack for previous menu')
    print('(S)ave word list now without quitting.')
    print('\n(HELP) for help or (QUIT) to exit.')
    choice = input('\n> ')
    choice = choice.lower()
    while choice != 'b':
        if choice == 'b':
            break
        # Add New Words
        if choice == 'a':
            print('### ADDING NEW WORDS ###')
            print('\n(B)ack to stop adding new words.')
            adding = input('What word would you like to add?\n> ')
            adding = adding.lower()
            if adding == 'b':
                break
            elif adding in words:
                words.append(adding)
                print(f'{adding} already exists in the list.')
            elif not adding.isalpha():
                print('Letters only please.')
            elif len(adding) < 1:
                print('That\'s not a word! Minimum requirement: Two characters.')
            elif adding not in words:
                words.append(adding)
                print(f'"{adding}" was added to the word list.\n')
        # Remove Existing Words
        elif choice == 'r':
            print('\n### REMOVING EXISTING WORDS ###')
            print('\n(B)ack to stop removing words. (CLEAR ALL) to remove all words.')
            removing = input('What word would you like to remove?\n> ')
            if removing.lower() == 'b':
                break
            elif removing.lower() in words:
                words.remove(removing)
                print(f'"{removing.lower()}" has been removed from the word list.')
            elif removing.lower() == 'clear all':
                print('\nAre you sure you want to remove all the words in the list?')
                print('This will include the default word list and any newly added words.')
                print('Changes will be applied during this game session.')
                print('To apply changes for the next session, save at the Editing Menu or Quit Menu.')
                delete = input('\nRemove all words? Type (YES) to confirm or press (ENTER) to cancel.\n> ')
                if delete.lower() == 'yes':
                    words.clear()
                    print('All words in the list have been removed.')
                else:
                    print('No changes have taken place.')
            else:
                print(f'"{removing}" doesn\'t exist in the word list. Check your spelling.')
        # See Full List of Current Words
        elif choice == 'p':
            # Print 10 words per line:
            print('\n### YOUR CURRENT WORD LIST: ###\n')
            for word in range(0, len(words), 10):
                print('\t'.join(words[word:word + 10]))
            input('\nPress (ENTER) to go to the Starting Screen. ')
            break
        elif choice == 's':
            save()
            input('\nPress (ENTER) to continue. ')
            break
        elif choice == 'help':
            help()
            input('\nPress (ENTER) to continue. ')
            break
        elif choice == 'quit':
            close()
        else:
            input(f'\nSorry, I did not understand "{choice}". (ENTER) to continue. ')
            break
    os.system('cls')
    start()
            

def save():
    try:
        with open('hangman_words.txt', 'wb') as f:
            pickle.dump(words, f)
            print('\nWord list saved.')
    except Exception as e:
        print(e)
        print('\nSorry, I couldn\'t figure out how to save your words.')


def close():
    print('\nWould you like to save any newly added words?')
    saving = input('Enter (Y)es, (N)o or (HELP).\n> ')
    saving = saving.lower()
    if saving == 'y':
       save()
    elif saving == 'n':
        pass
    elif saving == 'help':
        help()
        # Loop back to whether the user would like to save.
        close()
    else:
        print(f'\nSorry I do not understand "{saving}".')

    input('\nThanks for playing! Hit (ENTER) to exit.')
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
            guess = input('(SOLVE) for the solution, (HELP) for help, or (QUIT) to exit.\n> ')
            guess = guess.lower()

        if guess == 'solve':
            os.system('cls')
            print(hangman[len(guesses)])
            print(f"\nPrevious Incorrect Guesses: {' '.join(guesses)}")
            print(' '.join(blanks))
            print(f'\nThe word was:', ''.join(answer))
            break
        elif guess == 'help':
            help()
            input('\nPress (ENTER) to continue. ')
        elif guess == 'quit':
            close()
        elif len(guess) > 1:
            msg.append('That\'s too many characters! One at a time please.')
        elif not guess.isalpha():
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

words = [
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

# Check if an existing word list exists.
# If yes, update the default list.
# Else, use the default list.
try:
    with open('hangman_words.txt', 'rb') as f:
        print('A previously saved word list was found, would you like to use it?')
        custom = input('(Y)es or (N)o.\n> ')
        if custom.lower() == 'y':
            words = pickle.load(f)
            input('Saved word list loaded. Press (ENTER) to continue.\n')
        elif custom.lower() == 'n':
            input('Using default word list. Press (ENTER) to continue.\n')
except:
    print('Playing with default word list.\n')

# Playing Hangman:
start()
while True:
    ask()
    if len(words) == 0:
        print('There are no words in the list to choose from.')
        input('Press (ENTER) to go to the Editing Menu. ')
        edit()
    else:
        pass
    answer = list(random.choice(words))
    # OR answer = [letter for letter in random.choice(words)]
    blanks = ['_' for letter in answer]
    msg.clear()
    playing()
    guesses.clear()
    print('\nPlay again?')
