#!/usr/bin/env python3
"""Defines the 'async_comprehension' coroutine."""
import asyncio
import typing
async_generator = __import__("0-async_generator").async_generator


async def async_comprehension() -> typing.List[float]:
    """Collects 10 numbers from async_generator and returns them.

    Returns: (list[float])"""
    return [v async for v in async_generator()]
