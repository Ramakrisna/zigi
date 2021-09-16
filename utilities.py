from typing import List
import itertools


class Utilities:
    @staticmethod
    def filter_and_organize_ranges(sub_ranges: List[tuple]) -> List[tuple]:
        """
        This method accepts a list of tuples of ranges and filters and then organizes them into a new list of ranges
        where the ranges are cleared of duplicates/overlapping and sorted by order.
        """
        if len(sub_ranges) <= 1:
            return sub_ranges
        # Sort the list of ranges by each range's starting point
        sorted_sub_ranges = sorted(sub_ranges, key=lambda x: x[0])

        new_sub_ranges = []
        temp_range = sorted_sub_ranges[0]
        idx = 1
        while idx < len(sorted_sub_ranges):
            if sorted_sub_ranges[0] > sorted_sub_ranges[1]:
                raise ValueError(f'The provided range {sorted_sub_ranges[idx]} to remove ranges from is not formatted'
                                 f'correctly, it should be (start of range, end of range)')
            if temp_range[1] < sorted_sub_ranges[idx][0]:
                new_sub_ranges.append((temp_range[0], temp_range[1]))
                temp_range = sorted_sub_ranges[idx]
            elif temp_range[0] <= sorted_sub_ranges[idx][0] and temp_range[1] < sorted_sub_ranges[idx][1]:
                temp_range = (temp_range[0], sorted_sub_ranges[idx][1])
            idx += 1
            if temp_range and idx == len(sorted_sub_ranges):
                new_sub_ranges.append(temp_range)
        return new_sub_ranges

    @staticmethod
    def filter_sub_ranges_from_whole_range(whole_range: tuple, sub_ranges: List[tuple]) -> List[tuple]:
        """
        This method accepts a large range and a list of sub ranges in that range, and returns a list of all the sub
        ranges that are part of the large range but not in the sub ranges list.
        """
        if whole_range[0] > whole_range[1]:
            raise ValueError(f'The provided range {whole_range} is not formatted correctly, it should be'
                             f'(start of range, end of range)')
        if len(sub_ranges) == 1 and sub_ranges[0] == whole_range:
            return []
        filtered_sub_ranges = Utilities.filter_and_organize_ranges(sub_ranges) if len(sub_ranges) > 1 else sub_ranges
        new_ranges = []
        temp_range_start = whole_range[0]
        for sub_range in filtered_sub_ranges:
            if sub_range[0] < temp_range_start:
                if sub_range[1] > temp_range_start:
                    temp_range_start = sub_range[1]
                continue
            new_ranges.append((temp_range_start, sub_range[0]))
            temp_range_start = sub_range[1]
        if temp_range_start < whole_range[1]:
            new_ranges.append((temp_range_start, whole_range[1]))
        return new_ranges
