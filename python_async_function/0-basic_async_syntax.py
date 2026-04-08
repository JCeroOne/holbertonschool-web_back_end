#!/usr/bin/env python3
"""Defines the asynchronous 'wait_random' coroutine."""
import asyncio


async def wait_random(max_delay: float) -> float:
    """Waits a random delay and then returns said delay.

    Parameters:
        max_delay (float): The maximum delay the program can wait.

    Returns:
        (float) The delay that was waited."""

    delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
