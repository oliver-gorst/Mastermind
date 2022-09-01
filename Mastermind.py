import random
import time

#The six possible symbols will be ~, !, @, #, $, and %
possible_options = ['~', '!', '@', '#', '$', '%']

#create a list of 4 items, pulling a random item from the list above for each item
#item1 = random.choice(possible_options)
#item2 = random.choice(possible_options)
#item3 = random.choice(possible_options)
#item4 = random.choice(possible_options)
#gameSolution = [item1, item2, item3, item4]
#Temporary game solution for testing
gameSolution = ['@', '#', '$', '@']

#Setup the turn counter
turnCounter = 8



def HitBlowCalc (exampleGuess, exampleSolution):
    #Define global variables to be used outside of function
    global hitCount
    hitCount = int(0)
    global blowCount
    blowCount = int(0)
    global hitBlowString
    hitBlowString = ''
    global hitTextLoop 
    #hitTextLoop = 0
    global blowTextLoop
    #blowTextLoop = 0

    #Loop to determine the number of hits
    itemCount = int(0)
    for items in exampleGuess:
        if items == exampleSolution[itemCount]:
            print("There is a hit!")
            hitCount = hitCount + 1
            itemCount = itemCount + 1
        else:
            itemCount = itemCount + 1
    #print("The hit count is...")
    #print(hitCount)

    #Loop to determine the number of blows
    startingCount = 0
    for items in exampleGuess:
        #Search for items which are common between the guess and the solution
        if items in exampleSolution:
            startingCount = startingCount + 1
            #Remove the counted item from the temporary solution so that it can not be counted twice
            exampleSolution.remove(items)
    #Subtract the hits which have already been counted earlier but still count as blows in this code block
    blowCount = startingCount - hitCount
    #print("The blow count is...")
    #print(blowCount)
    
    #Make loop that adds letters to string for each Hit and then 
    hitTextLoop = hitCount
    blowTextLoop = blowCount

    while hitTextLoop > 0:
        hitBlowString.append('H')
        hitTextLoop = hitTextLoop - 1

    while blowTextLoop > 0:
        hitBlowString.append('B')
        blowTextLoop = blowTextLoop - 1

    #Return variables at end of function
    return (hitCount, blowCount)



#Player 1 enter your name
player1Name = input("Player 1 enter your name.")
#Player 2 enter your name
player2Name = input("Player 2 enter your name.")
currentPlayer = ""

#Setup initial data structure to show guesses, add items to list, for items in list print item to put it on a new line
printableGuesses = []
#Setup initial data structure to show hit and blows associated with guess
printableHitBlow = []


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

    
    #Call Hit/Blow function here
    HitBlowCalc(guess, gameSolution)

    #Need to convert numbers of hits and blows into simple format of H's and B's

    #Add guess to list of existing guesses
    printableGuesses.append(guess)

    #Add hit blow calculation to list of existing hit blow calculations
    #printableHitBlow.append()

    #Print the guess
    print("The guess is: {}".format(guess))
    #Print the hits and blows
    print("There are {} hits.".format(hitCount))
    print("There are {} blows.".format(blowCount))

    #Print all previous guesses and results
    #Append the current guess and results to something that can be called again next version to be printed

    turnCounter = turnCounter - 1












#Game is over reveal the solution at the end
print("The game is over, the solution was...")
print(gameSolution)



























#Validate the input from the user
#for characters in guess:
#    if characters != '~' or '!' or '@' or '#' or '$' or '%':
#        print("No, I won't run")
#    else:
#        continue

