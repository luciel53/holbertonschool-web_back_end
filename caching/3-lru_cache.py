#!/usr/bin/env python3
"""
Create a class LRUCache that inherits from BaseCaching and is a caching system:

    You must use self.cache_data - dictionary from the parent class BaseCaching
    You can overload def __init__(self): but don’t forget to call the parent
    init: super().__init__()
    def put(self, key, item):
        Must assign to the dictionary self.cache_data the item value for the
        key key.
        If key or item is None, this method should not do anything.
        If the number of items in self.cache_data is higher that
        BaseCaching.MAX_ITEMS:
            you must discard the least recently used item (LRU algorithm)
            you must print DISCARD: with the key discarded and following by
            a new line
    def get(self, key):
        Must return the value in self.cache_data linked to key.
        If key is None or if the key doesn’t exist in self.cache_data,
        return None.
"""


from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """ LRUCache class """
    def __init__(self):
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ Put function """
        if key is None or item is None:
            return

        # If number of items in self.cache_data >= that BaseCaching.MAX_ITEMS:
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            if key not in self.cache_data:
                # stores the last item in a variable that is a tuple
                lru_item = self.cache_data.popitem(last=False)
                # just keep the key and store it in another variable
                just_key = lru_item[0]
                print("DISCARD: {}".format(just_key))
        # assign to the dictionary self.cache_data the item value for the key
        self.cache_data[key] = item

    def get(self, key):
        """ get function """
        if key in self.cache_data is None:
            return None
        if key in self.cache_data:
            self.cache_data.move_to_end(key)
            return self.cache_data[key]

        else:
            return None
