#!/usr/bin/env python
# a commandline timer app

import sys
from time import sleep


def unit_check():
    # get the argsuments for unit of time
    unit_of_time = sys.argv[1]

    if unit_of_time == '-m':
        unit_of_time = 'minute'
    
    elif unit_of_time == '-s':
        unit_of_time = 'seconds'
        
    return unit_of_time
    
def time_length():
    # get the length of timer for the timer
    length_of_time = int(sys.argv[2])
    return length_of_time
    
def convert_time():
    # convert the time to clock style
    unit_of_time = unit_check()
    length_of_time = time_length()
    
    if unit_of_time == 'minute':
        length_of_time = length_of_time * 60
    elif unit_of_time == 'seconds':
        length_of_time = length_of_time

    return length_of_time

def count_down(time):
    length_of_time = time
    length_of_time = length_of_time - 1
    return length_of_time

def main():
    print('running');
    time = count_down(convert_time())
    while time > 0:
        sleep(1)
        time = count_down(time)
        print(time)

if __name__ == "__main__":
    main()
