import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from src.CountClump import CountClump

class TestCountClump(unittest.TestCase):

    def test_no_clumps(self):
        self.assertEqual(CountClump.count_clumps([]), 0)
        self.assertEqual(CountClump.count_clumps(None), 0)
        self.assertEqual(CountClump.count_clumps([1]), 0)
        self.assertEqual(CountClump.count_clumps([1, 2, 3, 4]), 0)

    def test_one_clump(self):
        self.assertEqual(CountClump.count_clumps([1, 2, 2, 3]), 1)
        self.assertEqual(CountClump.count_clumps([1, 2, 3, 3]), 1)
        self.assertEqual(CountClump.count_clumps([1, 1, 1, 2, 3]), 1)

    def test_multiple_clumps(self):
        self.assertEqual(CountClump.count_clumps([1, 2, 2, 2, 3, 3]), 2)
        

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(TestCountClump))
    runner = unittest.TextTestRunner()
    runner.run(suite)