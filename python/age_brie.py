from updatable_item import UpdatableItem


class AgeBrie(UpdatableItem):
    AGED_BRIE_DOUBLE_QUALITY_DECREMENT_SELL_IN_THRESHOLD = 0

    def __init__(self, item):
        super().__init__(item)

    def update(self):
        self.decrease_sell_in()

        self.increase_quality()
        if self.sell_in < self.AGED_BRIE_DOUBLE_QUALITY_DECREMENT_SELL_IN_THRESHOLD:
            self.increase_quality()