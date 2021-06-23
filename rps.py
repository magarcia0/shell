#!/usr/bin/python
from random import randint

rematch = "yes"
total_rounds=0
rock = 0
paper = 0
scissors = 0
loss = 0
bot_wins = 0
user_wins = 0
bot_rock = 0
bot_paper = 0
bot_scissors = 0
most_yields="nuclear devastation"
while rematch == "yes" or rematch == "y" or rematch == "Y":
    #output selections available to player
    print("\n====>Rock, Paper, Scissors<====")
    #take input from player: 1=Rock, 2=Paper, 3=Scissors
    user_choice = int(input("Choose 1 for rock, 2 for paper, and 3 for scissors\n"))
    #randomly generate a number from (1, 3)
    bot_choice = randint(1, 3)
    print("Bot chose {}".format(bot_choice))
    #compare user input and bot generated number
    #keep track of data
    if user_choice == 1 and bot_choice == 3:
    #user has rock and bot scissors
        rock+=1
        print("You WON!")
        user_wins += 1
        total_rounds+=1
    elif user_choice == 1 and bot_choice == 2:
    #user has rock and bot paper
        bot_paper+=1
        print("Bot wins")
        bot_wins += 1
        total_rounds+=1
    elif user_choice == 2 and bot_choice == 1:
    #user=paper, bot=rock
        paper+=1
        print("You WON!")
        user_wins += 1
        total_rounds+=1
    elif user_choice == 2 and bot_choice == 3:
    #user=paper, bot=scissors
        bot_scissors+=1
        print("Bot wins")
        bot_wins += 1
        total_rounds+=1
    elif user_choice == 3 and bot_choice == 1:
    #user=scissors, bot=rock
        bot_rock+=1
        print("Bot wins")
        bot_wins += 1
        total_rounds+=1
    elif user_choice == 3 and bot_choice == 2:
    #user=scissors, bot=paper
        scissors+=1
        print("You WON!")
        user_wins += 1
        total_rounds+=1
    #else if draw
    elif user_choice == bot_choice:
        print("It's a DRAW partner! At least you didn't lose (`~_~)")
        scissors+=1
        bot_scissors+=1
        total_rounds+=1
    #Ask for rematch
    rematch = input("Would you like a rematch? (enter \"yes\" or \"no\")\n")
else:
    #if user wishes to not continue, display number of times player won, lost, and tied.
    #When player stops playing display number of times user chose rock, paper, and scissorks
    #After game ends, tell player which single object would have had the max number of wins against bot 
    #output user and bot choice, and who won (or if it is a tie)
    print("------------------------------------------------------------------")
    if bot_wins > user_wins:
        most_rounds=bot_wins-user_wins
        most_bot_usage=""
        print("Better luck next time pal! You got beat {} out of {} round(s)".format(most_rounds, total_rounds))
        if bot_scissors > bot_rock and bot_scissors > bot_paper:
            most_bot_usage="SCISSORS"
        elif  bot_rock > bot_scissors and bot_rock > bot_paper:
            most_bot_usage="ROCK"
        elif bot_paper > bot_rock and bot_paper > bot_scissors:
            most_bot_usage="PAPER"
        print("Your opponent devastated you the most using %s"%most_bot_usage)
    elif bot_wins < user_wins:
        most_rounds=user_wins-bot_wins
        most_usage=""
        print("Great work ol' chap! You won {} out of {} round(s)".format(most_rounds, total_rounds))
        if scissors > rock and scissors > paper:
            most_usage="SCISSORS"
        elif  rock > scissors and rock > paper:
            most_usage="ROCK"
        elif paper > rock and paper > scissors:
            most_usage="PAPER"
        print("You clobbered your opponent the most using %s"%most_usage)
    elif bot_wins == user_wins:
        print("---\_(^-^)_/-- It's a DRAW partner! At least you didn't lose --\_(^-^)_/---")
    if bot_scissors > bot_rock and bot_scissors > bot_paper:
        most_yields="ROCK"
    elif bot_rock > bot_scissors and bot_rock > bot_paper:
        most_yields="PAPER"
    elif bot_paper > bot_rock and bot_paper > bot_scissors:
        most_yields="SCISSORS"
    print("Picking {} would have yielded the max number of wins against the computer".format(most_yields))
    print("------------------------------------------------------------------")