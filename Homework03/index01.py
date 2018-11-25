#without the help of the internet

import simplegui
import random

interval = 100
count  = 0
total_stops = 0
succes_stops = 0
Stop = True
a=0
b=0
c=0
d=0
def Reset():
    global a,b,c,d,succes_stops,total_stops
    a = 0
    b = 0
    c = 0
    d = 0
    total_stops = 0
    succes_stops = 0
def Stop():
    global succes_stops,total_stops
    total_stops = total_stops + 1
    if d==0:
        succes_stops = succes_stops + 1
    timer.stop()
def Start():
    timer.start()
    
def draw_handler(canvas):
    canvas.draw_text(str(a), (115, 150), 50, 'White')
    canvas.draw_text(":", (145, 150), 50, 'White')
    canvas.draw_text(str(b), [160, 150], 50, 'White')
    canvas.draw_text(str(c), (190, 150), 50, 'White')
    canvas.draw_text(".", (210, 150), 50, 'White')
    canvas.draw_text(str(d), (225, 150), 50, 'White')
    canvas.draw_text(str(succes_stops), (400, 50), 50, 'Red')
    canvas.draw_text("/", (425, 50), 50, 'Red')
    canvas.draw_text(str(total_stops), (450, 50), 50, 'Red')
def timer_handler():
    global a,b,c,d
    d = d + 1
    if d==10:
        d = 0
        global c
        c = c + 1
        if c==10:
            c = 0
            global b
            b = b + 1
            if b==6:
                b = 0
                global a
                a = a + 1
            
frame = simplegui.create_frame('Testing', 500, 300)
frame.set_canvas_background('Blue')
button1 = frame.add_button('Start', Start, 100)
button2 = frame.add_button('Stop', Stop, 100)
button3 = frame.add_button('Restart', Reset,100)
frame.set_draw_handler(draw_handler)
timer = simplegui.create_timer(interval, timer_handler)
frame.start()