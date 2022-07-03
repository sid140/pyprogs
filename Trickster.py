from random import choice
import os

print("Trickster".upper())
print("=" * 20)
print("Game developed by Sid")
print("To get hints please type HINT")
print("=" * 20)
winner = []
loser = []
name = input("Enter your name?:").strip().title()
trick = input("Enter the magic number: ").strip().lower()
a = input("Type Hint> ")

if trick == "20":
    print("you won, {}!".format(name))
else:
    print("You lost!")
    loser.append(name)

    print("{},You lost".format(name))
n = input("Do you want to play again(y/n)?: ").strip().lower()

while trick is not True:
    input("Enter your name?:").strip().title()
    input("Enter the magic number: ").strip().lower()
    print("{},You lost again".format(name))
n = input("Do you want to play again(y/n)?: ").strip().lower()
if a == "HINT":
    print('600-450=100-30')
else:
    pass





