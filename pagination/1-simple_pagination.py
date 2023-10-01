#!/usr/bin/env python3
"""
Copy index_range from the previous task and the following class into your code

Implement a method named get_page that takes two integer arguments page with
 default value 1 and page_size with default value 10.

    You have to use this CSV file (same as the one presented at the top of
    the project)
    Use assert to verify that both arguments are integers greater than 0.
    Use index_range to find the correct indexes to paginate the dataset
    correctly and return the appropriate page of the dataset (i.e. the
    correct list of rows).
    If the input arguments are out of range for the dataset, an empty list
    should be returned.

"""


import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> tuple:
    """ index range function """
    end_index = page_size * page
    start_index = end_index - page_size
    return (start_index, end_index)


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
        """ get page method"""
        # check if page and page_size are the positive numbers and int
        assert type(page) == int and type(page_size) == int
        assert page > 0 and page_size > 0
        # compute start and end indexes
        indexes = index_range(page, page_size)
        # get dataset
        dataset = self.dataset()
        # computes length of dataset
        data_len = len(dataset)
        # check if indexes are within bounds
        if indexes[0] < data_len and indexes[1] <= data_len:
            return dataset[indexes[0]:indexes[1]]
        return []
