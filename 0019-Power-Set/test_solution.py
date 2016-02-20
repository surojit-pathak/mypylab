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
    def test_penny_and_nickel(self):
        with captured_output() as (out, err):
            fp = open('./testcase1.txt', 'r')
            solution.main(fp)
        exp = StringIO(fp.read())
        self.assertEqual(out.getvalue(), exp.getvalue())

    def test_quarter_and_dime(self):
        with captured_output() as (out, err):
            fp = open('./testcase2.txt', 'r')
            solution.main(fp)
        exp = StringIO(fp.read())
        self.assertEqual(out.getvalue(), exp.getvalue())

    def _test_input_run(self):
        fp = open('./testcase1.txt', 'r')
        solution.main(fp)

if __name__ == '__main__':
    unittest.main()
