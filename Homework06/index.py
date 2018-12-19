#

import simplegui
import random

# load card sprite - 949x392 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
score = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self.cards = []
        # pass    # create Hand object

    def __str__(self):
        string = "Hand contains"
        i = 0
        while(i < len(self.cards)):
            string = string + "" + self.cards[i].suit + self.cards[i].rank
            i = i + 1
        return string
        
    def add_card(self, card):
        self.cards.append(card)

    def get_value(self):
        i = 0
        aceCount = 0
        value = 0
        while(i < len(self.cards)):
            value = value + VALUES[self.cards[i].rank]
            if(self.cards[i].rank == "A"):
                aceCount += 1
            i = i + 1
            
        if(aceCount > 0):
            if(21 - value >= 10):
                value = value + 10
        return value
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        # pass  # compute the value of the hand, see Blackjack video
   
    def draw(self, canvas, pos):
        #pass  # draw a hand on the canvas, use the draw method for cards
        i=0
        while(i<len(self.cards)):
            self.cards[i].draw(canvas, [pos[0] + CARD_CENTER[0] + i * (30 + CARD_SIZE[0]), pos[1] + CARD_CENTER[1]])
            i=i+1
       
 
 
        
# define deck class 
class Deck:
    def __init__(self):
        self.cards = []
        for i in SUITS:
            for j in RANKS:
                self.cards.append(Card(i, j))
                print i,j

    def shuffle(self):
        # shuffle the deck
        random.shuffle(self.cards) 

    def deal_card(self):
        return self.cards.pop()
    
    def __str__(self):
        string = "Deck contains"
        i = 0
        while(i < len(self.cards)):
            string = string + " " + self.cards[i].suit + self.cards[i].rank
            i = i + 1
        return string



#define event handlers for buttons
def deal():
    global outcome, in_play, player, dealer, d, score

    # your code goes here
    d = Deck()
    d.shuffle()
    outcome = ""
    
    player = Hand()
    player.add_card(d.deal_card())
    player.add_card(d.deal_card())
    
    #print player
    
    dealer = Hand()
    dealer.add_card(d.deal_card())
    dealer.add_card(d.deal_card())
    
    #print dealer
    if in_play:
        score -=1
        outcome = "You lose."
    in_play = True

def hit():
    global in_play, player, d, score, outcome
 
    # if the hand is in play, hit the player
    if in_play:
        player.add_card(d.deal_card())
        
   
    # if busted, assign a message to outcome, update in_play and score
    if player.get_value() > 21:
            outcome = "Bust"
            score -= 1
            in_play = False
    
    
def stand():
    global dealer, player, d, in_play, score, outcome
   
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    # assign a message to outcome, update in_play and score
    if in_play:
        while dealer.get_value() < 17:
            dealer.add_card(d.deal_card())
        if player.get_value() > 21:
            outcome = "BUST"
        else:
            if dealer.get_value() > 21:
                outcome = "Dealer BUST"
                score += 1
            elif dealer.get_value() < player.get_value():
                outcome = "You win"
                score += 1
            else:
                outcome = "You lose"
                score -= 1
        in_play = False

    

# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    global in_play, dealer, player
    
    canvas.draw_text("Blackjack", [225, 50], 35, "Black")
    canvas.draw_text("Your Score " + str(score), [440,170], 25, "Black")
    canvas.draw_text("Dealer", [80, 170], 25, "Black")
    canvas.draw_text("Ivan Millionaire", [80, 370], 25, "Black")
    
    color="Black"
    if(outcome=="You lose."):
        color="Red"
    else:
        color="White"
    canvas.draw_text(outcome, [200, 170], 25, color)
    
 
    dealer.draw(canvas, [60, 170])
    if in_play:
        canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, [60 + CARD_BACK_SIZE[0], 170 + CARD_BACK_SIZE[1]], CARD_SIZE)
    else:
        dealer.cards[0].draw(canvas, [60 + CARD_CENTER[0], 170 + CARD_CENTER[1]])
    
    
    if in_play:
        canvas.draw_text("Hit or stand?", [300, 370], 25, "Black")
    else:
        canvas.draw_text("New deal?", [300, 370], 25, "Black")
    
    player.cards[0].draw(canvas, [60 + CARD_CENTER[0], 370 + CARD_CENTER[1]])
    player.draw(canvas, [60, 370])

    
    
    #card = Card("S", "A")
    #card.draw(canvas, [300, 300])


# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()