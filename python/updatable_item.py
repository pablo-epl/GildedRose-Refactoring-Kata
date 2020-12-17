from abc import ABC
from abc import abstractmethod

from item import Item


class UpdatableItem(Item, ABC):
    MIN_QUALITY = 0
    MAX_QUALITY = 50

    # Dependency injection
    def __init__(self, item: Item):
        super() .__init__(item.name, item.sell_in, item.quality)

    @abstractmethod
    def update(self):
        raise NotImplementedError("update method not implemented")

    def sell_in(self):
        return self.sell_in

    def decrease_sell_in(self):
        self.sell_in = self.sell_in - 1

    def increase_quality(self):
        if self.quality < self.MAX_QUALITY:
            self.quality = self.quality + 1

    def decrease_quality(self):
        if self.quality > self.MIN_QUALITY:
            self.quality = self.quality - 1

    def reset_quality(self):
        self.quality = 0
