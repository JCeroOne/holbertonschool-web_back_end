#!/usr/bin/env python3
"""Defines the index_range function."""
import typing


def index_range(page: int, page_size: int) -> typing.Tuple[int, int]:
    """Returns the edge indices of the given page.

    Parameters:
    page (int): The page number (1-indexed)
    page_size (int): Number of results per page.

    Returns: (int, int)
    The index interval of the page, [a, b)
    """
    return ((page - 1) * page_size, page * page_size)
