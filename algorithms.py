from itertools import combinations

import numpy as np

from things import Item, Knapsack


def brute_force(knapsack: Knapsack, item_list: list[Item]):
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


def recursive(knapsack: Knapsack, item_list: list[Item], n: int) -> int:
    if n == 0:
        return 0
    elif item_list[n - 1].get_weight() > (
        knapsack.current_capacity - knapsack.max_capacity
    ):
        return recursive(knapsack, item_list, n - 1)
    else:
        return max(
            [
                # listOfValues[n - 1]
                knapsack.insert_item(item_list[n - 1])
                + recursive(
                    # listOfValues, listOfWeights, capacity - listOfWeights[n - 1], n - 1
                    knapsack,
                    item_list,
                    n - 1,
                ),
                recursive(knapsack, item_list, n - 1),
            ]
        )
