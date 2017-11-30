#! /usr/bin/python3

import os
from battleship_grid import paint

def resetVars():  # Reset variables
    global w, e, A1, A2, A1_ships, A2_ships, AtoJ, showWhich, shipChar, shotChar, missedChar, A1_shots, A2_shots
    # w = 24  # Window width
    e = ""  # For the explanations, descriptions and warnings
    A1 = [['_', '_', '_', '_', '_', '_', '_', '_', '_', '_'], ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_'], ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_'], ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_'], ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_'], ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_'], ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_'], ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_'], ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_'], ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_']]
    A2 = [['_', '_', '_', '_', '_', '_', '_', '_', '_', '_'], ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_'], ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_'], ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_'], ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_'], ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_'], ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_'], ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_'], ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_'], ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_']]  # The grid arrays for players 1 and 2
    A1_shots = [['_', '_', '_', '_', '_', '_', '_', '_', '_', '_'], ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_'], ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_'], ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_'], ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_'], ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_'], ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_'], ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_'], ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_'], ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_']]
    A2_shots = [['_', '_', '_', '_', '_', '_', '_', '_', '_', '_'], ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_'], ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_'], ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_'], ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_'], ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_'], ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_'], ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_'], ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_'], ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_']]
    A1_ships = {'2':4, '3':3, '4':2, '6':1}
    A2_ships = {'2':4, '3':3, '4':2, '6':1}  # Remaining ships for the shippin'
    AtoJ = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
    showWhich = 1  # Determine that player whose grid must be painted
    shipChar = 'O'  # The character which will be used to depict ships
    shotChar = 'X'
    missedChar = '+'

def instructions():
    os.system("clear")
    print("""\nWelcome to Battleship.

To play, each player must first place their ships on the grid.
Your input must be like 1 A R 4,
where 1 A would be a point on the grid,
R would direct the ship to the right of that point,
and 4 would be the size of the ship.
You can also use L, U, or D instead of R.
After drawing your map, you'll shoot the other player's ships,
where your input must be a location like 1 A.
'X' means a hit and '+' is a miss.
Enjoy!

Press enter to continue.\n""")
    input()

def the_q():
    os.system("clear")
    print("\n\nAre you sure you want to quit? (Y/N)\n\n")
    inp = input().lower()
    if inp == "y":
        return True
    else:
        return False

def addShip(s, ships, A):   # Function to place the players ships at the start
    s = s.split()
    global e, shipChar
    if len(s) == 4 and s[1] in AtoJ and s[0].isdigit() and 1 <= int(s[0]) <= 10 and s[2] in ['r', 'l', 'u', 'd'] and s[3] in ships:  # Check the input
        i1 = int(s[0])-1
        i2 = AtoJ.index(s[1])
        if ships[s[3]] >= 1:
            for i in range(0, int(s[3])):  # Check the ship's position
                try:
                    if s[2] == 'r':
                        if A[i1][i2+i] == shipChar:
                            e = "There's already a ship placed there."
                            return(ships, A)
                    elif s[2] == 'l':
                        if A[i1][i2-i] == shipChar:
                            e = "There's already a ship placed there."
                            return(ships, A)
                    elif s[2] == 'u':
                        if A[i1-i][i2] == shipChar:
                            e = "There's already a ship placed there."
                            return(ships, A)
                    elif s[2] == 'd':
                        if A[i1+i][i2] == shipChar:
                            e = "There's already a ship placed there."
                            return(ships, A)
                except:
                    e = "The ship must be in the grid."
                    return(ships, A)
            for i in range(0, int(s[3])):  # Add the ship
                if s[2] == 'r':
                    A[i1][i2+i] = shipChar
                elif s[2] == 'l':
                    A[i1][i2-i] = shipChar
                elif s[2] == 'u':
                    A[i1-i][i2] = shipChar
                elif s[2] == 'd':
                    A[i1+i][i2] = shipChar
            ships[s[3]] -= 1
            e = "Done."
            return(ships, A)
        else:
            e = "You're out of ships of this size."
            return(ships, A)
    else:
        e = "Wrong input. Your input must be like: 1 A  R  3."
        return(ships, A)

