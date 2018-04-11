#!/usr/bin/env python

import click
import curses
import subprocess

from curses import wrapper


# https://steven.codes/blog/cs10/curses-tutorial/
def screen(stdscr, filename):
    stdscr = curses.initscr()
    curses.noecho()
    curses.cbreak()
    stdscr.keypad(True)
    stdscr.clear()

    # stdscr.addstr("Hello! " + filename)
    # https://stackoverflow.com/a/24477227/9041712
    input = 'head -n 3 {} | column -t -s, | less -S'.format(
        filename)

    process = subprocess.Popen(
        input, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    out, err = process.communicate()
    
    stdscr.addstr(out)
    stdscr.addstr(err)
    
    # p_status = p.wait()
    height,width = stdscr.getmaxyx()
    # curses.resizeterm(height, 500)
    height,width = stdscr.getmaxyx()

    '''
    num = min(height,width)
    for x in range(num):
        stdscr.addch(x,x,'X')
    '''
    stdscr.addstr(str(width))
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


@click.command()
@click.argument('filename')
def run(filename):
    # click.echo(filename)
    wrapper(screen, filename)


if __name__ == '__main__':
    run()
