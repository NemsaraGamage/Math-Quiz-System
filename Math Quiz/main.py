import sys
import mysql.connector
import quickgame.quickgame
import customgame.mode1.easy
import customgame.mode2.medium
import customgame.mode3.hard

# inserting the gamemenu to a function
def gamemenu():
    print()
    print("             Game menu")
    print("a) Quick Game")
    print("b) custom Game")
    print("c) Display Past Game Details")
    print("d) Exit")
    print()
    return str(input("Enter your option:"))#users option to choose one of them
    print()
    print()

while True:
    user_op=gamemenu()
#if user inputs "a" for quick game
    if (user_op == "a"):
        print()
        print("         Quick Game")
        print()
        quickgame.quickgame.quick()
        
#if user inputs "b" for custom game
    elif (user_op == "b"):
        print()
        print("         Custom Game")
        print()
        diff=str(input("Enter difficuilty (easy/medium/hard)= "))
        if (diff == "easy"):
            print()
            customgame.mode1.easy.ez()
        elif (diff == "medium"):
            print()
            customgame.mode2.medium.med()
        else:
            (diff == "hard")
            print()
            customgame.mode3.hard.hard()

#if user inputs "c" to view past game results
    elif (user_op == "c"):
        print()
        print ("    Past Game Detail")
        print()
        ask=str(input("View past score for Quick Game or Custom Game: "))
        if(ask == "Quick game"):
            import database.qgamedatabase
        else:
            (ask == "Custom game")
            import database.cgamedatabase

            
#if user inputs "d" to exit
    elif(user_op == "d"):
            exit()

