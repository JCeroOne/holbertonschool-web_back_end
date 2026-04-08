#!/usr/bin/env python3
"""Defines the 'async_generator' coroutine."""
import asyncio
import random
import typing


async def async_generator() -> typing.Generator[float]:
    """Loops 10 times, returning a value in the [0, 10] range after 1 s."""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
