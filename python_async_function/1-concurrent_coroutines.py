#!/usr/bin/env python3
"""
Write an asynchronous coroutine that takes in an integer argument
(max_delay, with a default value of 10) named wait_random that waits for a
random delay between 0 and max_delay (included and float value) seconds and
eventually returns it.

Use the random module.
"""

import random
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ wait_n function """
    # create the list that will be returned
    list_delay = []
    # spawn wait_random n times
    for i in range(n):
        # with the specified max_delay.
        delay = random.uniform(0, max_delay)
        # add each delay to the list
        list_delay.append(delay)
    return sorted(list_delay)
