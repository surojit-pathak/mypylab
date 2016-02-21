import unittest
import solution
import sys

from contextlib import contextmanager
from StringIO import StringIO

@contextmanager
def captured_output():
    new_out, new_err = StringIO(), StringIO()
    old_out, old_err = sys.stdout, sys.stderr
    try:
        sys.stdout, sys.stderr = new_out, new_err
        yield sys.stdout, sys.stderr
    finally:
        sys.stdout, sys.stderr = old_out, old_err
    
class MyTest(unittest.TestCase):
    def _test_testcase(self, testf):
        with captured_output() as (out, err):
            fp = open(testf, 'r')
            solution.main(fp)
        exp = StringIO(fp.read())
        self.assertEqual(out.getvalue(), exp.getvalue())

    def test_testcase3(self):
        self._test_testcase('./testcase3.txt')

    def test_testcase2(self):
        self._test_testcase('./testcase2.txt')

    def test_testcase1(self):
        self._test_testcase('./testcase1.txt')

    def _test_testcase4(self):
        self._test_testcase('./testcase4.txt')

    def _test_input_run(self):
        fp = open('./testcase4.txt', 'r')
        solution.main(fp)

if __name__ == '__main__':
    unittest.main()
