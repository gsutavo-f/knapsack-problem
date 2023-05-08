from random import randint
import time

from things import Item, Knapsack
from algorithms import brute_force, recursive, fptas

FILE_PATH = "./probs"


def file_init(file_path):
    with open(file_path, "r") as file:
        for line in file:
            parts = [int(value) for value in line.split()]
            n, max_capacity = parts[1:3]
            item_list = [Item(parts[i], parts[i + 1]) for i in range(3, len(parts), 2)]

        knapsack = Knapsack(max_capacity)

    return knapsack, item_list


def random_init():
    KS_max_cap = randint(50, 100)
    item_amount = randint(1, 20)
    item_list = []
    knapsack = Knapsack(max_capacity=KS_max_cap)

    for i in range(0, item_amount):
        item_list[i] = Item(weight=randint(1, KS_max_cap), value=randint(1, 201))

    return knapsack, item_list


def predefined_init():
    knapsack = Knapsack(max_capacity=100)

    item_list = [
        Item(weight=27, value=38),
        Item(weight=2, value=86),
        Item(weight=41, value=112),
        Item(weight=1, value=0),
        Item(weight=25, value=66),
        Item(weight=1, value=97),
        Item(weight=34, value=195),
        Item(weight=3, value=85),
        Item(weight=50, value=42),
        Item(weight=12, value=223),
    ]

    return knapsack, item_list


def main():
    # knapsack, item_list = random_init()
    knapsack, item_list = file_init(f"{FILE_PATH}/4_473.txt")

    # start = time.time()
    # best_value, best_tuple = brute_force(knapsack, item_list)
    # end = time.time()

    # print(f"Algoritmo lento e ruim executado em {end - start} segundos")
    # print(f"Solução: {best_value}, {best_tuple}")

    start = time.time()
    best_value = fptas(knapsack.max_capacity, item_list, len(item_list))
    end = time.time()

    print(f"Algoritmo fptas executado em {end - start} segundos")
    print(f"Solução: {best_value}")


if __name__ == "__main__":
    main()
