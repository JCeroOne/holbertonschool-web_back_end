#!/usr/bin/env python3
"""Defines the 'wait_n' asynchronous coroutine."""
import asyncio
import typing
task_wait_random = __import__("3-tasks").task_wait_random


async def wait_n(n: int, max_delay: int) -> typing.List[float]:
    """Uses task_wait_random to spawn n tasks with a specified max_delay.

    Parameters:
        n (int): The number of tasks to spawn.
        max_delay (int): The max delay to use.

    Returns:
        (list[float]) A list of the delays waited."""

    delays: typing.List[float] = []

    tasks = [task_wait_random(max_delay) for _ in range(n)]

    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)

    return delays
