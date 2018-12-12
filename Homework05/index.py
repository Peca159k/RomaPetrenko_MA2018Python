import simplegui
import random
mass= range(8)
mass2 = range(8)
mass.extend(mass2)
exposed = []
turns = 0
choices = [-1, -1]
state = 0

def new_game():
    global mass, exposed, turns, choices, state
    exposed = [0] * 16
    turns = 0
    choices = [-1, -1]
    state = 0
    label.set_text("Turns = 0")
    random.shuffle(mass) 
     
def mouseclick(pos):
    global choices, state, turns
    index = int(pos[0] / 50)
    if(state == 0):
        if(exposed[index] == 0):
            if(mass[choices[0]] != mass[choices[1]]):
                exposed[choices[0]] = 0
                exposed[choices[1]] = 0
            exposed[index] = 1
            state = 1
            choices[0] = index
    elif state == 1:
        if(exposed[index] == 0):
            state = 0
            exposed[index] = 1
            choices[1] = index
            turns += 1   
            label.set_text("Turns = " + str(turns))
                         
def draw(canvas):
    for item in range(0,len(mass)):
        if(exposed[item]==0):
            canvas.draw_polygon([(item * 50, 0),(item * 50 + 50, 0),(item * 50 + 50, 100),(item * 50, 100)], 1, "Red", "Green")
        else:
            canvas.draw_text(str(mass[item]), [item * 50 + 10, 70], 48, "White")
    if not(0 in exposed):
        canvas.draw_text("GAME OVER", (150, 75), 75, "Red")
        
        
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)
new_game()
frame.start()