from abc import ABC
from abc import abstractmethod
from item_sell_in import ItemSellIn
from item_name import ItemName
from item_quality import ItemQuality


class Item(ABC):
    def __init__(self, name: ItemName, sell_in: ItemSellIn, quality: ItemQuality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    @abstractmethod
    def update(self):
        raise NotImplementedError("update method not implemented")

    def has_to_be_sold_in_less_than(self, days: int):
        return self.sell_in < days

    def decrease_sell_in(self):
        self.sell_in = self.sell_in.decrease()

    def increase_quality(self):
        self.quality = self.quality.increase()

    def decrease_quality(self):
        self.quality = self.quality.decrease()

    def reset_quality(self):
        self.quality = self.quality.reset()

    def __repr__(self):
        return "%s, %s, %s" % (self.name(), self.sell_in(), self.quality())
