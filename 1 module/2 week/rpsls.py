import random


def name_to_number(name):
    if name == 'rock':
        number = 0
    elif name == 'Spock':
        number = 1
    elif name == 'paper':
        number = 2
    elif name == 'lizard':
        number = 3
    elif name == 'scissors':
        number = 4
    else:
        return "Wrong name!"

    return number


def number_to_name(number):
    if number == 0:
        name = 'rock'
    elif number == 1:
        name = 'Spock'
    elif number == 2:
        name = 'paper'
    elif number == 3:
        name = 'lizard'
    elif number == 4:
        name = 'scissors'
    else:
        return "Wrong number!"

    return name


def rpsls(player_choice):
    print

    print "Player's choice is " + player_choice

    player_number = name_to_number(player_choice)

    comp_number = random.randrange(0, 5)

    comp_choice = number_to_name(comp_number)

    print "Computer's choice is " + comp_choice

    result = (player_number - comp_number) % 5

    if 1 <= result <= 2:
        print 'Player wins!'
    elif 3 <= result <= 4:
        print 'Computer wins!'
    elif result == 0:
        print 'Player and computer tie!'
    else:
        print 'Something went wrong!'


# tests
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")
rpsls("rock")
