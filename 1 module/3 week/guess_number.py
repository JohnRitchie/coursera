import simpleguitk as simplegui
import random
import math


num_range = 100
secret_number = 0
count_of_guesses = 0


def new_game():
    print "New game!\nInput a number in range between 0 and", num_range-1

    global secret_number
    secret_number = random.randrange(0, num_range)

    global count_of_guesses
    count_of_guesses = int(math.ceil(math.log(num_range + 1, 2)))
    print count_of_guesses, "attempts left"


def range100():
    global num_range
    num_range = 100

    new_game()


def range1000():
    global num_range
    num_range = 1000

    new_game()


def input_guess(guess):
    try:
        guess = int(guess)
        print "Your guess is", guess
    except ValueError:
        print "Input must be a number!!!"
        return

    if not 0 <= guess < num_range:
        print "Number must be in range between 0 and", num_range-1
        return

    if guess == secret_number:
        print "You are a winner!\nSecret number is", secret_number
        return new_game()
    elif guess > secret_number:
        print "Lower!"
    elif guess < secret_number:
        print "Higher!"
    else:
        print "Something went wrong..."
        return new_game()

    global count_of_guesses
    count_of_guesses -= 1
    print count_of_guesses, " attempts left"

    if count_of_guesses <= 0:
        print "You have run out of attempts!"
        return new_game()
    else:
        print "Try more!"


frame = simplegui.create_frame("Guess the number", 300, 300)
frame.add_button("Range is [0,100)", range100, 100)
frame.add_button("Range is [0,1000)", range1000, 100)
frame.add_input("Input a number", input_guess, 100)

new_game()
frame.start()
