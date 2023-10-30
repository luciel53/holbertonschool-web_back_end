#!/usr/bin/env python3
""" Exercise file """

import redis
import uuid
from typing import Union


class Cache:
    """ Cache class """
    def __init__(self):
        """ init method """
        self._redis = redis.Redis()  # create an instance of Redis class
        self._redis.flushdb()  # clean completely the db

    def store(self, data: Union(str, bytes, int, float)) -> str:
        """ method that generates a random key"""
        random_key = str(uuid.uuid4())  # generate random key
        self._redis.set(random_key, data)  # associate the value to the key
        return random_key
