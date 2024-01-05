#!/usr/bin/env python3
'''async file'''
import asyncio
import random
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''measure runtime'''
    start_time = time.time()
    my_list = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*my_list)

    end_time = time.time()
    return (end_time - start_time)
