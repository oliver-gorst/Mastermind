import random

#The six possible symbols will be ~, !, @, #, $, and %
possible_options = ['~', '!', '@', '#', '$', '%']

#create a tuple of 4 items, pulling a random item from the list above for each item
item1 = random.choice(possible_options)
item2 = random.choice(possible_options)
item3 = random.choice(possible_options)
item4 = random.choice(possible_options)
game_solution = (item1, item2, item3, item4)



#Setup the turn counter
turn_counter = 8



#Player 1 enter your name
player1_name = input("Player 1 enter your name.")
#Player 2 enter your name
player2_name = input("Player 2 enter your name.")


#Do we want to put the entire game within a big while loop for the turn counter?
#Ask player to input a guess 
print("{} input your guess. Enter four characters from ~, !, @, #, $, and %".format(player1_name))

#Do we need to check to make sure that there are only and exactly 4 characters, and that they are from the list of possible options
guess = input("")

#Validate the input from the user
#for characters in guess:
#    if characters != '~' or '!' or '@' or '#' or '$' or '%':
#        print("No, I won't run")
#    else:
#        continue

#Convert input 4 character text into tuple
tuple_guess = tuple(guess)

#Setup the initial hit and blow count
HitCount = 0
BlowCount = 0

#Print the guess, so the history can be shown of each guess and results combination
print(tuple_guess)

#For each guess, figure out if its in the game solution, and if it is in the right space







