import random

global answer
global guess

answer = random.randint(0, 9)

level = input("What level do you want to play? ")
    

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


if level == "one":
    print("You chose level one")
    level_one()

elif level == "two":
    print("You chose level two")
    level_two()
elif level == "three":
    print("You chose level three")
    level_three()
else:
    print("Usage: 'one' for level one, 'two' for level two, 'three' for level three")

#level_one()
#level_two()
#level_three()