import unittest
from tmxtools import validate_translation_memory
from tmxtools import split_translation_memory


class allTests(unittest.TestCase):
    def testReading(self):
        self.assertTrue(
            validate_translation_memory.is_tmx_valid(
                "tests/testfiles/test1.tmx"))

    def testReadsCorrect(self):
        inputsread = []
        outputsread = []
        for inputsentence, outputsentence in split_translation_memory.get_input_output(
                "tests/testfiles/test1.tmx"):
            inputsread.append(inputsentence)
            outputsread.append(outputsentence)
        self.assertEqual(len(inputsread), 3)
        self.assertEqual(len(outputsread), 3)
        self.assertEqual(inputsread[0], "Test this input")
        self.assertEqual(outputsread[0], "Test deze invoer")


def main():
    unittest.main()


if __name__ == '__main__':
    main()
