from item import Item

from age_brie import AgeBrie
from sulfuras import Sulfuras
from backstage_passes import BackstagePasses
from standard_item import StandardItem

from updatable_item import UpdatableItem


class UpdatableItemFactory:
    AGED_BRIE = "Aged Brie"
    BACKSTAGE_PASSES = "Backstage passes to a TAFKAL80ETC concert"
    SULFURAS = "Sulfuras, Hand of Ragnaros"

    @staticmethod
    def based_on(item: Item) -> UpdatableItem:
        if item.name == UpdatableItemFactory.AGED_BRIE:
            return AgeBrie(item)
        elif item.name == UpdatableItemFactory.BACKSTAGE_PASSES:
            return BackstagePasses(item)
        elif item.name == UpdatableItemFactory.SULFURAS:
            return Sulfuras(item)
        else:
            return StandardItem(item)
