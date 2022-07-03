from random import choice
import os
from tkinter import *
from tkinter.ttk import *

print("Trickster".upper())
print("=" * 20)
print("Game developed by Sid")
print("To get hints please type HINT")
print("=" * 20)
winner = []
loser = []
name: str = input("Enter your name?:").strip().title()
trick = input("Enter the magic number: ").strip().lower()
a = input("Type Hint> ")
b = input("600-450=100-30")


if trick == "20":
    winner.append(name)
    pass
    print("you won, {}!".format(name))
else:
    print("{},You lost".format(name))
    loser.append(name)
    print("Better luck next time")
    if a == input("HINT"):
        print(b)
    else:
        pass

        input("Enter the magic number: ").strip().lower()
        print("Thank you for playing")
    n = input("Do you want to play again(y/n)?: ").strip().lower()

while trick is True:
    print("Congratulations, you won!")

while trick is not True:
    input("Enter your name?:").strip().title()
    input("Enter the magic number: ").strip().lower()
    print("{},You lost again".format(name))
n = input("Do you want to play again(y/n)?: ").strip().lower()
if input("Show winner list"):
    print(winner)
else:
    input("Show loser list")
    print(loser)
