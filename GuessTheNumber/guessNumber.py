import simplegui
import random
import math

# initialize global variables used in your code here
num_range = 100

# helper function to start and restart the game
def new_game():
    """Initializes and restarts the game."""
    
    global secret_number
    global guess_remain
    
    #Set new secret number from given range
    secret_number = random.randrange(0, num_range)
    if num_range == 100:
        print "New game. Range is from 0 to 100"
    elif num_range == 1000:
        print "New game. Range is from 0 to 1000"
    
    #Calculate the total guesses allowed
    guess_remain = int(math.ceil(math.log(num_range, 2)))    
    print "Number of remaining guesses is", guess_remain


# define event handlers for control panel
def range100():
    """This is the event handler set range to 0 - 100 
    on button click."""
    
    global num_range
    num_range = 100
    print ""
    new_game()
    

def range1000():
    """This is the event handler set range to 0 - 1000 
    on button click."""
    
    global num_range
    num_range = 1000
    print ""
    new_game()
    
    
def input_guess(guess):
    """Processes the guess and takes appropriate actions. """
    global guess_remain
    print ""
    
    #Handle non-integer input
    try:
        guess_num = int(guess)
    except ValueError:
        print "This is not an int! Try again."
        print "You entered ", guess
        return None
    
    #Handle out of range input
    if guess_num < 0 or guess_num > num_range:
        print "Please enter guess in the range 0 -", num_range
        print "You entered ", guess
        return None
    
    #Print guessed number
    print "Guess was", guess_num
    
    #Decrease number of remaining guesses and print value
    guess_remain -= 1
    print "Number of remaining guesses is", guess_remain
    
    #Guiding message
    if guess_remain == 0 and guess_num != secret_number:
        print "You ran out of guesses. The number was", secret_number
        print ""
        new_game()
    else:
        if guess_num < secret_number:
            print "Higher!"
        elif guess_num > secret_number:
            print "Lower!"
        else:
            print "Correct!"
            print ""
            new_game()
            
            
# create frame
frame = simplegui.create_frame("Guess the number", 200, 200) 

# register event handlers for control elements and start frame
btn_100 = frame.add_button("Range: 0 - 100", range100, 150)
btn_1000 = frame.add_button("Range: 0 - 1000", range1000, 150)
inp = frame.add_input("Enter a guess:", input_guess, 150)

# call new_game 
new_game()

# start frame
frame.start()
