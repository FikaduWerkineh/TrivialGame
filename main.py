from Astronemy import *
from Sport import *
from Movie import *
from General_Knowledge import *

def main():
    chose = input("What type of quiz you want to play with?  choose A/S/M/G ")

    if chose == "A":
        print("You are gonna to play Astronomy.", Astronemy())

    elif chose == "S":
        print("You are gonna to play sport.", Spoort())

    elif chose == "M":
        print("You are gonna to play movie.", Moviei())

    elif chose == "G":
        print("You are gonna to play General_knowledge.", General_Knowledge())

    playAgain = input("you wanna to play again?y/n ")
    if playAgain == "y":
        main()
    else:
        print("byeeeeeee")
main()
