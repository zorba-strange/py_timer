# Timer App.
# Main app that runs the program


import count_down
import sys

def main():
    print('running')
    set_time = int(sys.argv[-1])
    count_down.count_down(set_time)


if __name__ == '__main__':
    main()
