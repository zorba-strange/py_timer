# This is the count down function

import time


def count_down(set_time):
    # there is currently a two or three second delay
    # from starting the program before the count down starts

    current_min_time    = int(time.strftime("%M"))
    current_sec_time    = int(time.strftime("%S"))
    stop_min_time       = current_min_time + set_time
    stop_sec_time       = current_sec_time

    print('\t\t\t\t Your Count Down has Started.\n\n')

    while current_min_time != stop_min_time & current_sec_time != stop_sec_time:
        time.sleep(1)
        print "\t\t\t\t" + time.strftime("%H") + ':' + time.strftime("%M") + ':' + time.strftime("%S")

        current_min_time = int(time.strftime("%M"))
        current_sec_time = int(time.strftime("%S"))

    print('Your count down has finished.')
