# -*- coding: utf-8 -*-
from item import Item


class GildedRose(object):

    @staticmethod
    def update_quality(items):
        for item in items:
            item.update()
