# "Stopwatch: The Game"
#http://www.codeskulptor.org/#user40_Ndhmb4WnVxUi4yV.py
import simplegui

# define global variables
sw_time = 0
success_stop = 0
total_stop = 0
watch_stopped = True

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    """This function format the time in MM:SS.M format."""
    
    #Extract individual parts of the time from counter
    temp = t
    sec = 0
    minute = 0
    mili_sec = temp % 10
    temp /=10
    if (temp > 0):
        sec = temp % 60
        temp /= 60
        if (temp > 0):
            minute = temp % 10
            temp /= 10
            if(temp > 0):
                #Means timer has reached its limit of 10 minutes. Reset it again
                reset_button_handler()
            
    # Convert all times from int format to string format
    str_mili_sec = str(mili_sec)
    str_sec = ''
    str_minute = ''
    if sec < 10:
        str_sec = '0' + str(sec)
    else:
        str_sec = str(sec)
    str_minute = str(minute)
    return str_minute + ':' + str_sec + '.' + str_mili_sec
          
# define event handlers for buttons; "Start", "Stop", "Reset"
def reset_button_handler():
    """This function implements the event handler for reset button"""
    
    global sw_time, success_stop, total_stop
    timer.stop()
    sw_time = 0
    success_stop = 0
    total_stop = 0

def start_button_handler():
    """This function implements the event handler for start button"""
    
    global watch_stopped
    if (watch_stopped == True):
        timer.start()
        watch_stopped = False

def stop_button_handler():
    """This function implements the event handler for stop button"""
    
    global success_stop, total_stop, watch_stopped
    
    if (watch_stopped == False):
        timer.stop()
        if (sw_time%10 == 0):
            success_stop += 1
        total_stop += 1
        watch_stopped = True

# define event handler for timer with 0.1 sec interval
def timer_handler():
    """This function implements the timer handler"""
    
    global sw_time
    sw_time += 1

# define draw handler
def draw_handler(canvas):
    """This function implements the draw handler"""
    
    global success_stop, total_stop
    canvas.draw_text(format(sw_time), [100, 140], 40, 'White')
    canvas.draw_text(str(success_stop)+'/'+str(total_stop), [240, 35], 40, 'Green')
    
# create frame
frame = simplegui.create_frame("Stopwatch", 300, 250)

# register event handlers
timer = simplegui.create_timer(100, timer_handler)
start_button = frame.add_button('Start', start_button_handler, 70)
stop_button = frame.add_button('Stop', stop_button_handler, 70)
reset_button = frame.add_button('Reset', reset_button_handler, 70)
frame.set_draw_handler(draw_handler)

# start frame
frame.start()