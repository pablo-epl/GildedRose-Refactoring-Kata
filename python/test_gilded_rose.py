# -*- coding: utf-8 -*-
import unittest

from gilded_rose import GildedRose
from item import Item
from updatable_item_factory import UpdatableItemFactory


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        updatable_items = [UpdatableItemFactory.based_on(item) for item in items]
        gilded_rose = GildedRose(updatable_items)
        gilded_rose.update_quality()
        self.assertEquals("foo", updatable_items[0].name)


if __name__ == '__main__':
    unittest.main()
