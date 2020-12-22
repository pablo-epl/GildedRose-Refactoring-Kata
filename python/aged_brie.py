from item import Item


class AgedBrie(Item):
    AGED_BRIE_DOUBLE_QUALITY_DECREMENT_SELL_IN_THRESHOLD = 0

    def update(self):
        self.decrease_sell_in()

        self.increase_quality()
        if self.has_to_be_sold_in_less_than(AgedBrie.AGED_BRIE_DOUBLE_QUALITY_DECREMENT_SELL_IN_THRESHOLD):
            self.increase_quality()
