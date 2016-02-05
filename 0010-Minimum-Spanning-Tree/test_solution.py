import unittest
import solution

class MyTest(unittest.TestCase):
    def test_input1(self):
        fp = open('./input1.txt', 'r')
        self.assertEqual(solution.main(fp), 15)

    def test_input2(self):
        fp = open('./input2.txt', 'r')
        self.assertEqual(solution.main(fp), 200)

    def test_input3(self):
        fp = open('./input3.txt', 'r')
        self.assertEqual(solution.main(fp), 6359060)

if __name__ == '__main__':
    unittest.main()
