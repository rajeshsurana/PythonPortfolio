import time
import webbrowser

break_count = 0
total_breaks = 3

print ("This program started at " + time.ctime())
while break_count < total_breaks:
    time.sleep(2*60*60)
    webbrowser.open("www.google.com")
    break_count += 1
