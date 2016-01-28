import unittest
import solution

pangram = 'pangram'
not_pangram = 'not pangram'

class MyTest(unittest.TestCase):
    def test_with_panagram(self):
        s = 'We promptly judged antique ivory buckles for the next prize'
        self.assertEqual(solution.find_if_pangram(s), pangram)

    def test_with_not_panagram(self):
        s = 'We promptly judged antique ivory buckles for the prize'
        self.assertEqual(solution.find_if_pangram(s), not_pangram)

    def test_with_not_panagram_with_space(self):
        s = 'We promptly judged antique ivory buckles for the prize    '
        self.assertEqual(solution.find_if_pangram(s), not_pangram)

    def test_with_not_panagram_with_non_alpha(self):
        s = 'We ... promptly judged antique ivory buckles for the next prize'
        self.assertEqual(solution.find_if_pangram(s), pangram)

    def test_with_not_panagram_with_upper_case(self):
        s = 'We Promptly Judged antique ivory buckles for the next prize'
        self.assertEqual(solution.find_if_pangram(s), pangram)

if __name__ == '__main__':
    unittest.main()
