# Rock-paper-scissors-lizard-Spock template
import math
import random

# http://www.codeskulptor.org/#user20_VhMn9HJgnZjG5NZ.py

# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

def number_to_name(number):
    # fill in your code below
    if number == 0:
        return "rock"
    elif number == 1:
        return "Spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizard"
    elif number == 4:
        return "scissors"
        
    # convert number to a name using if/elif/else
    # don't forget to return the result!

    
def name_to_number(name):
    # fill in your code below
    if name == "rock":
        return 0
    elif name == "Spock":
        return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3
    elif name == "scissors":
        return 4
    # convert name to number using if/elif/else
    # don't forget to return the result!


def rpsls(name): 
    # fill in your code below

    # convert name to player_number using name_to_number
    player_number = name_to_number(name)
    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(0,5)
    # compute difference of player_number and comp_number modulo five
    dif_player = player_number % 5
    dif_comp = comp_number % 5
    # use if/elif/else to determine winner
    if dif_player > dif_comp:
        result = "Player wins!"
    elif dif_player < dif_comp:
        result = "Computer wins!"
    else:
        result = "Player and computer tie!"
    # convert comp_number to name using number_to_name
    print "Player uses %s" % name
    print "Computer uses %s" % number_to_name(comp_number)
    # print results
    print result
    print ""

    
# test your code
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric


