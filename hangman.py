#importing the time module
import time

#importing the random module
import random
from turtle import bgcolor

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m' 
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m' 
    ENDC = '\033[0m'
    BOLD = '\033[1m'

#Welcome the user
name = input (f"{bcolors.OKBLUE}What is your name?{bcolors.ENDC} ")

print("-"*40)
print("Hello, " + bcolors.OKBLUE + bcolors.ENDC + "\nTime to play Hangman!" )
print("-"*40+"\n")

# wait for 1 second
time.sleep(1)

print(f"Start guessing...\n{bcolors.WARNING}Hint{bcolors.ENDC}:It is a fruit")
time.sleep(0.5)

someWords = ''' apple banana mango strawberry orange grape pineapple apricot lemon coconut watermelon cherry papaya lychee muskemelon'''

someWords = someWords. split(' ')

# randomly choose a secret word from our "somewords" list
word = random.choice(someWords)

#creates an variable with an empyt value
guesses = ''

# determines the number of turns
turns = 5

#create a while loop
# checrs if the turn are more than zero
while turns > 0:
    #make a counter that starts with zero
    failed = 0
    # for every character in secret_word
    for char in word:
         # see if the character is in the player guess
        if char in guesses:
            # print then out the character
            print(bcolors.OKGREEN + char + bcolors.ENDC, end=' ')
        else:
            # if not found, print a dash
            print(f"{bcolors.OKCYAN}_{bcolors.ENDC}", end=' ')
            # and increase the failed counter with one
            failed += 1
    # if failed is equal to zero
    # print you won
    if failed == 0:
        print(f"{bcolors.OKGREEN}\n\n"+"#"*40+f"{bcolors.ENDC}")
        print(f"{bcolors.OKGREEN}\t\tYou won{bcolors.ENDC}")
        print(f"{bcolors.OKGREEN}#"*40+f"{bcolors.ENDC}")
    # exit the script
        break


    # ask the user to guess a character
    guess = input(f"\n\n{bcolors.BOLD+bcolors.OKBLUE}Guess a character: {bcolors.ENDC}")

    # validation of the guess
    if not guess.isalpha():
        print(f'{bcolors.WARNING}Enter only a LETTER{bcolors.ENDC}')
        continue
    elif len(guess) > 1:
        print(f'{bcolors.WARNING}Enter only a SINGLE letter{bcolors.ENDC}')
        continue
    elif guess in guesses:
        print(f'{bcolors.WARNING}You have already guessed that letter{bcolors.ENDC}')
        continue
    
    # see the player guess to guesses
    guesses += guess

    # if the guess is not found in the secret word
    if guess not in word:
        # turn the counter decrease with 1(now 9)
        turns -= 1
        # print wrong
        print(f"{bcolors.FAIL}\nWrong{bcolors.ENDC}")
        # how many turns are left
        print(f"you have{bcolors.HEADER}",+ turns ,f"{bcolors.ENDC}more guesses\n")

        # if the turns are equal to the zeero 
        if turns == 0:
            # print you loose
            print(f"\n{bcolors.FAIL}\n\n" + "#"*40 + f"{bcolors.ENDC}")
            print(f"\n{bcolors.FAIL}\t\tYou Loose{bcolors.ENDC}") 
            print(f"\n{bcolors.FAIL}#"*40 + f"{bcolors.ENDC}")

print("The word was:", bcolors.OKGREEN + word + bcolors.ENDC)