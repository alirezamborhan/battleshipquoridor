#! /usr/bin/python3

import os
from quoridor_grid import paint

def resetVars():  # Reset variables
    global won, e, players, playerChars, emptyChar, wallChar_h, wallChar_v, A, W_v, W_h, player, AtoI
    won = [False, 0]  # First item is whether the game has ended, second is the winner.
    e = ""  # For descriptions, explanations and errors.
    players = 0  # Number of players, can be 2 or 4
    playerChars = ['', 'X', 'Y', 'Z', 'Q']  # The character each player receives
    emptyChar = '-'  # For empty cells
    wallChar_h = '‒'
    wallChar_v = '|'  # For horizontal and vertical walls
    A = [['-', '-', '-', '-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-', '-', '-', '-']]  # A 9x9 list for the players' part of the grid
    W_v = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]  # A 8x9 list for vertical walls
    W_h = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]  # A 9x8 list for horizontal walls
    player = 1
    AtoI = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

def instructions():
    os.system("clear")
    print("""\nWelcome to Quoridor.

The object of the game is for one player to get to
the row or column furthest to their starting position.
In each turn, the player can either move to a cell
adjacent to his current position by typing the address
like A 1, or place a 2-cell-wide wall between the cells
by typing the address of the cell to the wall's
northeast and whether it is to be horizontal or vertical,
like A 1 V. You cannot cross walls, you can jump other
players, and if your path is blocked twice, you can move
to the side of the adjacent player. The game can be
played by two or four players.
Enjoy!

Press enter to continue.\n""")
    input()

def getPlayers():
    global players, A, remainingWalls
    os.system('clear')
    print()
    while True:
        print("""\n1. Play with two players
2. Play with four players\n\n""")
        inp = str(input())
        if inp == '1':
            players = 2
            A[0][4] = playerChars[1]
            A[8][4] = playerChars[2]
            remainingWalls = {1:10, 2:10}
            break
        elif inp == '2':
            players = 4
            A[0][4] = playerChars[1]
            A[8][4] = playerChars[2]
            A[4][0] = playerChars[3]
            A[4][8] = playerChars[4]
            remainingWalls = {1:5, 2:5, 3:5, 4:5}
            break
        else:
            os.system('clear')
            print("Choose 1 or 2.")

def checkWin(player, A):  # To see if anyone has won at the end of each turn.
    global playerChars
    won = [False, 0]
    char = playerChars[player]
    if player == 1:
        if char in A[8]:
            won[0] = True
    elif player == 2:
        if char in A[0]:
            won[0] = True
    elif player == 3:
        for i in range(len(A)):
            if A[i][8] == char:
                won[0] = True
                break
    else:
        for i in range(len(A)):
            if A[i][0] == char:
                won[0] = True
                break
    won[1] = player
    return(won)

def nextPlayer():  # Change player
    global player, players, won, A, playerChars
    won = checkWin(player, A)
    if not won[0]:
        player += 1
        if (players == 2 and player == 3) or (players == 4 and player == 5):
            player = 1
    else:
        os.system('clear')
        print("\n\nThe game has ended!\nAnd the glorious winner of this oh-so-beautifully played game is... Player %d (%s)!\n\n" % (won[1], playerChars[won[1]]))
        input()

def the_q():  # The quitter
    os.system("clear")
    print("\n\nAre you sure you want to quit? (Y/N)\n\n")
    inp = input().lower()
    if inp == "y":
        return True
    else:
        return False

def clone(theList):  # Make a copy of two dimensional lists to avoid issues with reference value.
    theList_clone = []
    for x in theList:
        theList_clone.append(x.copy())
    return theList_clone

