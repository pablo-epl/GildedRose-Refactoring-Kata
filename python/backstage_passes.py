from item import Item


class BackstagePasses(Item):
    BACKSTAGE_PASSES_DOUBLE_QUALITY_INCREASE_SELL_IN_THRESHOLD = 10
    BACKSTAGE_PASSES_TRIPLE_QUALITY_INCREASE_SELL_IN_THRESHOLD = 5
    BACKSTAGE_PASSES_QUALITY_RESET_SELL_IN_THRESHOLD = 0

    def update(self):
        self.decrease_sell_in()

        self.increase_quality()
        if self.has_to_be_sold_in_less_than(BackstagePasses.BACKSTAGE_PASSES_DOUBLE_QUALITY_INCREASE_SELL_IN_THRESHOLD):
            self.increase_quality()
        if self.has_to_be_sold_in_less_than(BackstagePasses.BACKSTAGE_PASSES_TRIPLE_QUALITY_INCREASE_SELL_IN_THRESHOLD):
            self.increase_quality()
        if self.has_to_be_sold_in_less_than(BackstagePasses.BACKSTAGE_PASSES_QUALITY_RESET_SELL_IN_THRESHOLD):
            self.reset_quality()
