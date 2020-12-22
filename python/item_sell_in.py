from dataclasses import dataclass


@dataclass(frozen=True)
class ItemSellIn:
    value: int

    def decrease(self):
        return ItemSellIn(self.value - 1)

    def __lt__(self, days: int):
        return self.value < days

    def __eq__(self, other):
        if isinstance(other, ItemSellIn):
            return other.value == self.value
        return False

    def __call__(self, *args, **kwargs):
        return self.value
