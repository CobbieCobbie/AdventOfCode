import unittest

import AdventOfCode.DayTwo.day_two as day_two

class TestDayTwo(unittest.TestCase):

    def test_safeness(self):
        self.assertTrue(day_two.safeness_check([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
        self.assertTrue(day_two.safeness_check([1, 4, 7, 10]))
        self.assertFalse(day_two.safeness_check([1, 3, 7, 9, 11]))
        self.assertTrue(day_two.safeness_check([]))

    def test_isIncreasing(self):
        self.assertTrue(day_two.isIncreasing([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
        self.assertTrue(day_two.isIncreasing([1, 4, 7, 10]))
        self.assertTrue(day_two.isIncreasing([1, 3, 7, 9, 11]))
        self.assertTrue(day_two.isIncreasing([]))
        self.assertFalse(day_two.isIncreasing([1, 3, 2, 4, 5, 6, 7, 8, 3]))

    def test_isDecreasing(self):
        self.assertTrue(day_two.isDecreasing([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))
        self.assertFalse(day_two.isDecreasing([1, 4, 7, 10]))
        self.assertTrue(day_two.isDecreasing([]))

    def test_correctable(self):
        self.assertTrue(day_two.correctable([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
        self.assertTrue(day_two.correctable([1, 4, 7, 10]))
        self.assertTrue(day_two.correctable([1, 4, 7, 9, 11]))
        self.assertTrue(day_two.correctable([1, 7, 9, 11]))
        self.assertTrue(day_two.correctable([7, 1, 9, 11]))
        self.assertTrue(day_two.correctable([7, 9, 1, 11]))
        self.assertTrue(day_two.correctable([7, 9, 11, 1]))
        self.assertTrue(day_two.correctable([7, 6, 4, 2, 1]))
        self.assertTrue(day_two.correctable([1,3,2,4,5]))
        self.assertTrue(day_two.correctable([8,6,4,4,1]))
        self.assertTrue(day_two.correctable([1,3,6,7,9]))
        
        self.assertFalse(day_two.correctable([1, 2, 7, 8, 9]))
        self.assertFalse(day_two.correctable([9, 7, 6, 2, 1]))
        

if __name__ == "__main__":
    unittest.main()
