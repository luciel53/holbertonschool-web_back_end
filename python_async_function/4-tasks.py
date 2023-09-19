#!/usr/bin/env python3
"""
Take the code from wait_n and alter it into a new function task_wait_n.
The code is nearly identical to wait_n except task_wait_random is being called.
"""

import asyncio
import random
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ task_wait_n function """
    # create the list of tasks
    tasks = []
    # calls task_wait_random n times and stores it to the list of tasks
    tasks = [task_wait_random(max_delay) for i in range(n)]
    # await all the tasks are finished
    finished_tasks = await asyncio.gather(*tasks)
    # add each delay to the list
    return sorted(finished_tasks)
