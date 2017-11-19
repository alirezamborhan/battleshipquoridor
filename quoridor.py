#! /usr/bin/python3

import os
from grid2 import paint

def resetVars():  # Reset variables
    global won, e, players, playerChars, emptyChar, wallChar_h, wallChar_v, A, W_v, W_h, player, AtoI
    won = [False, 0]  # First item is whether the game has ended, second is the winner.
    e = ""  # For descriptions, explanations and errors.
    players = 0  # Number of players, can be 2 or 4
    playerChars = ['X', 'Y', 'Z', 'K']  # The character each player receives
    emptyChar = '-'  # For empty cells
    wallChar_h = '‒'
    wallChar_v = '|'  # For horizontal and vertical walls
    A = [['-', '-', '-', '-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-', '-', '-', '-'], ['-', '-', '-', '-', '-', '-', '-', '-', '-']]  # A 9x9 list for the players' part of the grid
    W_v = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]  # A 8x9 list for vertical walls
    W_h = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]  # A 9x8 list for horizontal walls
    player = 1
    AtoI = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

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
            A[0][4] = playerChars[0]
            A[8][4] = playerChars[1]
            remainingWalls = {1:10, 2:10}
            break
        elif inp == '2':
            players = 4
            A[0][4] = playerChars[0]
            A[8][4] = playerChars[1]
            A[4][0] = playerChars[2]
            A[4][8] = playerChars[3]
            remainingWalls = {1:5, 2:5, 3:5, 4:5}
            break
        else:
            os.system('clear')
            print("Choose 1 or 2.")

def checkWin():  # To see if anyone has won at the end of each turn.
    global A, player, playerChars, won
    char = playerChars[player-1]
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
    if won[0] == True:
        won[1] = player

def nextPlayer():  # Change player
    global player, players, won
    checkWin()
    if not won[0]:
        player += 1
        if (players == 2 and player == 3) or (players == 4 and player == 5):
            player = 1
    else:
        os.system('clear')
        print("\n\nThe game has ended!\nAnd the glorious winner of this oh-so-beautifully played game is... Player %d!\n\n" % won[1])
        input()

def the_q():  # The quitter
    os.system("clear")
    print("\n\nAre you sure you want to quit? (Y/N)\n\n")
    inp = input().lower()
    if inp == "y":
        return True
    else:
        return False

def checkSurrounded():  # Check to see if putting a wall would surround a pawn.
    pass

def play(s):  # Play a move
    global A, W_h, W_v, AtoI, e, player, playerChars, emptyChar, wallChar_h, remainingWalls
    s = s.split()
    char = playerChars[player-1]
    if len(s) == 2 and s[0] in AtoI and s[1].isdigit() and 1 <= int(s[1]) <= 9:  # To move the pawns.
        i1 = int(s[1])-1
        i2 = AtoI.index(s[0])  # Destination coordinates
        for j in range(len(A)):
            if char in A[j]:
                p1 = j
                p2 = A[j].index(char)  # Current coordinates
                break
        else:
            e = "Where the hell is your player?"  # This should never occur!
            return
        if A[i1][i2] not in playerChars and (
(i1 == p1-1 and i2 == p2 and W_h[i1][i2] != wallChar_h) or
(i1 == p1-2 and i2 == p2 and W_h[i1][i2] != wallChar_h and W_h[i1+1][i2] != wallChar_h and A[i1+1][i2] in playerChars) or
(i1 == p1+1 and i2 == p2 and W_h[p1][p2] != wallChar_h) or
(i1 == p1+2 and i2 == p2 and W_h[p1][p2] != wallChar_h and W_h[p1+1][p2] != wallChar_h and A[i1-1][i2] in playerChars) or
(i1 == p1 and i2 == p2-1 and W_v[i1][i2] != wallChar_v) or
(i1 == p1 and i2 == p2-2 and W_v[i1][i2] != wallChar_v and W_v[i1][i2+1] != wallChar_v and A[i1][i2+1] in playerChars) or
(i1 == p1 and i2 == p2+1 and W_v[p1][p2] != wallChar_v) or
(i1 == p1 and i2 == p2+2 and W_v[p1][p2] != wallChar_v and W_v[p1][p2+1] != wallChar_v and A[i1][i2-1] in playerChars)
):  # Check destination and walls.
            A[i1][i2] = char
            A[p1][p2] = emptyChar
            e = ""
            nextPlayer()
        else:
            e = "You can only move to cells adjacent to your player, without jumping walls. You can also jump other players."
    elif len(s) == 3 and s[0] in AtoI and s[1].isdigit() and 1 <= int(s[1]) <= 9 and s[2] in ['h', 'v']:  # To put walls.
        i1 = int(s[1])-1
        i2 = AtoI.index(s[0])
        if not (0 <= i1 <= 7 or 0 <= i2 <= 7):
            e = "Out of the grid!"
        elif remainingWalls[player] == 0:
            e = "You're out of walls."
        elif s[2] == 'h':
            if W_h[i1][i2] != wallChar_h and W_h[i1][i2+1] != wallChar_h:
                W_h[i1][i2] = wallChar_h
                W_h[i1][i2+1] = wallChar_h
                remainingWalls[player] -= 1
                e = ""
                nextPlayer()
            else:
                e = "There's already a wall there."
        else:
            if W_v[i1][i2] != wallChar_v and W_v[i1+1][i2] != wallChar_v:
                W_v[i1][i2] = wallChar_v
                W_v[i1+1][i2] = wallChar_v
                remainingWalls[player] -= 1
                e = ""
                nextPlayer()
            else:
                e = "There's already a wall there."
    else:
        e = "Wrong input. To move, write something like E 2, and to put a wall, your input must be like E 3 H."

def main():
    resetVars()
    global e, players, A, W_h, W_v, player
    getPlayers()
    while True:
        os.system('clear')
        print("Player %d: %s You have %d walls remaining.\n" % (player, e, remainingWalls[player]))
        paint(A, W_v, W_h)
        inp = str(input()).lower()
        if inp == "q":  # The quitter
            if the_q():
                break
            e = ""
        else:
            play(inp)
        if won[0]:
            break
