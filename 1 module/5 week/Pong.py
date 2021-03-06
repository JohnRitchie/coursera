import simpleguitk as simplegui
import random

WIDTH = 600
HEIGHT = 400
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2


def spawn_ball(direction='RIGHT'):
    global ball_pos, ball_vel

    ball_pos = [WIDTH / 2, HEIGHT / 2]

    ball_vel = [0, 0]
    ball_vel[0] = random.randrange(2, 4) if direction == 'RIGHT' else random.randrange(-4, -2)
    ball_vel[1] = random.randrange(-3, -1) if direction == 'RIGHT' else random.randrange(-3, -1)


def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel
    global score1, score2

    paddle1_pos = paddle2_pos = (HEIGHT - PAD_HEIGHT)/2
    paddle1_vel = paddle2_vel = 0

    score1 = score2 = 0

    spawn_ball()


def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel

    canvas.draw_line([0, 0], [0, HEIGHT], WIDTH * 2, "Green")
    canvas.draw_circle([WIDTH / 2, HEIGHT / 2], BALL_RADIUS, 2, "White", "Green")
    canvas.draw_line([WIDTH / 2, 0], [WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0], [PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0], [WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "Red", "White")
    canvas.draw_line([HALF_PAD_WIDTH, paddle1_pos], [HALF_PAD_WIDTH, paddle1_pos + PAD_HEIGHT], PAD_WIDTH, "Yellow")
    canvas.draw_line([WIDTH - HALF_PAD_WIDTH, paddle2_pos], [WIDTH - HALF_PAD_WIDTH, paddle2_pos + PAD_HEIGHT], PAD_WIDTH, "Red")
    canvas.draw_text(str(score1), [80, 90], 40, "White")
    canvas.draw_text(str(score2), [480, 90], 40, "White")

    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]

    if ball_pos[0] <= BALL_RADIUS + PAD_WIDTH:
        if paddle1_pos <= ball_pos[1] <= (paddle1_pos + PAD_HEIGHT):
            ball_vel[0] *= 1.1
            ball_vel[0] = - ball_vel[0]
        else:
            score2 += 1
            spawn_ball('RIGHT')
    elif ball_pos[0] >= WIDTH - BALL_RADIUS - PAD_WIDTH:
        if paddle2_pos <= ball_pos[1] <= (paddle2_pos + PAD_HEIGHT):
            ball_vel[0] *= 1.1
            ball_vel[0] = - ball_vel[0]
        else:
            score1 += 1
            spawn_ball('LEFT')

    if ball_pos[1] <= BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
    elif ball_pos[1] >= HEIGHT - BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]

    if 0 <= (paddle1_pos + paddle1_vel) <= HEIGHT - PAD_HEIGHT:
        paddle1_pos += paddle1_vel
    if 0 <= (paddle2_pos + paddle2_vel) <= HEIGHT - PAD_HEIGHT:
        paddle2_pos += paddle2_vel


def keydown(key):
    global paddle1_vel, paddle2_vel

    base_vel = 5

    if key == simplegui.KEY_MAP["w"]:
        paddle1_vel = -base_vel
    elif key == simplegui.KEY_MAP["up"]:
        paddle2_vel = -base_vel
    elif key == simplegui.KEY_MAP["s"]:
        paddle1_vel = base_vel
    elif key == simplegui.KEY_MAP["down"]:
        paddle2_vel = base_vel


def keyup(key):
    global paddle1_vel, paddle2_vel

    base_vel = 0

    if key == simplegui.KEY_MAP["w"] or key == simplegui.KEY_MAP["s"]:
        paddle1_vel = base_vel
    elif key == simplegui.KEY_MAP["up"] or key == simplegui.KEY_MAP["down"]:
        paddle2_vel = base_vel


frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart", new_game, 100)

new_game()
frame.start()
