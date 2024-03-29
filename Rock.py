# Rock-paper-scissors-lizard-Spock template


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
import random

def name_to_number(name):
    # delete the following pass statement and fill in your code below
    #pass
    if name=="rock":
        return 0
    elif name=="Spock":
        return 1
    elif name=="paper":
        return 2
    elif name=="lizard":
        return 3
    else:
        return 4
    

    # convert name to number using if/elif/else
    # don't forget to return the result!


def number_to_name(number):
    # delete the following pass statement and fill in your code below
    #pass
    #i=random.randrange(0,4)
    i=number
    if i==0:
        return "rock"
    elif i==1:
        return "Spock"
    elif i==2:
        return "paper"
    elif i==3:
        return "lizard"
    elif i==4:
        return "scissors"
    else:
        return "wrong entry"


    
    
    
    # convert number to a name using if/elif/else
    # don't forget to return the result!
    

def rpsls(player_choice): 
    # delete the following pass statement and fill in your code below
    #pass
    
    # print a blank line to separate consecutive games

    # print out the message for the player's choice

    # convert the player's choice to player_number using the function name_to_number()

    # compute random guess for comp_number using random.randrange()

    # convert comp_number to comp_choice using the function number_to_name()
    
    # print out the message for computer's choice

    # compute difference of comp_number and player_number modulo five

    # use if/elif/else to determine winner, print winner message

    print ("\n")
    print "Player chooses %s" %player_choice
    player_number=name_to_number(player_choice)
    comp_number=random.randrange(0,4)
    print "Comptuer chooses ", number_to_name(comp_number)
    if (player_number==comp_number):
        print "Player and computer tie!"
    elif  (comp_number-player_number)%5 >2:
        print "Player wins!"
    elif  (comp_number-player_number)%5 <=2:
        print "Computer wins!"
    else:
        print "Wrong wrong!!!"
        
    
    
    
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric


