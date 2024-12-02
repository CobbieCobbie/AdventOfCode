import unittest

import AdventOfCode.DayTwo.day_two as day_two

class TestDayTwo(unittest.TestCase):

    def test_safeness(self):
        self.assertTrue(day_two.safeness_check([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
        self.assertTrue(day_two.safeness_check([1, 4, 7, 10]))
        self.assertFalse(day_two.safeness_check([1, 3, 7, 9, 11]))
        self.assertTrue(day_two.safeness_check([]))


if __name__ == "__main__":
    unittest.main()
