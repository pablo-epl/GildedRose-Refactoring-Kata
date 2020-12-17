# -*- coding: utf-8 -*-
from updatable_item import UpdatableItem


class GildedRose(object):
    def __init__(self, items: [UpdatableItem]):
        self.items = items

    def update_quality(self):
        for item in self.items:
            item.update()
