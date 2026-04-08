#!/usr/bin/env python3
"""Defines the 'sum_mixed_list' function."""
import typing


def sum_mixed_list(mxd_lst: typing.List[typing.Union[int, float]]) -> float:
    """Returns the sum of an array of integers and floats.

    Parameters:
        mxd_lst (list[int, float]): The list of numbers to sum.

    Returns: (float) The sum of all numbers in the list."""

    return sum(mxd_lst)
