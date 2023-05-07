from random import randint
import time

from things import Item, Knapsack
from algorithms import dumb


def random_init():
    KS_max_cap = randint(50, 100)
    item_amount = randint(1, 20)
    item_list = []
    knapsack = Knapsack(max_capacity=KS_max_cap)

    for i in range(0, item_amount):
        item_list[i] = Item(weight=randint(1, KS_max_cap), value=randint(1, 201))

    return knapsack, item_list


def predefined_init():
    knapsack = Knapsack(max_capacity=50)

    item_list = [
        Item(weight=10, value=60),
        Item(weight=20, value=100),
        Item(weight=30, value=120),
    ]

    return knapsack, item_list


def main():
    # knapsack, item_list = random_init()
    knapsack, item_list = predefined_init()

    start = time.time()
    best_value, best_tuple = dumb(knapsack, item_list)
    end = time.time()

    print(f"Algoritmo lento e ruim executado em {end - start} segundos")
    print(f"Solução: {best_value}, {best_tuple}")


if __name__ == "__main__":
    main()
