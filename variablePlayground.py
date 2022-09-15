import random

#The six possible symbols will be ~, !, @, #, $, and %
PossibleOptions = ['A', 'B', 'C', 'D', 'E', 'F']

#Create a list of 4 items, pulling a random item from the list above for each item
item1 = random.choice(PossibleOptions)
item2 = random.choice(PossibleOptions)
item3 = random.choice(PossibleOptions)
item4 = random.choice(PossibleOptions)
MeowGameSolution = [item1, item2, item3, item4]


print(MeowGameSolution)


CopyCatSolution = MeowGameSolution[:]


print(CopyCatSolution)


CopyCatSolution.remove(CopyCatSolution[0])

print(CopyCatSolution)
print(MeowGameSolution)


#look into self.variable to see if that solves the problem


