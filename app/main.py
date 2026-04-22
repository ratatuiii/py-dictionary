from typing import Any


class Dictionary:
    def __init__(
        self,
        initial_capacity: int = 8,
        load_factor: float | int = 2 / 3,
    ) -> None:

        self.capacity = initial_capacity
        self.load_factor = load_factor
        self.size = 0

        self.table = [None] * self.capacity

    def find_index(self, key: str) -> int:
        return hash(key) % self.capacity

    def resize(self) -> None:
        old_table = self.table
        self.capacity *= 2
        self.table = [None] * self.capacity
        self.size = 0

        for item in old_table:
            if item is not None:
                key, value = item
                self[key] = value

    def __len__(self) -> int:
        return self.size

    def __getitem__(self, key: Any) -> Any:
        index = self.find_index(key)

        while self.table[index] is not None:
            if self.table[index][0] == key:
                return self.table[index][1]
            index = (index + 1) % self.capacity

        raise KeyError

    def __setitem__(self, key: Any, value: Any) -> None:
        if self.size >= self.capacity * self.load_factor:
            self.resize()

        index = self.find_index(key)

        while self.table[index] is not None:
            if self.table[index][0] == key:
                break
            index = (index + 1) % self.capacity

        if self.table[index] is None:
            self.size += 1

        self.table[index] = (key, value)
