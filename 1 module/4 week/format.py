# Testing template for format function in "Stopwatch - The game"

###################################################
# Student should add code for the format function here


def format(total_deciseconds):
    minutes = total_deciseconds // 600
    seconds = total_deciseconds // 10
    deciseconds = (seconds - total_deciseconds) % 60
    formated_time = str(minutes) + ":" + str(seconds) + "." + str(deciseconds)
    return formated_time


###################################################
# Test code for the format function
# Note that function should always return a string with
# six characters


# print format(0)  # 0:00.0
# print format(7)  # 0:00.7
print format(17)  # 0:01.7
print format(60)  # 0:06.0
print format(63)  # 0:06.3
# print format(214)  # 0:21.4
# print format(599)  # 0:59.9
# print format(600)  # 1:00.0
# print format(602)  # 1:00.2
# print format(667)  # 1:06.7
# print format(1325)  # 2:12.5
# print format(4567)  # 7:36.7
# print format(5999)  # 9:59.9
