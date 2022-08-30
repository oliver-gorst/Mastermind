#Setup the example solution to test against instead of a randomized version in the game
exampleSolution = ['@', '#', '$', '%']

#Setup example guess
#This example is going to have 1 hit, 2 blow, and 1 duplicate character which should not be counted
exampleGuess = ['%', '#', '%', '$']

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


#Find the number of total blows, and subtract the number of hits
#Think there might be a better way to do this
#If item from guess is in solution, add a 1 to the count, don't need to care about the quanitity in the list

#Simple version of same code below
startingCount = 0
temporarySolution = exampleSolution
#Which version do you loop through? The temporary version or the complete version?
for items in exampleGuess:
    if items in exampleSolution:
        startingCount = startingCount + 1
        #If the number is in the Guess twice, it needs to be in the solution twice to count
        #If the number is in the solution twice, it needs to be in the guess twice to count
        #In the blow count calculator, you need to temporaility remove an item from the solution list, so that it can't be found again by a future item in the guess
        #May need to make a new temporary version of the example Solution that can be destroyed for each test


      
blowCount = startingCount - hitCount
print("The blow count is...")
print(blowCount)




def common_elements(exampleGuess, exampleSolution):
    result = []
    for element in exampleGuess:
        if element in exampleSolution:
            #Stop duplicate elements being recorded at this point
            result.append(element)
    length = len(result)
    #print(length)
    return length

#Combine this into the function above
#calcBlow = common_elements(exampleGuess, exampleSolution)
#blowCount = calcBlow - hitCount

#print("The blow count is...")
#print (blowCount)

#Can you put the entire hit and blow searching into a single function that can be called?