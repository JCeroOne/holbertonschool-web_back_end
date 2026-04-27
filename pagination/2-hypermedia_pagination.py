#!/usr/bin/env python3
"""Defines the index_range function."""
import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
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
        assert (isinstance(page, int) and isinstance(page_size, int))
        assert (page > 0 and page_size > 0)

        bounds = index_range(page, page_size)
        rows = []

        for i in range(bounds[0], bounds[1]):
            try:
                rows.append(self.dataset()[i])
            except IndexError:
                return []

        return rows

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """Get hypermedia pagination."""
        assert (isinstance(page, int) and isinstance(page_size, int))
        assert (page > 0 and page_size > 0)

        pages = math.floor(len(self.dataset()) / page_size)
        prv = page - 1 if page > 1 else None
        nxt = page + 1 if page <= pages - 1 else None
        data = self.get_page(page, page_size)
        res = {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": nxt,
            "prev_page": prv,
            "total_pages": pages
        }

        return res
