#! /usr/bin/python3

# Functions to paint the grid

def line(first, l):
    print(first + " ", end='')
    for i in l:
        print(i + " ", end='')
    print()

def paint(g):
    line("  ", ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'])
    for i in range(len(g)):
        if i+1 < 10:
            f = str(i+1) + " "
        else:
            f = str(i+1)
        line(f, g[i])
    print()
