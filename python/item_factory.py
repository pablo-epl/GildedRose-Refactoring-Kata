from item import Item

from aged_brie import AgedBrie
from sulfuras import Sulfuras
from backstage_passes import BackstagePasses
from standard_item import StandardItem

from item import Item
from item_sell_in import ItemSellIn
from item_name import ItemName
from item_quality import ItemQuality


class ItemFactory:

    @staticmethod
    def based_on(name: str, sell_in: int, quality: int) -> Item:
        name = ItemName(name)
        sell_in = ItemSellIn(sell_in)
        quality = ItemQuality(quality)

        if name.is_aged_brie():
            return AgedBrie(name, sell_in, quality)
        elif name.is_backstage_passes():
            return BackstagePasses(name, sell_in, quality)
        elif name.is_sulfuras():
            return Sulfuras(name, sell_in, quality)
        else:
            return StandardItem(name, sell_in, quality)
