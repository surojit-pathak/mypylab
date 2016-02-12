import unittest
import solution

class MyTest(unittest.TestCase):
    def test_with_panagram(self):
        self.assertEqual(solution.find_max_xor(10, 14), 7)

if __name__ == '__main__':
    unittest.main()
