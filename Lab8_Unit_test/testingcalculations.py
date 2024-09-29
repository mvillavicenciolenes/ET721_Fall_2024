"""
Example 2: Calculation testing
Michael Villavicencio
"""

import unittest
import calculations

class testingCalculations(unittest.TestCase):
    def test_addthreenumbers(self):
        self.assertEqual(calculations.addthreenumbers(1, 2, 3), 6)
        self.assertEqual(calculations.addthreenumbers(5, 3), 8)
        self.assertEqual(calculations.addthreenumbers(9), 9)
        self.assertEqual(calculations.addthreenumbers(), 0)

    def test_subtracttwonumbers(self):
        self.assertEqual(calculations.subtracttwonumbers(2, 8), -6)
        self.assertEqual(calculations.subtracttwonumbers(8, 2), 6)

    def test_dividetwonumbers(self):
        # test normal division
        self.assertEqual(calculations.dividetwonumbers(8, 2), 4)
        self.assertEqual(calculations.dividetwonumbers(-8, 2), -4)
        # float comparison
        self.assertEqual(calculations.dividetwonumbers(7, 2), 3.5)

    # division by zero
    def test_dividebyzero(self):
        self.assertIsNone(calculations.dividetwonumbers(10, 0))
        self.assertIsNone(calculations.dividetwonumbers(0, 0))
    
    # non-numeric testing
    def test_nonnumericvalues(self):
        self.assertIsNone(calculations.dividetwonumbers("p", 2))
        self.assertIsNone(calculations.dividetwonumbers(10, "n"))
    
    # any other exceptions
    def test_unexpected_exception(self):
        # flag raises if 'Exception' is detected
        with self.assertRaises(Exception):
            calculations.dividetwonumbers()

if __name__ == "__main__":
    unittest.main()