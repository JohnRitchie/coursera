# implementation of card_index game - Memory

import simpleguitk as simplegui
import random

cards = []
exposed = {}
state_1 = None
state_2 = None


# helper function to initialize globals
def new_game():
    global cards, exposed, state_1, state_2

    cards = [random.randrange(0, 8) for _ in range(8)] * 2
    random.shuffle(cards)

    exposed = {key: False for key in range(16)}

    state_1 = 0
    state_2 = 0


# define event handlers
def mouseclick(pos):
    global cards, exposed, state_1, state_2

    print cards[pos[0] // 50]
    exposed[pos[0] // 50] = True
    print exposed


# card_indexs are logically 50x100 pixels in size
def draw(canvas):
    global cards, exposed

    for card_index in range(16):
        card_pos = 50 * card_index

        if exposed[card_index]:
            canvas.draw_text(str(cards[card_index]), [20 + card_pos, 62], 24, "White")
        else:
            canvas.draw_polygon([[card_pos, 0], [50 + card_pos, 0], [50 + card_pos, 150], [card_pos, 150]], 2, "White", "Green")


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