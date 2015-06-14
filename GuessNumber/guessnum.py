print ("Please think of a number between 0 and 100!")
low = 0
high = 100
guess = 50
inp = ''
while True:
    print "Is your secret number " + str(guess) + "?"
    inp = raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    if (inp == 'c'):
        print "Game over. Your secret number was: " + str(guess),
        break;
    elif (inp == 'l'):
        low = guess
    elif (inp == 'h'):
        high = guess
    else:
        print "Sorry, I did not understand your input."
        continue
    guess = (low + high)/2