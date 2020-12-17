from updatable_item import UpdatableItem


class StandardItem(UpdatableItem):
    DEFAULT_ITEM_QUALITY_DECREASE_SELL_IN_THRESHOLD = 0

    def __init__(self, item):
        super().__init__(item)

    def update(self):
        self.decrease_sell_in()

        self.decrease_quality()
        if self.sell_in < self.DEFAULT_ITEM_QUALITY_DECREASE_SELL_IN_THRESHOLD:
            self.decrease_quality()
