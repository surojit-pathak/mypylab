import unittest
import solution

class MyTest(unittest.TestCase):
    def test_with_all_positive(self):
        arr = [1, 2, 3, 4]
        self.assertEqual(solution.find_maximum_sum_of_subarray(arr), (10, 10))

    def test_with_all_negative(self):
        arr = [-1, -2, -3, -4]
        self.assertEqual(solution.find_maximum_sum_of_subarray(arr), (-1, 0))

    def test_with_mix(self):
        arr = [2, -1, 2, 3, 4, -5]
        self.assertEqual(solution.find_maximum_sum_of_subarray(arr), (10, 11))

if __name__ == '__main__':
    unittest.main()
