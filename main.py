#! /usr/bin/python3

import os
import quoridor
import battleship

e = ""
w = 24

def menu():
    while True:
        os.system('clear')
        global e
        print(e)
        print()
        print("1. Play Battleship")
        print("2. Play Quoridor")
        print("3. Quit\n")
        print()
        try:
            inp = int(input())
        except:
            e = "Enter 1, 2, or 3."
            continue
        if inp == 1:
            battleship.main()
        elif inp == 2:
            quoridor.main()
        elif inp == 3:
            print("Fairwell to you, me old pal!\n")
            quit()
        else:
            e = "Enter 1, 2, or 3."
            continue

menu()
