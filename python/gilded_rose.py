# -*- coding: utf-8 -*-

class GildedRose(object):

    AGED_BRIE = "Aged Brie"
    BACKSTAGE_PASSES = "Backstage passes to a TAFKAL80ETC concert"
    SULFURAS = "Sulfuras, Hand of Ragnaros"

    AGED_BRIE_DOUBLE_QUALITY_DECREMENT_SELL_IN_THRESHOLD = 0

    BACKSTAGE_PASSES_DOUBLE_QUALITY_INCREASE_SELL_IN_THRESHOLD = 10
    BACKSTAGE_PASSES_TRIPLE_QUALITY_INCREASE_SELL_IN_THRESHOLD = 5
    BACKSTAGE_PASSES_QUALITY_RESET_SELL_IN_THRESHOLD = 0

    DEFAULT_ITEM_QUALITY_DECREASE_SELL_IN_THRESHOLD = 0

    MIN_QUALITY = 0
    MAX_QUALITY = 50

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            # existen 4 casos para manipular un item
            # "Aged Brie", "Backstage passes to a TAFKAL80ETC concert",
            # "Sulfuras, Hand of Ragnaros" y cuando no es ninguno de
            # los anteriores
            # Si el item es AGE_BRIED
            #  Si el item.quality es menor a la MAX_QUALITY, se incrementa la calidad
            #
            if item.name == self.AGED_BRIE:
                self.decrease_sell_in(item)
                self.update_aged_brie_quality(item)

            elif item.name == self.BACKSTAGE_PASSES:
                self.decrease_sell_in(item)
                self.update_backstage_passes_quality(item)

            elif item.name == self.SULFURAS:
                pass

            else:
                self.decrease_sell_in(item)
                self.update_default_item_quality(item)

    def increase_quality(self, item):
        if item.quality < self.MAX_QUALITY:
            item.quality = item.quality + 1

    def decrease_quality(self, item):
        if item.quality > self.MIN_QUALITY:
            item.quality = item.quality - 1

    def decrease_sell_in(self, item):
        item.sell_in = item.sell_in - 1

    def reset_quality(self, item):
        item.quality = 0

    def update_aged_brie_quality(self, item):
        self.increase_quality(item)
        if item.sell_in < self.AGED_BRIE_DOUBLE_QUALITY_DECREMENT_SELL_IN_THRESHOLD:
            self.increase_quality(item)

    def update_backstage_passes_quality(self, item):
        self.increase_quality(item)
        if item.sell_in <= self.BACKSTAGE_PASSES_DOUBLE_QUALITY_INCREASE_SELL_IN_THRESHOLD:
            self.increase_quality(item)
        if item.sell_in <= self.BACKSTAGE_PASSES_TRIPLE_QUALITY_INCREASE_SELL_IN_THRESHOLD:
            self.increase_quality(item)
        if item.sell_in <= self.BACKSTAGE_PASSES_QUALITY_RESET_SELL_IN_THRESHOLD:
            self.reset_quality(item)

    def update_default_item_quality(self, item):
        self.decrease_quality(item)
        if item.sell_in < self.DEFAULT_ITEM_QUALITY_DECREASE_SELL_IN_THRESHOLD:
            self.decrease_quality(item)

    def update_sulfuras_quality(self, item):
        pass




class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

