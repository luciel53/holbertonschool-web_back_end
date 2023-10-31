#!/usr/bin/env python3
""" Exercise file """

import redis
import uuid
from typing import Union, Callable
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """ count calls method decorator """
    method_name = method.__qualname__  # store the name of the method

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ count how many times methods of the Cache class are called """
        self._redis.incr(method_name)  # increment counter associated to name
        value = method(self, *args, **kwargs)  # call original meth & store it
        return value
    return wrapper


def call_history(method: Callable) -> Callable:
    """ Store the historyof in inputs and outputs for a function """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        #  Create keys for input and output lists
        input = "{}:inputs".format(method.__qualname__)
        output = "{}:outputs".format(method.__qualname__)

        data = str(args)  # convert args in str

        self._redis.rpush(input, data)  # add data to input list

        value = method(self, *args, **kwargs)  # exec originale function

        self._redis.rpush(output, value)  # add value to output list

        return value

    return wrapper


class Cache:
    """ Cache class """
    def __init__(self):
        """ init method """
        self._redis = redis.Redis()  # create an instance of Redis class
        self._redis.flushdb()  # clean completely the db

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ method that generates a random key and store data in database """
        random_key = str(uuid.uuid4())  # generate random key
        self._redis.set(random_key, data)  # associate the value to the key
        return random_key

    def get(self, key: str, fn: Callable = None) -> Union[str, Callable, bytes,
                                                          int, float]:
        """ method that returns the value of the given key from the db """
        value = self._redis.get(key)  # get the value with the key
        if fn:
            value = fn(value)
        return value

    def get_str(self, key: str) -> str:
        """  parametrize value from redis to string """
        return self._redis.get(key)

    def get_int(self, key: str) -> int:
        """ parametrize value from redis to int """
        numb = int(self._redis.get(key))
        return numb
