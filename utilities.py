from typing import List, Tuple
import itertools


class Utilities:
    @staticmethod
    def range_diff(range1: Tuple[int, int], range2: Tuple[int, int]) -> List[Tuple[int, int]]:
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
    def multi_range_diff(range1_list: List[Tuple[int, int]],
                         range2_list: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
        for range2 in range2_list:
            range1_list = list(
                itertools.chain(*[Utilities.range_diff(range1, range2) for range1 in range1_list]))
        return range1_list
