import simpleguitk as simplegui
import random

cards = []
exposed = {}
state, card_1, card_2 = None, None, None
turns_counter = 0


def new_game():
    global cards, exposed, state, card_1, card_2, turns_counter

    cards = [_ for _ in range(8)] * 2
    random.shuffle(cards)

    for key in range(16):
        exposed[key] = False

    state, turns_counter = 0, 0
    card_1, card_2 = None, None


def mouseclick(pos):
    global cards, exposed, state, card_1, card_2, turns_counter

    card_index = pos[0] // 50

    if state == 0:
        card_1 = card_index
        exposed[card_1] = True
        state = 1
    elif state == 1:
        card_2 = card_index
        exposed[card_2] = True
        state = 2
        turns_counter += 1
    elif state == 2:
        if not cards[card_1] == cards[card_2]:
            exposed[card_1], exposed[card_2] = False, False
        card_1 = card_index
        exposed[card_1] = True
        state = 1


def draw(canvas):
    global cards, exposed

    for card_index in range(16):
        card_pos = 50 * card_index

        if exposed[card_index]:
            canvas.draw_text(str(cards[card_index]), [20 + card_pos, 62], 24, "White")
        else:
            canvas.draw_polygon([[card_pos, 0], [50 + card_pos, 0], [50 + card_pos, 150], [card_pos, 150]], 2, "White", "Green")

    label.set_text("Turns = %s" % turns_counter)

frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

new_game()
frame.start()
