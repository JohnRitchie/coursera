import simpleguitk as simplegui


counter = 0
successful_stops = 0
total_stops = 0


def format_time(total_deciseconds):
    minutes = str(total_deciseconds // 600)
    seconds = (total_deciseconds % 600) // 10
    seconds = "0" + str(seconds) if seconds < 10 else str(seconds)
    deciseconds = str((total_deciseconds % 600) % 10)
    formated_time = minutes + ":" + seconds + "." + deciseconds

    return formated_time


def check_win(count):
    point = True if (count % 10) == 0 else False
    return point


def timer_start():
    timer.start()


def timer_stop():
    timer.stop()

    global counter

    global successful_stops
    if check_win(counter):
        successful_stops += 1

    global total_stops
    total_stops += 1


def timer_reset():
    timer.stop()

    global counter
    counter = 0

    global successful_stops
    successful_stops = 0

    global total_stops
    total_stops = 0


def timer_handler():
    global counter
    counter += 1


def draw_handler(canvas):
    current_time = format_time(counter)
    canvas.draw_text(current_time, [130, 200], 48, "Red")

    success_rate = str(successful_stops) + "/" + str(total_stops)
    canvas.draw_text(success_rate, [280, 70], 30, "Green")


frame = simplegui.create_frame("Stopwatch: The Game", 400, 400)
frame.add_button("Start", timer_start, 100)
frame.add_button("Stop", timer_stop, 100)
frame.add_button("Reset", timer_reset, 100)
frame.set_draw_handler(draw_handler)

timer = simplegui.create_timer(100, timer_handler)

frame.start()
