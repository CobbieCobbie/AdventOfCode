import unittest

import AdventOfCode.A_DayOne.day_one as day_one

class TestDayOne(unittest.TestCase):
    
    def test_day_one(self):
        
        self.assertEqual(day_one.compare(3,4),1)
        self.assertEqual(day_one.compare(1,1),0)
        self.assertFalse(day_one.compare(3,4) < 0)
        self.assertTrue(day_one.list_check([1,2,3] , [4,5,6]))


if __name__ == '__main__':
    unittest.main()
