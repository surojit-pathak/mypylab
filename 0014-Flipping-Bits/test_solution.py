import unittest
import solution


class MyTest(unittest.TestCase):
    def test1(self):
        self.assertEqual(solution.flip_bits(2147483647), 2147483648)

    def test2(self):
        self.assertEqual(solution.flip_bits(1), 4294967294)

    def test3(self):
        self.assertEqual(solution.flip_bits(0), 4294967295)

if __name__ == '__main__':
    unittest.main()
