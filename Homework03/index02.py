#complexity homework 9/10. TRUE HARD
#with the help of the internet
import simplegui
import random

interval = 100
total_stops = 0
succes_stops = 0
t = 0

def result(succes_stops, total_stops):
    return str(succes_stops) + '/' + str(total_stops)

#Transformation found on the Internet
def format(t):
    a = str(t / 600)
    b = str((t % 600) / 100)
    c = str((t % 100) / 10)
    d = str((t % 10))
    return a + ':' + b + c + '.' + d

def Start():
    timer.start()
    
def Stop():
    timer.stop()
    global total_stops,succes_stops
    total_stops = total_stops + 1
    if t%10==0:
        succes_stops = succes_stops + 1
        
def Reset():
    timer.stop()
    global t,total_stops,succes_stops
    t = 0
    total_stops = 0
    succes_stops = 0
    
def draw_handler(canvas):
    canvas.draw_text(format(t), (130, 130), 50, "White")
    canvas.draw_text(result(succes_stops,total_stops), (300,50), 30, "Red") 
def timer_handler():
    global t
    t = t + 1
    
frame = simplegui.create_frame('Testing', 500, 300,)
frame.set_canvas_background('Blue')
button1 = frame.add_button('Start', Start, 100)
button2 = frame.add_button('Stop', Stop, 100)
button3 = frame.add_button('Restart', Reset,100)
frame.set_draw_handler(draw_handler)
timer = simplegui.create_timer(interval, timer_handler)
frame.start()