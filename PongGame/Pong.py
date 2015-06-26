# Implementation of classic arcade game Pong
#http://www.codeskulptor.org/#user40_DWG0hswoqwI7kJQ.py

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
ball_pos = [WIDTH / 2, HEIGHT / 2]


# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    """Spawns the ball in appropriate direction."""
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    if direction == LEFT:
        ball_vel = [-random.randrange(120, 240)/60.0, -random.randrange(60, 180)/60.0]
    elif direction == RIGHT:
        ball_vel = [random.randrange(120, 240)/60.0, -random.randrange(60, 180)/60.0]
    
# define event handlers
def new_game():
    """Starts new game."""
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2  # these are ints
    
    #Initialize scores, paddle positions and paddle velocities
    score1 = 0 
    score2 = 0
    paddle1_pos = HEIGHT/2 - HALF_PAD_HEIGHT
    paddle2_pos = HEIGHT/2 - HALF_PAD_HEIGHT
    paddle1_vel = 0
    paddle2_vel = 0
    spawn_ball(LEFT)

def draw(canvas):
    """Draw Handler for canvas."""
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
 
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    if ball_pos[1] - BALL_RADIUS <= 0 or  ball_pos[1] + BALL_RADIUS >= HEIGHT:
        ball_vel[1] = -ball_vel[1]
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]

    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "Red", "White")
    
    # update paddle's vertical position, keep paddle on the screen
    if paddle1_pos + paddle1_vel > 0 and paddle1_pos + PAD_HEIGHT + paddle1_vel < HEIGHT:
        paddle1_pos += paddle1_vel
    if paddle2_pos + paddle2_vel > 0 and paddle2_pos + PAD_HEIGHT + paddle2_vel < HEIGHT:
        paddle2_pos += paddle2_vel
    
    # draw paddles
    canvas.draw_polygon([[0, paddle1_pos], [PAD_WIDTH, paddle1_pos], [PAD_WIDTH, paddle1_pos + PAD_HEIGHT], [0, paddle1_pos + PAD_HEIGHT]], 2, 'White')
    canvas.draw_polygon([[WIDTH - PAD_WIDTH, paddle2_pos], [WIDTH, paddle2_pos], [WIDTH, paddle2_pos + PAD_HEIGHT], [WIDTH - PAD_WIDTH, paddle2_pos + PAD_HEIGHT]], 2, 'White')

    # determine whether paddle and ball collide    
    if ball_pos[0] - BALL_RADIUS - PAD_WIDTH <= 0:
        if ball_pos[1] > paddle1_pos and ball_pos[1] < paddle1_pos + PAD_HEIGHT:
            ball_vel[0] = -ball_vel[0] * 1.1
        else:
            score2 += 1
            spawn_ball(RIGHT)
    if ball_pos[0] + BALL_RADIUS + PAD_WIDTH >= WIDTH:
        if ball_pos[1] > paddle2_pos and ball_pos[1] < paddle2_pos + PAD_HEIGHT:
            ball_vel[0] = -ball_vel[0] * 1.1
        else:
            score1 += 1
            spawn_ball(LEFT)
            
            
    # draw scores
    canvas.draw_text(str(score1), (WIDTH * (1.0 / 4), 50), 42, 'White', 'serif')
    canvas.draw_text(str(score2), (WIDTH * (3.0 / 4), 50), 42, 'White', 'serif')
        
def keydown(key):
    """Defines keydown handler for game controls."""
    global paddle1_vel, paddle2_vel
    
    if key == simplegui.KEY_MAP['w']:
        paddle1_vel = -3
    if key == simplegui.KEY_MAP['s']:
        paddle1_vel = 3
    if key == simplegui.KEY_MAP['up']:
        paddle2_vel = -3
    if key == simplegui.KEY_MAP['down']:
        paddle2_vel = 3

def keyup(key):
    """Defines keyup handler for game controls."""
    global paddle1_vel, paddle2_vel
    
    if key == simplegui.KEY_MAP['w']:
        paddle1_vel = 0
    if key == simplegui.KEY_MAP['s']:
        paddle1_vel = 0
    if key == simplegui.KEY_MAP['up']:
        paddle2_vel = 0
    if key == simplegui.KEY_MAP['down']:
        paddle2_vel = 0

def button_handler():
    """Defines button handler for "RESET" Button."""
    new_game()

# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button('Restart', button_handler, 60)


# start frame
new_game()
frame.start()
