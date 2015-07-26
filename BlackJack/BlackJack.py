# Mini-project #6 - Blackjack
#http://www.codeskulptor.org/#user40_3Z8oUAhKPYSVDFg.py
import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
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
        global in_play
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        if in_play and pos == [100, 420]:
            canvas.draw_image(card_back, CARD_CENTER, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        else:
            canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        # create Hand object
        self.cards = []

    def __str__(self):
        # return a string representation of a hand
        str =  "Hand contains"
        for card in self.cards:
            str += " " + card.__str__()
        return str

    def add_card(self, card):
        # add a card object to a hand
        self.cards.append(card)

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        # compute the value of the hand, see Blackjack video
        value = 0
        rank = ''
        ace_found = False
        for card in self.cards:
            rank = card.get_rank()
            if rank == 'A':
                ace_found = True
            value += VALUES[rank]
        if ace_found and (10 + value) <= 21:
            value += 10
        return value 
   
    def draw(self, canvas, pos):
        for card in self.cards:
            card.draw(canvas, pos)
            pos[0] += CARD_SIZE[0] + 5
 
        
# define deck class 
class Deck:
    def __init__(self):
        # create a Deck object
        self.cards = []
        for suit in SUITS:
            for rank in RANKS:
                self.cards.append(Card(suit, rank))

    def shuffle(self):
        # shuffle the deck 
        # use random.shuffle()
        random.shuffle(self.cards)

    def deal_card(self):
        # deal a card object from the deck
        return self.cards.pop()
    
    def __str__(self):
        # return a string representing the deck
        str =  "Deck contains"
        for card in self.cards:
            str += " " + card.__str__()
        return str



#define event handlers for buttons
def deal():
    global outcome, in_play, deck, player, dealer, score
    if in_play:
        score -= 1 
        outcome = "Player has busted. Dealer won. Hand dealt."
        winner = "Dealer"
    else:
        outcome = "New game started. Hit or stand?"
    deck = Deck()
    deck.shuffle()
    player = Hand()
    dealer = Hand()
    player.add_card(deck.deal_card())
    player.add_card(deck.deal_card())
    dealer.add_card(deck.deal_card())
    dealer.add_card(deck.deal_card())    
    in_play = True
    
def hit():
    global player, deck, in_play, outcome, winner, score
 
    # if the hand is in play, hit the player
    if in_play:
        player.add_card(deck.deal_card())   
        # if busted, assign a message to outcome, update in_play and score
        if player.get_value() > 21:
            outcome = "Player has busted. Dealer won. New deal?"
            winner = "Dealer"
            score -= 1
            in_play = False
        else:
            outcome = "Hit or stand?"
    else:
        outcome = "Game ended. " + winner + " won. New deal?"

def stand():
    global in_play, dealer, player, outcome, winner, score
    
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    if not in_play:
        outcome = "Game ended. " + winner + " won. New deal?"
    else:
        while(dealer.get_value() < 17):
            dealer.add_card(deck.deal_card()) 
        # assign a message to outcome, update in_play and score
        in_play = False
        if dealer.get_value() > 21 or dealer.get_value() < player.get_value():
            outcome = "Dealer has busted. Player won. New deal?"
            winner = "Player"
            score += 1
        elif dealer.get_value() >= player.get_value():
            outcome = "Player has busted. Dealer won. New deal?"
            winner = "Dealer"
            score -= 1

# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    global player, dealer, outcome, score
    player.draw(canvas, [100, 220])
    dealer.draw(canvas, [100, 420])
    canvas.draw_text("Blackjack", [230, 55], 40, 'Yellow')
    canvas.draw_text(outcome, [50, 130], 20, 'White')
    canvas.draw_text("Score: " + str(score), [440, 130], 30, 'White')
    canvas.draw_text("Player", [130, 200], 30, 'White')
    canvas.draw_text("Dealer", [130, 400], 30, 'White')
    


# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()


# remember to review the gradic rubric