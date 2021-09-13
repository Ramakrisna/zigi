from typing import List
import itertools


class Utilities:
    @staticmethod
    def range_diff(range1: tuple, range2: tuple) -> List[tuple]:
        """
        A method that takes 2 tuples of comparables that represent a range, and return all the ranges that are part of
        the first tuple and not in the second tuple.
        """
        start1, end1 = range1
        start2, end2 = range2
        endpoints = sorted((start1, start2, end1, end2))
        result = []
        if endpoints[0] == start1 and endpoints[1] != start1:
            result.append((endpoints[0], endpoints[1]))
        if endpoints[3] == end1 and endpoints[2] != end1:
            result.append((endpoints[2], endpoints[3]))
        return result

    @staticmethod
    def multi_range_diff(range1_list: List[tuple], range2_list: List[tuple]) -> List[tuple]:
        """
        A method that takes 2 lists with tuples of comparables that represent ranges, and return all the ranges that are
        part of the first list and not in the second one.
        """
        for range2 in range2_list:
            range1_list = list(
                itertools.chain(*[Utilities.range_diff(range1, range2) for range1 in range1_list]))
        return range1_list
