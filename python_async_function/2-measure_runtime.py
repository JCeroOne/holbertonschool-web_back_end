#!/usr/bin/env python3
"""Defines the 'measure_time' function."""
import time
import asyncio
wait_n = __import__("1-concurrent_coroutines").wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measures the execution time for wait_n.

    Parameters:
        n (int): The number of times to run wait_random.
        max_delay (int): The max delay to use in wait_random.

    Returns:
        (float) The average time it takes to run each wait function."""

    start: float = time.time()
    asyncio.run(wait_n(n, max_delay))
    return (time.time() - start) / n
