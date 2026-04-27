#!/usr/bin/env python3
"""Defines the index_range function."""
import csv
import math
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


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Retrieves the entries in a given page."""
        rows = []
        with open("Popular_Baby_Names.csv") as file:
            reader = csv.reader(f)
            for i, row in enumerate(reader):
                if a <= i < b:
                    rows.append(row)
                elif i >= b:
                    break
