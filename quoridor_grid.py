#! /usr/bin/python3

# Functions to paint the grid

def line(first, l, w):  # Draw the spaces and walls betweene cells
    # This draws something like: FI L1 W1 L2 W2 L3 W3 L4
    # Or: FI L1   L2   L3   L4
    print(first + '  ', end='')
    for i in range(len(l)):
        if i < len(l)-1:
            print("%s %s " % (l[i], w[i]), end='')
        else:
            print(l[i])

def paint(A, W_v, W_h):
    line(" ", ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'], [' ']*8)
    for i in range(len(A)):
        line(str(i+1), A[i], W_v[i])
        if i < len(A)-1:
            line(" ", W_h[i], [' ']*8)
    print("\n")
