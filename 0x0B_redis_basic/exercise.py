#!/usr/bin/env python3
""" Exercise file """

import redis
import uuid
from typing import Union, Callable


class Cache:
    """ Cache class """
    def __init__(self):
        """ init method """
        self._redis = redis.Redis()  # create an instance of Redis class
        self._redis.flushdb()  # clean completely the db

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ method that generates a random key and store data in database """
        random_key = str(uuid.uuid4())  # generate random key
        self._redis.set(random_key, data)  # associate the value to the key
        return random_key

    def get(self, key: str, fn: Callable) -> Union[str, Callable, bytes, int,
                                                   float]:
        """ method that returns the value of the given key from the db """
        value = self._redis.get(key)  # get the value with the key
        if fn:
            value = fn(value)
        return value

    def get_str(self, key: str) -> str:
        """  parametrize value from redis to string """
        return self._redis.get(key)

    def get_int(self, key: str) -> int:
        """ get int """
        numb = int(self._redis.get(key))
        return numb


cache = Cache()

TEST_CASES = {
    b"foo": None,
    123: int,
    "bar": lambda d: d.decode("utf-8")
}

for value, fn in TEST_CASES.items():
    key = cache.store(value)
    assert cache.get(key, fn=fn) == value
