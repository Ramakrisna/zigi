from utilities import Utilities
import unittest


class TestSum(unittest.TestCase):
    range1 = (1, 10)
    range2 = (2, 4)
    range3 = (6, 8)

    def test_range_diff(self):
        self.assertEqual(Utilities.range_diff(self.range1, self.range2), [(1, 2), (4, 10)])

    def test_multi_range_diff(self):
        self.assertEqual(Utilities.multi_range_diff([self.range1], [self.range2, self.range3]),
                         [(1, 2), (4, 6), (8, 10)])


if __name__ == '__main__':
    unittest.main()
