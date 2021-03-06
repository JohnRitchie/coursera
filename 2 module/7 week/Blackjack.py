import simpleguitk as simplegui
import random

CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")

in_play = False
outcome = ""
score = 0
deck, dealer_hand, player_hand = None, None, None

SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 10, 'Q': 10, 'K': 10}


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank),
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]],
                          CARD_SIZE)

    def draw_back(self, canvas, pos):
        card_loc = (CARD_CENTER[0], CARD_CENTER[1])
        canvas.draw_image(card_back, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0] + 1, pos[1] + CARD_CENTER[1] + 1],
                          CARD_SIZE)


class Hand:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def get_value(self):
        value = 0
        has_ace = False

        for card in self.cards:
            rank = card.get_rank()
            value += VALUES[rank]
            if rank == 'A':
                has_ace = True

        if has_ace and value < 12:
            value += 10

        return value

    def draw(self, canvas, pos):
        for card in self.cards:
            pos[0] = pos[0] + CARD_SIZE[0] + 40
            card.draw(canvas, pos)


class Deck:
    def __init__(self):
        self.deck = [SUIT + RANK for SUIT in SUITS for RANK in RANKS]

    def shuffle(self):
        return random.shuffle(self.deck)

    def deal_card(self):
        suit, rank = tuple(self.deck.pop())
        card = Card(suit, rank)

        return card


def deal():
    global outcome, in_play, deck, dealer_hand, player_hand, score

    outcome = "New game!\nHit or stand?"

    if in_play:
        in_play = False
        score -= 1
        deal()
    else:
        deck = Deck()
        deck.shuffle()

        dealer_hand = Hand()
        dealer_hand.add_card(deck.deal_card())
        dealer_hand.add_card(deck.deal_card())

        player_hand = Hand()
        player_hand.add_card(deck.deal_card())
        player_hand.add_card(deck.deal_card())

        in_play = True


def hit():
    global player_hand, outcome, in_play, score

    if in_play:
        if player_hand.get_value() <= 21:
            player_hand.add_card(deck.deal_card())
        else:
            outcome = "You have busted!\nDealer wins!\nNew deal?"
            in_play = False
            score -= 1

        if player_hand.get_value() > 21:
            outcome = "You have busted!\nDealer wins!\nNew deal?"
            in_play = False
            score -= 1


def stand():
    global player_hand, dealer_hand, outcome, in_play, score

    if in_play:
        if player_hand.get_value() > 21:
            outcome = "You have busted!\nDealer wins!\nNew deal?"
            score -= 1
            return

        while dealer_hand.get_value() < 17:
            dealer_hand.add_card(deck.deal_card())

        if dealer_hand.get_value() > 21:
            outcome = "Dealer have busted!\nYou win!\nNew deal?"
            score += 1
        else:
            if player_hand.get_value() <= dealer_hand.get_value():
                outcome = "Dealer wins!\nNew deal?"
                score -= 1
            else:
                outcome = "You win!\nNew deal?"
                score += 1

        in_play = False


def draw(canvas):
    global player_hand, dealer_hand, in_play, score

    player_hand.draw(canvas, [-50, 400])
    dealer_hand.draw(canvas, [-50, 50])

    canvas.draw_text(outcome, (55, 300), 30, "Black")
    canvas.draw_text("Blackjack", (335, 60), 40, "Black")
    canvas.draw_text("Player\n" + str(player_hand.get_value()), (10, 445), 30, "Red")
    canvas.draw_text("Score: " + str(score), (355, 300), 30, "Red")

    if in_play:
        dealer_hand.cards[0].draw_back(canvas, [60, 50])
        canvas.draw_text("Dealer", (10, 55), 30, "Red")
    else:
        canvas.draw_text("Dealer\n" + str(dealer_hand.get_value()), (10, 100), 30, "Red")


frame = simplegui.create_frame("Blackjack", 900, 600)
frame.set_canvas_background("Green")

frame.add_button("Deal", deal, 200)
frame.add_button("Hit", hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)

deal()
frame.start()
