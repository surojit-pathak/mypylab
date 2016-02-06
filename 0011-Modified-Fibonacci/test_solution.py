import unittest
import solution

class MyTest(unittest.TestCase):
    def test_input1(self):
        fp = open('./input1.txt', 'r')
        self.assertEqual(solution.main(fp), 5)

    def test_input2(self):
        fp = open('./input2.txt', 'r')
        self.assertEqual(solution.main(fp), 84266613096281243382112)
if __name__ == '__main__':
    unittest.main()
