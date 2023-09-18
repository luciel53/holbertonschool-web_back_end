#!/usr/bin/env python3
"""
Write an asynchronous coroutine that takes in an integer argument
(max_delay, with a default value of 10) named wait_random that waits for a
random delay between 0 and max_delay (included and float value) seconds and
eventually returns it.

Use the random module.
"""

import random
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ wait_n function """
    list_delay = []
    for i in range(n):
        delay = random.uniform(0, max_delay)
        list_delay.append(delay)
    return list_delay
