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
#player1_name = input("Player 1 enter your name.")
#Player 2 enter your name
#player2_name = input("Player 2 enter your name.")





print(game_solution)




