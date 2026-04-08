#!/usr/bin/env python3
"""Defines the 'task_wait_random' function."""
import asyncio
wait_random = __import__("0-basic_async_syntax").wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Creates an asyncio.Task to run wait_random with a specific delay.

    Parameters:
        max_delay (int): The maximum delay to use.

    Returns:
        (asyncio.Task)"""

    return asyncio.create_task(wait_random(max_delay))
