#!/usr/bin/env python3
"""
Import async_comprehension from the previous file and write a measure_runtime
coroutine that will execute async_comprehension four times in parallel using
asyncio.gather.

measure_runtime should measure the total runtime and return it.

Notice that the total runtime is roughly 10 seconds, explain it to yourself.
"""


import asyncio
import time
from typing import List

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ measure_runtime function """
    # start time
    start_time = time.time()
    # Executes async_comprehension 4 times in parallel using asyncio.gather
    tasks = [async_comprehension() for i in range(4)]
    # wait for async_comprehension tasks finished
    await asyncio.gather(*tasks)
    # end time
    end_time = time.time()
    # compute the total time
    total_time = end_time - start_time
    return total_time
