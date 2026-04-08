#!/usr/bin/env python3
"""Defines the 'element_length' function."""
import typing


def element_length(
        lst: typing.Iterable[typing.Sequence]
    ) -> typing.List[typing.Tuple[typing.Sequence, int]]:
    """Returns the contents and length of each element in a list.

    Parameters:
        lst (list[*]): The list.

    Returns: (*, int) Exactly what it says above."""

    return [(i, len(i)) for i in lst]
