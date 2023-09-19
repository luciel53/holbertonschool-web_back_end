#!/usr/bin/env python3
"""
Import async_generator from the previous task and then write a coroutine
called async_comprehension that takes no arguments.

The coroutine will collect 10 random numbers using an async comprehensing
over async_generator, then return the 10 random numbers.
"""

import asyncio
import random


async def async_generator():
    """ async_generetor function """
    for i in range(0, 10):
        asyncio.sleep(1)
        yield random.uniform(0, 10)
