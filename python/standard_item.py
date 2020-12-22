from item import Item


class StandardItem(Item):
    DEFAULT_ITEM_QUALITY_DECREASE_SELL_IN_THRESHOLD = 0

    def update(self):
        self.decrease_sell_in()

        self.decrease_quality()

        if self.has_to_be_sold_in_less_than(StandardItem.DEFAULT_ITEM_QUALITY_DECREASE_SELL_IN_THRESHOLD):
            self.decrease_quality()
