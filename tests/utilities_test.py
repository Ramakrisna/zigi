from utilities import Utilities
import unittest


class TestSum(unittest.TestCase):
    range1 = (1, 100)
    range2 = (10, 40)
    range3 = (20, 30)
    range4 = (25, 55)
    range5 = (70, 90)
    range6 = (-20, -10)
    range7 = (-10, 10)
    range8 = (100, 1)
    range_list = [range3, range5, range2, range4]

    def test_filter_and_organize_ranges(self):
        self.assertEqual(Utilities.filter_and_organize_ranges([]), [])
        self.assertEqual(Utilities.filter_and_organize_ranges([self.range2]), [(10, 40)])
        self.assertEqual(Utilities.filter_and_organize_ranges([self.range2, self.range3]), [(10, 40)])
        self.assertEqual(Utilities.filter_and_organize_ranges([self.range2, self.range4]), [(10, 55)])
        self.assertEqual(Utilities.filter_and_organize_ranges(self.range_list), [(10, 55), (70, 90)])

    def test_filter_sub_ranges_from_whole_range(self):
        with self.assertRaises(Exception):
            Utilities.filter_sub_ranges_from_whole_range(self.range8, [()])
        self.assertEqual(Utilities.filter_sub_ranges_from_whole_range(self.range1, [self.range6]),
                         [(1, 100)])
        self.assertEqual(Utilities.filter_sub_ranges_from_whole_range(self.range1, [self.range7]),
                         [(10, 100)])
        self.assertEqual(Utilities.filter_sub_ranges_from_whole_range(self.range1, self.range_list),
                         [(1, 10), (55, 70), (90, 100)])


if __name__ == '__main__':
    unittest.main()
