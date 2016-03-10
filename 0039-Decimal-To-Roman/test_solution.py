import unittest
import solution
import sys
import os

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

    def test_all_testcases(self):
        for f in os.listdir('.'):
            if f.startswith('testcase'):
                print f
                self._test_testcase('./' + f)

if __name__ == '__main__':
    unittest.main()