def check(player, A, W_h, W_v):  # Continuation of checkSurrounded. Works by playing a fake game to see if it can be won.
    global checked, checkResult, remainingWalls, playerChars
    char = playerChars[player]
    A = clone(A)
    if not checkResult:
        return
    for j in range(len(A)):
        if char in A[j]:
            p1 = j
            p2 = A[j].index(char)  # Pawn coordinates
            break
    for move in [
            (p2 <= 7, None if not p2 <= 7 else str(AtoI[p2+1])+" "+str(p1+1)),  # Move right
            (p2 >= 1, None if not p2 >= 1 else str(AtoI[p2-1])+" "+str(p1+1)),  # Move left
            (p1 <= 7, None if not p1 <= 7 else str(AtoI[p2])+" "+str(p1+2)),  # Move down
            (p1 >= 1, None if not p1 >= 1 else str(AtoI[p2])+" "+str(p1)),  # Move up
            (p2 <= 6, None if not p2 <= 6 else str(AtoI[p2+2])+" "+str(p1+1)),  # Jump pawn to right
            (p2 >= 2, None if not p2 >= 2 else str(AtoI[p2-2])+" "+str(p1+1)),  # Jump pawn to left
            (p1 <= 6, None if not p1 <= 6 else str(AtoI[p2])+" "+str(p1+3)),  # Jump pawn to down
            (p1 >= 2, None if not p1 >= 2 else str(AtoI[p2])+" "+str(p1-1)),  # Jump pawn to up
            (p2 <= 7 and p1 >= 1, None if not (p2 <= 7 and p1 >= 1) else str(AtoI[p2+1])+" "+str(p1)),  # Jump blocks to northeast
            (p2 >= 1 and p1 >= 1, None if not (p2 >= 1 and p1 >= 1) else str(AtoI[p2-1])+" "+str(p1)),  # Jump blocks to northwest
            (p2 <= 7 and p1 <= 7, None if not (p2 <= 7 and p1 <= 7) else str(AtoI[p2+1])+" "+str(p1+2)),  # Jump blocks to southeast
            (p2 >= 1 and p1 <= 7, None if not (p2 >= 1 and p1 <= 7) else str(AtoI[p2-1])+" "+str(p1+2))  # Jump blocks to southwest
]:
        if move[0]:
            (A_new, F_new, W_h_new, W_v_new, walls) = play(move[1], A, W_h, W_v, remainingWalls, player)  # Fake play!
            if not checked.__contains__(A_new):
                checked.append(A_new)
                if F_new:
                    if checkWin(player, A_new)[0]:
                        checkResult = False
                        return
                    else:
                        check(player, A_new, W_h_new, W_v_new)

def checkSurrounded(A, W_h, W_v):  # Check to see if putting a wall would surround a pawn. True means surrounded, False means not.
    global e, players, playerChars, checkResult, checked
    results = []
    for player in range(1, players+1):
        checkResult = True
        checked = [A]
        check(player, A, W_h, W_v)
        if checkResult:
            return True
    return False

