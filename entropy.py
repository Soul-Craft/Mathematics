# Example of Entropy

## Imports
import math
from scipy.stats import entropy

## Calculate Entropy By Hand
entropy_by_hand = 0
p_list = [.6666667, .3333333]
for p in p_list:
    entropy_by_hand += (-1*p)*math.log(p, 2)
print('Calculating Entropy By Hand:')
print(entropy_by_hand)

## Calculate Entropy Using Scipy 
entropy_by_scipy = entropy([2,1], base = 2)

print('\nCalculate Entropy by Scipy:')
print(entropy_by_scipy)

## Calculate Information Gain
entropy_parent = entropy([2,2], base = 2)
entropy_child_1 = entropy([2,1], base = 2)
entropy_child_2 = entropy([0,1], base = 2)

information_gain = entropy_parent - (.75 * entropy_child_1 + .25 * entropy_child_2)
print('\nCalculate Information Gain:')
print(information_gain)
