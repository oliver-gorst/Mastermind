#Setup the example solution to test against instead of a randomized version in the game
exampleSolution = ['@', '#', '$', '@']

#Setup example guess
#This example is going to have 1 hit, 2 blow, and 1 duplicate character which should not be counted
exampleGuess = ['%', '#', '@', '$']


def HitBlowCalc (exampleGuess, exampleSolution):
    hitCount = 0
    blowCount = 0

    #Loop to determine the number of hits
    itemCount = 0
    for items in exampleGuess:
        if items == exampleSolution[itemCount]:
            print("There is a hit!")
            hitCount = hitCount + 1
            itemCount = itemCount + 1
        else:
            itemCount = itemCount + 1
    print("The hit count is...")
    print(hitCount)
    

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
    print("The blow count is...")
    print(blowCount)





HitBlowCalc(exampleGuess, exampleSolution)

#Need to find a way to get the variables out of the function, maybe break into 2 functions and use return?