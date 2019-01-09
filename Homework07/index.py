import simplegui
import random


def new_game():
    global position
    position={(1,1):0,(1,2):0,(1,3):0,(1,4):0,
              (2,1):0,(2,2):0,(2,3):0,(2,4):0,
              (3,1):0,(3,2):0,(3,3):0,(3,4):0,
              (4,1):0,(4,2):0,(4,3):0,(4,4):0}
    position[random.randint(1,4),random.randint(1,4)]=random.choice([2,4,2])
    position[random.randint(1,4),random.randint(1,4)]=random.choice([2,4,2])
new_game()

def draw(canvas):
    canvas.draw_line((100, 400), (100, 0), 3, 'Red')
    canvas.draw_line((200, 400), (200, 0), 3, 'Red')
    canvas.draw_line((300, 400), (300, 0), 3, 'Red')
    canvas.draw_line((400, 100), (0, 100), 3, 'Red')
    canvas.draw_line((400, 200), (0, 200), 3, 'Red')
    canvas.draw_line((400, 300), (0, 300), 3, 'Red')
    line=1
    pollar=1
    while line<=4:
        while pollar<=4:
            if position.get((line,pollar))!=0:
                canvas.draw_text(str(position.get((line,pollar))), (line*85, pollar*85), 20, 'White')
            pollar= pollar + 1 
        line= line + 1
        pollar=1
        
def start():
    yes=False
    while yes==False:
        line=random.randint(1,4)
        pollar=random.randint(1,4)
        if position[line,pollar]==0:
            position[line,pollar]=2
            yes=True
            
def keydown(key):
    if key == simplegui.KEY_MAP["up"]:
        y = 1
        x = 1
        while y <= 4:
            while x <= 4: 
                if position.get((x, y))!= 0:
                    moving = 3
                    while moving > 0:
                        if position.get((x, y - moving)) == 0:
                            position[(x, y - moving)] = position[(x, y)]
                            position[(x, y)] = 0
                            break
                        elif position.get((x, y - moving)) == position.get((x, y)):
                            position[x, y - moving] = position[x ,y] * 2
                            position[x, y] = 0
                        moving = moving - 1
                x = x + 1
            y = y + 1
            x = 1
        start()   
    if key == simplegui.KEY_MAP["right"]:
        y = 1
        x = 1
        while y <= 4:
            while x <= 4:
                if position.get((x, y)) != 0:
                    moving = 3
                    while moving > 0:
                        if position.get((x + moving, y)) == 0:
                            position[(x + moving, y)]=position[(x, y)]
                            position[(x, y)] = 0
                            break
                        elif position.get((x + moving, y)) == position.get((x, y)):
                            position[x + moving, y] = position[x, y] * 2
                            position[x, y] = 0
                        moving = moving - 1
                x = x + 1
            y = y + 1
            x = 1
        start()
    if key==simplegui.KEY_MAP["left"]:
        y = 1
        x = 1
        while y <= 4:
            while x <= 4:
                
                if position.get((x, y)) != 0:
                    
                    moving = 3
                    while moving > 0:
                        if position.get((x - moving, y)) == 0:
                            position[(x - moving, y)] = position[(x, y)]
                            position[(x, y)] = 0
                            break
                        elif position.get((x - moving, y)) == position.get((x, y)):
                            position[x - moving, y] = position[x, y] * 2
                            position[x, y] = 0
                        moving = moving - 1
                x = x + 1
            y = y + 1
            x = 1
        start()
    if key == simplegui.KEY_MAP["down"]:
        y = 1
        x = 1
        while y <= 4:
            while x <= 4: 
                if position.get((x, y))!= 0:
                    moving = 3
                    while moving > 0:
                        if position.get((x, y + moving)) == 0:
                            position[(x, y + moving)] = position[(x, y)]
                            position[(x, y)] = 0
                            break
                        elif position.get((x, y + moving)) == position.get((x, y)):
                            position[x, y + moving] = position[x ,y] * 2
                            position[x, y] = 0
                        moving = moving - 1
                x = x + 1
            y = y + 1
            x = 1
        start()

        
        
frame = simplegui.create_frame("Game 2048", 400, 400)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
newgame = frame.add_button('new_game', new_game)

frame.start()