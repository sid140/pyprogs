from random import choice

print("Trickster".upper())
print("=" * 20)
print("Game developed by Sid")

winner = []
loser = []
name = input("Enter your name?:").strip().title()
trick = input("Enter the magic number: ").strip().lower()
if trick == "20":
    print("you won, {}!".format(name))
else:
    print("You lost!")
    loser.append(name)

    print("{},You are now in loser's list".format(name))
n = input("Do you want to play again(y/n)?: ").strip().lower()

while trick is not True:
    input("Enter your name?:").strip().title()
    input("Enter the magic number: ").strip().lower()
    print("{},You are now in loser's list again".format(name))
n = input("Do you want to play again(y/n)?: ").strip().lower()
while trick is True:
    print("Good game")

