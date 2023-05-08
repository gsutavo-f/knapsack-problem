from itertools import combinations
import collections.abc
import functools

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


def recursive(curr_capacity: int, item_list: list[Item], n: int) -> int:
    if n == 0:
        return 0
    elif item_list[n - 1].get_weight() > curr_capacity:
        return recursive(curr_capacity, item_list, n - 1)
    else:
        return max(
            [
                item_list[n - 1].get_value()
                + recursive(
                    # listOfValues, listOfWeights, capacity - listOfWeights[n - 1], n - 1
                    curr_capacity - item_list[n - 1].get_weight(),
                    item_list,
                    n - 1,
                ),
                recursive(curr_capacity, item_list, n - 1),
            ]
        )
    
def dynnamic_programming(max_capacity: int, item_list: list[Item], n: int):
    K = [[0 for i in range(0,max_capacity + 1)] for i in range(0,n + 1)]

    for i in range(n + 1):
        for cap in range(max_capacity + 1):
            if i == 0 or cap == 0:
                K[i][cap] = 0
            elif item_list[i - 1].get_weight() <= cap:
                K[i][cap] = max(
                    item_list[i - 1].get_value() + K[i - 1][cap -
                                                            item_list[i - 1].get_weight()],
                    K[i - 1][cap]
                )
            else:
                K[i][cap] = K[i - 1][cap]
                
    return K[n][max_capacity]


def fptas(curr_capacity: int, item_list: list[Item], n: int, scaling_factor: int = 4) -> int:
    weight_list = (item.get_weight() for item in item_list)
    max_value = max(weight_list)
    
    # scaling_factor = (max_value * epsilon) / n
    new_capacity = int(curr_capacity / scaling_factor)
    new_items_cost = []
    for item in item_list:
        item.weight = round(item.get_weight() / scaling_factor) + 1
        new_items_cost.append(item)

    return dynnamic_programming(new_capacity, new_items_cost, n)