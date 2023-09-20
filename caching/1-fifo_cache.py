#!/usr/bin/env python3
"""
Create a class FIFOCache that inherits from BaseCaching and is a caching
system:

    You must use self.cache_data - dictionary from the parent class BaseCaching
    You can overload def __init__(self): but don’t forget to call the parent
    init: super().__init__()
    def put(self, key, item):
        Must assign to the dictionary self.cache_data the item value for the
        key key.
        If key or item is None, this method should not do anything.
        If the number of items in self.cache_data is higher that
        BaseCaching.MAX_ITEMS:
            you must discard the first item put in cache
            (FIFO algorithm)
            you must print DISCARD: with the key discarded and following by a
            new line
    def get(self, key):
        Must return the value in self.cache_data linked to key.
        If key is None or if the key doesn’t exist in self.cache_data,
        return None.

"""


from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ FIFOCache class """
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        if key in self.cache_data is None or item in self.cache_data is None:
            return
        self.cache_data[key] = item

        # If number of items in self.cache_data > that BaseCaching.MAX_ITEMS:
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            # define that first item is the next item and the first to pop
            item1 = next(iter(self.cache_data))
            # delete the first item
            self.cache_data.pop(item1)
            print("DISCARD " + item1)

    def get(self, key):
        if key in self.cache_data is None or key not in self.cache_data:
            return None
        # Return the value linked to the key
        return self.cache_data.get(key)