def play(s, A, W_h, W_v, remainingWalls, player):  # Play a move
    global AtoI, e, playerChars, emptyChar, wallChar_h
    Next = False  # To see if the player should be changed
    A = clone(A)
    W_h = clone(W_h)
    W_v = clone(W_v)
    s = s.split()
    char = playerChars[player]
    if len(s) == 2 and s[0] in AtoI and s[1].isdigit() and 1 <= int(s[1]) <= 9:  # To move the pawns.
        i1 = int(s[1])-1
        i2 = AtoI.index(s[0])  # Destination coordinates
        for j in range(len(A)):
            if char in A[j]:
                p1 = j
                p2 = A[j].index(char)  # Current coordinates
                break
        if A[i1][i2] not in playerChars and (  # Check destination and walls.
                (i1 == p1-1 and i2 == p2 and W_h[i1][i2] != wallChar_h) or  # Move up
                (i1 == p1-2 and i2 == p2 and W_h[i1][i2] != wallChar_h and W_h[i1+1][i2] != wallChar_h and A[i1+1][i2] in playerChars) or  # Jump pawn up
                (i1 == p1+1 and i2 == p2 and W_h[p1][p2] != wallChar_h) or  # Move down
                (i1 == p1+2 and i2 == p2 and W_h[p1][p2] != wallChar_h and W_h[p1+1][p2] != wallChar_h and A[i1-1][i2] in playerChars) or  # Jump pawn down
                (i1 == p1 and i2 == p2-1 and W_v[i1][i2] != wallChar_v) or  # Move left
                (i1 == p1 and i2 == p2-2 and W_v[i1][i2] != wallChar_v and W_v[i1][i2+1] != wallChar_v and A[i1][i2+1] in playerChars) or  # Jump pawn left
                (i1 == p1 and i2 == p2+1 and W_v[p1][p2] != wallChar_v) or  # Move right
                (i1 == p1 and i2 == p2+2 and W_v[p1][p2] != wallChar_v and W_v[p1][p2+1] != wallChar_v and A[i1][i2-1] in playerChars) or  # Jump pawn right
                (i1 == p1-1 and i2 == p2-1 and A[p1-1][p2] in playerChars and W_h[p1-1][p2] != wallChar_h and (p1 == 1 or W_h[p1-2][p2] == wallChar_h or A[p1-2][p2] in playerChars) and W_v[p1-1][p2-1] != wallChar_v) or  # Jump northwest when path blocked twice above
                (i1 == p1-1 and i2 == p2-1 and A[p1][p2-1] in playerChars and W_v[p1][p2-1] != wallChar_v and (p2 == 1 or W_v[p1][p2-2] == wallChar_v or A[p1][p2-2] in playerChars) and W_h[p1-1][p2-1] != wallChar_h) or  # Jump northwest when path blocked twice on left
                (i1 == p1+1 and i2 == p2-1 and A[p1+1][p2] in playerChars and W_h[p1][p2] != wallChar_h and (p1 == 7 or W_h[p1+1][p2] == wallChar_h or A[p1+2][p2] in playerChars) and W_v[p1+1][p2-1] != wallChar_v) or  # Jump southwest when path blocked twice below
                (i1 == p1+1 and i2 == p2-1 and A[p1][p2-1] in playerChars and W_v[p1][p2-1] != wallChar_v and (p2 == 1 or W_v[p1][p2-2] == wallChar_v or A[p1][p2-2] in playerChars) and W_h[p1][p2-1] != wallChar_h) or  # Jump southwest when path blocked twice on left
                (i1 == p1-1 and i2 == p2+1 and A[p1-1][p2] in playerChars and W_h[p1-1][p2] != wallChar_h and (p1 == 1 or W_h[p1-2][p2] == wallChar_h or A[p1-2][p2] in playerChars) and W_v[p1-1][p2] != wallChar_v) or  # Jump northeast when path blocked twice above
                (i1 == p1-1 and i2 == p2+1 and A[p1][p2+1] in playerChars and W_v[p1][p2] != wallChar_v and (p2 == 7 or W_v[p1][p2+1] == wallChar_v or A[p1][p2+2] in playerChars) and W_h[p1-1][p2+1] != wallChar_h) or  # Jump northeast when path blocked twice on right
                (i1 == p1+1 and i2 == p2+1 and A[p1+1][p2] in playerChars and W_h[p1][p2] != wallChar_h and (p1 == 7 or W_h[p1+1][p2] == wallChar_h or A[p1+2][p2] in playerChars) and W_v[p1+1][p2] != wallChar_v) or  # Jump southeast when path blocked twice below
                (i1 == p1+1 and i2 == p2+1 and A[p1][p2+1] in playerChars and W_v[p1][p2] != wallChar_v and (p2 == 7 or W_v[p1][p2+1] == wallChar_v or A[p1][p2+2] in playerChars) and W_h[p1][p2+1] != wallChar_h)  # Jump southeast when path blocked twice on right
):
            A[i1][i2] = char
            A[p1][p2] = emptyChar
            e = ""
            Next = True
        else:
            e = "You can only move to cells adjacent to your player, without jumping walls. You can also jump other players."
    elif len(s) == 3 and s[0] in AtoI and s[1].isdigit() and 1 <= int(s[1]) <= 9 and s[2] in ['h', 'v']:  # To put walls.
        i1 = int(s[1])-1
        i2 = AtoI.index(s[0])
        if not (0 <= i1 <= 7 and 0 <= i2 <= 7):
            e = "Out of the grid!"
        elif remainingWalls[player] == 0:
            e = "You're out of walls."
        elif s[2] == 'h':  # For horizontal walls
            if W_h[i1][i2] != wallChar_h and W_h[i1][i2+1] != wallChar_h:
                W_h_clone = clone(W_h)
                W_v_clone = clone(W_v)
                W_h[i1][i2] = wallChar_h
                W_h[i1][i2+1] = wallChar_h
                if checkSurrounded(A, W_h, W_v):
                    e = "The walls you put must not block any player's path completely."
                    return A, Next, W_h_clone, W_v_clone, remainingWalls
                remainingWalls[player] -= 1
                e = ""
                Next = True
            else:
                e = "There's already a wall there."
        elif s[2] == 'v':  # For vertical walls
            if W_v[i1][i2] != wallChar_v and W_v[i1+1][i2] != wallChar_v:
                W_h_clone = clone(W_h)
                W_v_clone = clone(W_v)
                W_v[i1][i2] = wallChar_v
                W_v[i1+1][i2] = wallChar_v
                if checkSurrounded(A, W_h, W_v):
                    e = "The walls you put must not block any player's path completely."
                    return A, Next, W_h_clone, W_v_clone, remainingWalls
                remainingWalls[player] -= 1
                e = ""
                Next = True
            else:
                e = "There's already a wall there."
        else:
            e = "Bug?"
    else:
        e = "Wrong input. To move, write something like E 2, and to put a wall, your input must be like E 3 H."
    return A, Next, W_h, W_v, remainingWalls

def main():
    resetVars()
    global e, players, A, W_h, W_v, player, remainingWalls, playerChars
    Next = False
    instructions()
    getPlayers()
    while True:
        os.system('clear')
        print("Player %d (%s): %s You have %d walls remaining.\n" % (player, playerChars[player], e, remainingWalls[player]))
        paint(A, W_v, W_h)
        inp = str(input()).lower()
        if inp == "q":  # The quitter
            if the_q():
                break
            e = ""
        else:
            (A, Next, W_h, W_v, remainingWalls) = play(inp, A, W_h, W_v, remainingWalls, player)
            if Next:
                nextPlayer()
        if won[0]:
            break
