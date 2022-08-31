#Setup the example solution to test against instead of a randomized version in the game
exampleSolution = ['@', '#', '$', '@']

#Setup example guess
#This example is going to have 1 hit, 2 blow, and 1 duplicate character which should not be counted
exampleGuess = ['%', '#', '@', '$']

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



startingCount = 0
#Create a new version of the game solution where items which have been counted can be removed
temporarySolution = exampleSolution
for items in exampleGuess:
    #Search for items which are common between the guess and the solution
    if items in temporarySolution:
        startingCount = startingCount + 1
        #Remove the counted item from the temporary solution so that it can not be counted twice
        temporarySolution.remove(items)
#Subtract the hits which have already been counted earlier but still count as blows in this code block
blowCount = startingCount - hitCount
print("The blow count is...")
print(blowCount)


#Combine this into the function above
#Can you put the entire hit and blow searching into a single function that can be called?