import random
import time

#The six possible symbols will be ~, !, @, #, $, and %
possible_options = ['~', '!', '@', '#', '$', '%']

#create a tuple of 4 items, pulling a random item from the list above for each item
item1 = random.choice(possible_options)
item2 = random.choice(possible_options)
item3 = random.choice(possible_options)
item4 = random.choice(possible_options)
gameSolution = (item1, item2, item3, item4)

#Setup the turn counter
turnCounter = 8



'''
#Add Hit/Blow Function in here
'''



#Player 1 enter your name
player1Name = input("Player 1 enter your name.")
#Player 2 enter your name
player2Name = input("Player 2 enter your name.")
currentPlayer = ""


while turnCounter > 0:

    #Check if turn is odd or even to see if the person guessing should be Player 1 or Player 2
    if turnCounter % 2 == 0:
        currentPlayer = player1Name
    else:
        currentPlayer = player2Name
    
    #Ask player to input a guess
    print("{} input your guess. Enter four characters from ~, !, @, #, $, and %".format(currentPlayer))
    
    guess = input("")
    #Need to check to make sure that there are only and exactly 4 characters, and that they are from the list of possible options
    
    #Convert 4 characters from guess into list of characters
    guessList = list(guess)

    #Check if the guess matches the solution and the game is over
    if guessList == gameSolution:
        print("Congratulations, you have won the game!")
        quit()
    else:
        continue
    












#Game is over reveal the solution at the end
print("The game is over, the solution was...")
print(gameSolution)



























#Validate the input from the user
#for characters in guess:
#    if characters != '~' or '!' or '@' or '#' or '$' or '%':
#        print("No, I won't run")
#    else:
#        continue

