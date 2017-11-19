#! /usr/bin/python3

# Functions to paint the grid

def line(first, l):
    print(first + " ", end='')
    for i in l:
        print(i + " ", end='')
    print()

def paint(g):
    if len(g) == 10:
        line("  ", ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'])
    else:
        line("  ", ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'])
    for i in range(len(g)):
        if i+1 < 10:
            f = str(i+1) + " "
        else:
            f = str(i+1)
        line(f, g[i])
    print()
