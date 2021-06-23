#!/usr/bin/python
from random import randint

rematch = "yes"
rock = 0
paper = 0
scissors = 0
wins = 0
loss = 0
while rematch == "yes" or rematch == "y" or rematch == "Y":
    #output selections available to player
    print("====>Rock, Paper, Scissors<====")
    #take input from player: 1=Rock, 2=Paper, 3=Scissors
    user_choice = int(input("Choose 1 for rock, 2 for paper, and 3 for scissors\n"))
    #randomly generate a number from (1, 3)
    bot_choice = randint(1, 3)
    print(bot_choice)
    #compare user input and bot generated number
    if user_choice == 1 and bot_choice == 3:
    #keep track of data
    #user has rock and bot scissors
    #output user and bot choice, and who won (or if it is a tie)
        rock+=1
        print("You WON!")
    elif user_choice == 1 and bot_choice == 2:
    #keep track of data
    #user has rock and bot paper
    #output user and bot choice, and who won (or if it is a tie)
        rock+=1
        print("Bot wins")
    elif user_choice == 2 and bot_choice == 1:
    #keep track of data
    #user=paper, bot=rock
    #output user and bot choice, and who won (or if it is a tie)
        paper+=1
        print("You WON!")
    elif user_choice == 2 and bot_choice == 3:
    #keep track of data
    #user=paper, bot=scissors
    #output user and bot choice, and who won (or if it is a tie)
        paper+=1
        print("Bot wins")
    elif user_choice == 3 and bot_choice == 1:
    #keep track of data
    #user=scissors, bot=rock
    #output user and bot choice, and who won (or if it is a tie)
        scissors+=1
        print("Bot wins")
    elif user_choice == 3 and bot_choice == 2:
    #keep track of data
    #user=scissors, bot=paper
    #output user and bot choice, and who won (or if it is a tie)
        scissors+=1
        print("You WON!")
    #else if draw
    elif user_choice == bot_choice:
        print("It's a DRAW partner! At least you didn't lose \_(^-^)_/")
    #Ask for rematch
    rematch = input("Would you like a rematch?\n")
else:
    print("Goodbye")
#}
#if user wishes to not continue, display number of times player won, lost, and tied.
#When player stops playing display number of times user chose rock, paper, and scissorks
#After game ends, tell player which single object would have had the max number of wins against bot 