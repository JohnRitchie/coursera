import simpleguitk as simplegui

# define global variables


# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
# def format(t):
#     pass


def timer_start():
    pass


def timer_stop():
    pass


def timer_restart():
    pass


# define event handler for timer with 0.1 sec interval


# define draw handler


frame = simplegui.create_frame("Stopwatch: The Game", 400, 400)
frame.add_button("Start", timer_start(), 100)
frame.add_button("Stop", timer_stop(), 100)
frame.add_button("Restart", timer_restart(), 100)


frame.start()


# Please remember to review the grading rubric
