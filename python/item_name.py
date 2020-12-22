from dataclasses import dataclass


@dataclass(frozen=True)
class ItemName:
    AGED_BRIE = "Aged Brie"
    BACKSTAGE_PASSES = "Backstage passes to a TAFKAL80ETC concert"
    SULFURAS = "Sulfuras, Hand of Ragnaros"

    value: str

    def is_aged_brie(self):
        return self.value == ItemName.AGED_BRIE

    def is_backstage_passes(self):
        return self.value == ItemName.BACKSTAGE_PASSES

    def is_sulfuras(self):
        return self.value == ItemName.SULFURAS

    def __eq__(self, other):
        if isinstance(other, ItemName):
            return other.value == self.value
        return False

    def __call__(self, *args, **kwargs):
        return self.value
