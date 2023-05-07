from itertools import combinations

import numpy as np

from things import Item, Knapsack


def dumb(knapsack: Knapsack, item_list: list[Item]):
    allCombinations = []

    for i in range(1, len(item_list) + 1):
        auxComb = list(combinations(item_list, i))
        for a in auxComb:
            allCombinations.append(a)
            
    bestValue = -1
    bestTuple = None
    for tuple in allCombinations:
        knapsack.reset()
        
        for item in tuple:
            knapsack.insert_item(item)

        if not knapsack.max_capacity_reached():
            if knapsack.current_value > bestValue:
                bestValue = knapsack.current_value
                bestTuple = tuple

    return bestValue, bestTuple
