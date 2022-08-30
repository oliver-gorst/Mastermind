#Setup the example solution to test against instead of a randomized version in the game
exampleSolution = ['@', '#', '$', '%']

#Setup example guess
#This example is going to have 1 hit, 2 blow, and 1 character which are not in the solution
exampleGuess = ['%', '#', '~', '$']

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
for items in exampleGuess:
    if items in exampleSolution:
        blow




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
calcBlow = common_elements(exampleGuess, exampleSolution)
blowCount = calcBlow - hitCount

print("The blow count is...")
print (blowCount)

#Can you put the entire hit and blow searching into a single function that can be called?