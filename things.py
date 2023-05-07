class Item:
    def __init__(self, weight, value) -> None:
        self.weight = weight
        self.value = value

    def get_weight(self) -> int:
        return self.weight

    def get_value(self) -> int:
        return self.value

    def __repr__(self) -> str:
        return f"Peso: {self.weight} :: Valor: {self.value}"


class Knapsack:
    def __init__(self, max_capacity: int) -> None:
        self.items: list[Item] = []
        self.max_capacity = max_capacity
        self.current_capacity = 0
        self.current_value = 0

    def max_capacity_reached(self, new_item: Item = None):
        if new_item is not None:
            extra_weight = new_item.get_weight()
            if self.current_capacity + extra_weight > self.max_capacity:
                return True
        else:
            if self.current_capacity > self.max_capacity:
                return True

        return False

    def insert_item(self, item: Item) -> None:
        if self.max_capacity_reached(item):
            return

        self.items.append(item)
        self.current_capacity += item.get_weight()
        self.current_value += item.get_value()

    def remove_item(self, item: Item) -> None:
        if not self.items:
            return

        try:
            self.items.remove(item)
        except ValueError:
            raise ValueError(
                f"Item {item} de peso {item.weight} e valor {item.value} nao existe na mochila e nao pode ser removido"
            )

        self.current_capacity -= item.get_weight()
        self.current_value -= item.get_value()

    def check_capacity_and_value(self) -> bool:
        curr_wgt = 0
        curr_val = 0

        for item in self.items:
            curr_wgt += item.weight
            curr_val += item.value

        if curr_wgt == self.current_capacity and curr_val == self.current_value:
            return True

        return False
    
    def reset(self) -> None:
        self.items: list[Item] = []
        self.current_capacity = 0
        self.current_value = 0
