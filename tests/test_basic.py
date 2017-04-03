import unittest
# import the package
import tmxtools
from tmxtools import validate_translation_memory

# Here's our "unit".
def IsOdd(n):
    return n % 2 == 1

# Here's our "unit tests".
class IsOddTests(unittest.TestCase):

    def testOne(self):
        self.failUnless(IsOdd(1))

    def testTwo(self):
        self.failIf(IsOdd(2))
    def testThree(self):
        self.failIf(IsOdd(4))
    def testFour(self):
        self.failIf(IsOdd(6))

class  allTests(unittest.TestCase):
    def testReading(self):
        self.assertTrue(validate_translation_memory.is_tmx_valid("test1.tmx"))


def main():
    unittest.main()

if __name__ == '__main__':
    main()
