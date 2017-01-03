# This is the count down function

import time


def count_down(set_time):
    # there is currently a two or three second delay
    # from starting the program before the count down starts

    current_time = int(time.strftime("%M"))
    stop_time = current_time + set_time

    print('\t\t\t\t Your Count Down has Started.\n\n')

    while current_time != stop_time:
        time.sleep(1)
        print "\t\t\t\t" + time.strftime("%H") + ':' + time.strftime("%M") + ':' + time.strftime("%S")

        current_time = int(time.strftime("%M"))

    print('Your count down has finished.')


