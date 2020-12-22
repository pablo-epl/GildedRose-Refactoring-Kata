# -*- coding: utf-8 -*-
import unittest

from gilded_rose import GildedRose
from item_factory import ItemFactory


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [ItemFactory.based_on("foo", 0, 0)]
        gilded_rose = GildedRose()
        gilded_rose.update_quality(items)
        self.assertEquals("foo", items[0].name())


if __name__ == '__main__':
    unittest.main()
