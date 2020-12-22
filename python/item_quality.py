from dataclasses import dataclass


@dataclass(frozen=True)
class ItemQuality:
    MIN_QUALITY = 0
    MAX_QUALITY = 50

    value: int

    def increase(self):
        if self.value < ItemQuality.MAX_QUALITY:
            return ItemQuality(self.value + 1)
        return self

    def decrease(self):
        if self.value > ItemQuality.MIN_QUALITY:
            return ItemQuality(self.value - 1)
        return self

    def reset(self):
        return ItemQuality(ItemQuality.MIN_QUALITY)

    def __eq__(self, other):
        if isinstance(other, ItemQuality):
            return other.value == self.value
        return False

    def __call__(self, *args, **kwargs):
        return self.value