def changePlayer(s):  # A pause to change players. Players mustn't see each other's grids.
    os.system("clear")
    print("\n\n%s\nNow change the player.\n\n" % s)
    input()
    

def checkEnd(A):  # Check to see if the game has ended
    global shipChar
    for i in A:
        if shipChar in i:
            return False
    return True

def theEnd(winner):
    os.system('clear')
    print("\n\nAnd the winner is... The magnificent Player %d!\n\n" % winner)
    input()

def shootShip(s, A, A_shots):  # To shoot!
    global shotChar, missedChar, shipChar, e
    s = s.split()
    if len(s) == 2 and s[0].isdigit() and 1 <= int(s[0]) <= 10 and s[1] in AtoJ:
        i1 = int(s[0])-1
        i2 = AtoJ.index(s[1])
        if A[i1][i2] == shipChar:
            A[i1][i2] = shotChar
            A_shots[i1][i2] = shotChar
            changePlayer("It was a hit.")
            e = "Hit."
            return A, True, A_shots
        elif A[i1][i2] == shotChar or A[i1][i2] == missedChar:
            changePlayer("You'd shot there before.")
            e = ""
            return A, True, A_shots
        else:
            A[i1][i2] = missedChar
            A_shots[i1][i2] = missedChar
            changePlayer("You missed.")
            e = "Missed."
            return A, True, A_shots
    else:
        e = "Wrong input. Your input must be like: 1 A."
        return A, False, A_shots

def main():
    resetVars()
    global e, A1, A2, A1_ships, A2_ships, showWhich, shipChar, A1_shots, A2_shots
    ended, winner = False, 0
    instructions()
    e = "Start shipping. Your remaining ships are: Size 2: %d, Size 3: %d, Size 4: %d, Size 6: %d." % (A1_ships['2'], A1_ships['3'], A1_ships['4'], A1_ships['6'])
    while True:
        if ended:
            break
        os.system("clear")
        if showWhich == 1:
            e = "Player 1:  " + e
        else:
            e = "Player 2:  " + e
        print(e, end="\n\n")
        print("Your map:\n")
        if showWhich == 1:  # Show the previous shots
            paint(A1)
            if list(A1_ships.values()) == [0,0,0,0]:
                print("Your shots:\n")
                paint(A1_shots)
        else:
            paint(A2)
            if list(A2_ships.values()) == [0,0,0,0]:
                print("Your shots:\n")
                paint(A2_shots)
        inp = str(input()).lower()
        if inp == "q":  # The quitter
            if the_q():
                break
            e = ""
        elif list(A1_ships.values()) != [0,0,0,0]:  # If ships aren't placed yet
            (A1_ships, A1) = addShip(inp, A1_ships, A1)
            if list(A1_ships.values()) == [0,0,0,0]:
                showWhich = 2
                e += " Your remaining ships are: Size 2: %d, Size 3: %d, Size 4: %d, Size 6: %d." % (A2_ships['2'], A2_ships['3'], A2_ships['4'], A2_ships['6'])
            else:
                e += " Your remaining ships are: Size 2: %d, Size 3: %d, Size 4: %d, Size 6: %d." % (A1_ships['2'], A1_ships['3'], A1_ships['4'], A1_ships['6'])
        elif list(A2_ships.values()) != [0,0,0,0]:  # For the second player
            (A2_ships, A2) = addShip(inp, A2_ships, A2)
            if list(A2_ships.values()) != [0,0,0,0]:
                e += " Your remaining ships are: Size 2: %d, Size 3: %d, Size 4: %d, Size 6: %d." % (A2_ships['2'], A2_ships['3'], A2_ships['4'], A2_ships['6'])
            else:
                showWhich = 1
                e = "Shoot away."
                changePlayer("The shipping is done.")
        elif showWhich == 1:  # For the first player's shots
            (A2, mustChange, A1_shots) = shootShip(inp, A2, A1_shots)
            if mustChange:
                showWhich = 2
            if checkEnd(A2):
                ended = True
                theEnd(1)
        elif showWhich == 2:  # For the second's shots
            (A1, mustChange, A2_shots) = shootShip(inp, A1, A2_shots)
            if mustChange:
                showWhich = 1
            if checkEnd(A1):
                ended = True
                theEnd(2)
        else:
            e = ""
