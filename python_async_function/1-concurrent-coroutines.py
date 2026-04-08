#!/usr/bin/env python3
"""Defines the 'wait_n' asynchronous coroutine."""
import typing
wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> typing.List[float]:
    """Executes wait_random n times with a specified max_delay.

    Parameters:
        n (int): The number of times to run the function.
        max_delay (int): The max delay to use.

    Returns:
        (list[float]) A list of the delays waited."""

    return [wait_random(max_delay) for i in range(n)]
