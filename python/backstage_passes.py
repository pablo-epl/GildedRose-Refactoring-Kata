from updatable_item import UpdatableItem


class BackstagePasses(UpdatableItem):
    BACKSTAGE_PASSES_DOUBLE_QUALITY_INCREASE_SELL_IN_THRESHOLD = 10
    BACKSTAGE_PASSES_TRIPLE_QUALITY_INCREASE_SELL_IN_THRESHOLD = 5
    BACKSTAGE_PASSES_QUALITY_RESET_SELL_IN_THRESHOLD = 0

    def __init__(self, item):
        super().__init__(item)

    def update(self):
        self.decrease_sell_in()

        self.increase_quality()
        if self.sell_in < self.BACKSTAGE_PASSES_DOUBLE_QUALITY_INCREASE_SELL_IN_THRESHOLD:
            self.increase_quality()
        if self.sell_in < self.BACKSTAGE_PASSES_TRIPLE_QUALITY_INCREASE_SELL_IN_THRESHOLD:
            self.increase_quality()
        if self.sell_in < self.BACKSTAGE_PASSES_QUALITY_RESET_SELL_IN_THRESHOLD:
            self.reset_quality()
