import unittest
import solution

class MyTest(unittest.TestCase):
    def test_including_range_ends(self):
        self.assertEqual(solution.count_squares(1, 25), 5)

    def test_excluding_range_ends(self):
        self.assertEqual(solution.count_squares(2, 24), 3)

    def test_range_with_no_result(self):
        self.assertEqual(solution.count_squares(17, 24), 0)

    def test_single_point_range_positive(self):
        self.assertEqual(solution.count_squares(16, 16), 1)

    def test_single_point_range_negative(self):
        self.assertEqual(solution.count_squares(17, 17), 0)

if __name__ == '__main__':
    unittest.main()
