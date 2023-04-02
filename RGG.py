# imports
import random

#global vars
global answer
global guess

# gen random number for easy mode, currently no other dificulties
answer = random.randint(0, 9)

# ask user for level to play
level = input("What level do you want to play? ")

# definition for level one
def level_one(): 
    global answer
    global guess

    guess = ""
    remaining_guesses = 5

    print("Amount of guesses for level one: " + str(remaining_guesses))
    
    while (guess != str(answer)) and (remaining_guesses != 0):
        guess = input("Guess: ")
    
        if guess == str(answer):
            print("Congratulations, you got the right for level one!")
            break
        else:
            remaining_guesses -= 1
    else:
        print("I am sorry, but you lost.")
        print("The right answer would have been: " + str(answer))


# definition for level two
def level_two():
    global answer
    global guess
    
    guess = ""
    remaining_guesses = 3

    print("Amount of guesses for level two: " + str(remaining_guesses))

    while (guess != str(answer)) and (remaining_guesses != 0):
        guess = input("Guess: ")

        if guess == str(answer):
            print("Congratulations, you got the right answer for level two!")
            break
        else:
            remaining_guesses -= 1
    else:
        print("I am sorry, but you lost.")
        print("The right answer would have been: " + str(answer))


# definition for level three
def level_three():
    global answer
    global guess

    guess = ""
    remaining_guesses = 1

    print("Amount of guesses for level 3: " + str(remaining_guesses))

    while (guess != str(answer)) and (remaining_guesses != 0):
        guess = input("Guess: ")

        if guess == str(answer):
            print("Congratulations, you got the right answer for level three!")
            break
        else:
            remaining_guesses -= 1
    else:
        print("I am sorry, but you lost.")
        print("The right answer would have been: " + str(answer))


# determine what level to play after users input
if (level == "one") or (level == "1"):
    print("You chose level one")
    level_one()
elif (level == "two") or (level == "2"):
    print("You chose level two")
    level_two()
elif (level == "three") or (level == "3"):
    print("You chose level three")
    level_three()
else:
    # declare the usage if user input is not one of the levels
    print("Usage:")
    print("'one' or '1' for the first level")
    print("'two' or '2' for the second level")
    print("'three' or '3' for the third level")
