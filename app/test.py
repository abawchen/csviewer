#!/usr/bin/env python

import click

@click.command()
def less():
    click.echo_via_pager('\n'.join(('Line %d' % idx) * 20
                                   for idx in range(200)))

if __name__ == '__main__':
    less()

'''
import curses

from curses import wrapper

# https://steven.codes/blog/cs10/curses-tutorial/
def main(stdscr):
    stdscr = curses.initscr()
    curses.noecho()
    curses.cbreak()
    stdscr.keypad(True)
    stdscr.clear()
    while True:
        # Store the key value in the variable `c`
        c = stdscr.getch()
        # Clear the terminal
        stdscr.clear()
        if c == ord('a'):
            stdscr.addstr("You pressed the 'a' key.")
        elif c == curses.KEY_UP:
            stdscr.addstr("You pressed the up arrow.")
        else:
            stdscr.addstr("This program doesn't know that key.....")

wrapper(main)
'''

