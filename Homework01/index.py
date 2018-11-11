import random
def name_to_number(name):
    if name == 'paper':
        return 2
    elif name == 'rock':
        return 0
    elif name == 'scissors':
        return 4
    elif name == 'Spock':
        return 1
    elif name == 'lizard':
        return 3
    else:
        return "not a valid choice"
def number_to_name(number):
    if number == 0:
        return 'rock'
    elif number == 1:
        return 'Spock'
    elif number == 2:
        return 'paper'
    elif number == 3:
        return 'lizard'
    elif number == 4:
        return 'scissors'
    else:
        return " inavlid choice "
def rpsls(player_choice): 
    print "" 
    print "player chooses", player_choice
    player_choice = name_to_number(player_choice)  
    comp_number = random.randrange(0,5)
    comp_number = number_to_name(comp_number)
    print "computer chooses", comp_number
    comp_number = name_to_number(comp_number)
    x = (comp_number - player_choice) % 5
    if x ==   1:
        print "computer wins"    
    elif x == 2:
        print "computer wins"    
    elif x == 3:
        print "player wins"   
    elif x == 4:
        print "player wins"
    else:
        print "Draw!"
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")