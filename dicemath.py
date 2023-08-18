# -*- coding: utf-8 -*-
"""
Perfectly functional, but has scaling issues.
Scaling issues need to be addressed with better math formulas, using combinatorics.

@author: i-JL
"""
import random
from itertools import product

def roll(dice):
    for j in range(quantity): # For as many times as we wanna roll dice
        dice.append(random.SystemRandom().randint(1,size)) # "Roll" a number between 1 and our die size
    for i in range (dtd): # After rolling our numbers
        dice.remove(min(dice)) # Remove as many of the lowest as specified
    return dice

def peel_and_drop(combo):
    sorted_combo = sorted(combo)
    final_combo = sorted_combo[dtd:]
    return final_combo
    
size = 6 # Dice size, or sides
quantity = 4 # How many dice we'll roll total
dtd = 1 # Dice to drop, we'll find the lowest and drop it from the list
###
po = pow(size,quantity) # Possible Outcomes counter
lps = quantity - dtd # Lowest possible result for our dice combination
hps = lps * size # Highest possible result for our dice combination
rp = 0.0 # Result probability
rr = [v for v in range(lps, hps + 1)] # Calculate and save all possible dice results
rrr = len(rr) # rr's range 
pp = [vv for vv in range(pow(quantity,size))] # Calculate and save all possible results for each combination of dice
###
literalblackmagic = 0
probability_Table = {}
###
temp = [list(range(1, size+1)) for _ in range(quantity)]
res = list(product(*temp))
sorted_res = sorted(res)

for combination in res:
    fc = peel_and_drop(combination)
    try:
        probability_Table[sum(fc)] += 1
    except KeyError:
        probability_Table[sum(fc)] = 1
        

for key in probability_Table:
    probability_Table[key] /= po
    #print(str(key) + " * " + str(probability_Table[key]))    #Debugging
    literalblackmagic += key * probability_Table[key]

###
reps = 10000 # Number of repetitions. More = Slower, but closer to statistical average
total = 0 # Initializing sum variable
i = 0 # Initializing iterators
j = 1
k = 1
l = 0
hamsterdance = 0
minimum = 1 # Minimum result on each die
dice = [] # Temporary for each repetition
diceCombos = [] # Generate all possible combinations of dice for mathemagic purposes
comboMean = 0

while i < reps:
    i += 1
    total += sum(roll(dice)) # Roll our numbers, sum them up, and store them in our variable
    dice.clear() # We need to empty the "dice" array after each repetition

"""# Optional in-line progress tracker
    if i % 500000 == 0:
        print("Update: At " + str(i/1000) + "k")
    """

print("# of dice:           " + str(quantity))
print("# of sides of dice:  " + str(size))
print("# of dice dropped:   " + str(dtd))
print("# of repetitions:    " + str(reps/1000000) + " mil")

average = total/reps


print("Statistical average: " + str(literalblackmagic))
print("Average of rolls:    " + str(average))
