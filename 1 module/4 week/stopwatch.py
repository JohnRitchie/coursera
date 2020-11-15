import simplegui

counter = 0


# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D

# def format(t):
#     pass


def timer_start():
    timer.start()


def timer_stop():
    timer.stop()
    global counter
    counter = 0


def timer_restart():
    timer.stop()
    global counter
    counter = 0


def timer_handler():
    global counter
    counter += 1
    print counter


# define draw handler


frame = simplegui.create_frame("Stopwatch: The Game", 400, 400)
frame.add_button("Start", timer_start, 100)
frame.add_button("Stop", timer_stop, 100)
frame.add_button("Restart", timer_restart, 100)
frame.start()

timer = simplegui.create_timer(100, timer_handler)


# Please remember to review the grading rubric
