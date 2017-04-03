import unittest
from tmxtools import validate_translation_memory

class allTests(unittest.TestCase):
    def testReading(self):
        self.assertTrue(validate_translation_memory.is_tmx_valid("tests/testfiles/test1.tmx"))


def main():
    unittest.main()

if __name__ == '__main__':
    main()
