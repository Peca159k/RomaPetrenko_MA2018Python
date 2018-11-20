import simplegui
import random
import math

secret = 0
user_guess = 0
num_guesses = 0

def range100():
    print ("A new has started with a range from 0 to 100")
    print ("You have 7 guesses")
    global secret
    secret = random.randrange(0,100)
    global num_guesses
    num_guesses = 7
    
def range1000():
    print ("A new has started with a range from 0 to 1000")
    print ("You have 10 guesses ")
    global secret
    secret = random.randrange(0,1000)
    global num_guesses
    num_guesses = 10
    
def input_guess(user_input):
    global user_guess
    global num_guesses
    user_guess=int(user_input)
    if user_guess==secret:
        print "Your guess = ",user_guess
        print "Correct"
        range100()
    elif user_guess<secret:
        print "Your guess = ",user_guess
        print "high"
        num_guesses = num_guesses - 1
        print "remaning guesses", num_guesses
        print ""
        if num_guesses==0:
            print "The end."
            range100()
    elif user_guess>secret:
        print "Your guess = ",user_guess
        print "low"
        num_guesses = num_guesses - 1
        print "remaning guesses", num_guesses
        print ""
        if num_guesses == 0:
            print "The end."

            print ""
            range100()
    

frame = simplegui.create_frame("Guess the number",200,200)
frame.add_button('Range [0, 100]',range100,200)
frame.add_button('Range [0, 1000]', range1000,200)
frame.add_input('Enter guess', input_guess, 100)

frame.start()