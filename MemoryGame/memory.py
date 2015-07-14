# implementation of card game - Memory
# http://www.codeskulptor.org/#user40_9EvAhAeiFTEtxoA.py

import simplegui
import random

lst1 = [i for i in range(8)]
lst2 = [i for i in range(8)]
memoryDeck = lst1 + lst2


# helper function to initialize globals
def new_game():
    global memoryDeck, exposed, state, unpaired1, unpaired2, turns, cardColor
    random.shuffle(memoryDeck)
    exposed = [False for a in range(16)]
    state = 0
    unpaired1 = -1
    unpaired2 = -1
    turns = 0
    label.set_text("Turns = " + str(turns))
    cardtype = []
    index = 0
    color = ""
    cardColor = []
    
    # To make half of the deck red and half of it black
    for card in memoryDeck:
        if card in cardtype:
            index = cardtype.index(card)
            color = cardColor[index]
            if(color == "Red"):
                cardColor.append("Black")
            elif(color == "Black"):
                cardColor.append("Red")
            cardtype.append(card)
        else:
            cardColor.append(random.choice(["Red", "Black"]))
            cardtype.append(card)
        
        
# define event handlers
def mouseclick(pos):
    global memoryDeck, exposed, state, unpaired1, unpaired2, turns
    if state == 0:
        if pos[0] >=0 and pos[0] <= 800 and pos[1] >= 0 and pos[1] <= 100:
            state = 1
            index = pos[0]/50
            if exposed[index] == False:
                exposed[index] = True 
                unpaired1 = index
        
    elif state == 1:
        if pos[0] >=0 and pos[0] <= 800 and pos[1] >= 0 and pos[1] <= 100:
            state = 2
            index = pos[0]/50
            if exposed[index] == False:
                exposed[index] = True 
                unpaired2 = index
                turns += 1
                label.set_text("Turns = " + str(turns))
      
    else:
        if pos[0] >=0 and pos[0] <= 800 and pos[1] >= 0 and pos[1] <= 100:
            index = pos[0]/50
            if exposed[index] == False:
                exposed[index] = True 
                state = 1
                if memoryDeck[unpaired1] != memoryDeck[unpaired2]:
                    exposed[unpaired1] = False
                    exposed[unpaired2] = False  
                unpaired1 = index
                unpaired2 = -1
                
                           
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global memoryDeck, turns, cardColor
    x = 0
    index = 0
    #cardtype = []
    for card in memoryDeck:
        if exposed[index]:
            canvas.draw_polygon([[x, 0], [x + 50, 0], [x + 50, 100], [x, 100]], 3, 'Silver', 'White')
            canvas.draw_text(str(card), (x + 15, 62), 38, cardColor[index])
            canvas.draw_text(str(card), (x + 6, 20), 15, cardColor[index], 'monospace')
            canvas.draw_text(str(card), (x + 36, 90), 15, cardColor[index], 'monospace')
            canvas.draw_polygon([[x + 38, 12], [x + 41, 15], [x + 38, 18], [x + 35, 15]], 3, cardColor[index], cardColor[index])
            canvas.draw_polygon([[x + 12, 82], [x + 15, 85], [x + 12, 88], [x + 9, 85]], 3, cardColor[index], cardColor[index])
        else:
            canvas.draw_polygon([[x, 0], [x + 50, 0], [x + 50, 100], [x, 100]], 3, 'Silver', 'White')
            # If image is not loading then uncomment draw_polygon() and comment draw_image()
            #canvas.draw_polygon([[x, 0], [x + 50, 0], [x + 50, 100], [x, 100]], 1, 'White', 'Green')
            canvas.draw_image(image, (600 / 2, 742 / 2), (600, 742), (x+25, 50), (50, 100))
            
        x += 50
        index += 1

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.set_canvas_background('White')
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
image = simplegui.load_image('http://blog.spoongraphics.co.uk/wp-content/uploads/2013/playing-cards/13.jpg')
new_game()
frame.start()
