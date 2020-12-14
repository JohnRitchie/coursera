# implementation of card game - Memory

import simpleguitk as simplegui
import random

pairs_list = []
exposed = {}


# helper function to initialize globals
def new_game():
    global pairs_list, exposed

    pairs_list = [random.randrange(0, 8) for _ in range(8)] * 2
    random.shuffle(pairs_list)

    exposed = {key: False for key in range(16)}


# define event handlers
def mouseclick(pos):
    # add game state logic here
    pass


# cards are logically 50x100 pixels in size
def draw(canvas):
    global pairs_list, exposed

    step = 0
    for card in range(16):
        if exposed[card]:
            canvas.draw_text(str(pairs_list[card]), [20 + step, 62], 24, "White")
        else:
            canvas.draw_polygon([[step, 0], [50 + step, 0], [50 + step, 150], [step, 150]], 2, "White", "Green")

        step += 50


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()

# Always remember to review the grading rubric