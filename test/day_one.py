import unittest

import AdventOfCode.DayOne.day_one as day_one

class DayOne(unittest.TestCase):
    
    def day_one(self):
        
        self.assertEqual(day_one.compare(3,4),1)
        self.assertEqual(day_one.compare(1,1),0)
        self.assertFalse(day_one.compare(3,4) < 0)
        self.assertTrue(day_one.list_check([1,2,3] , [4,5,6]))


if __name__ == '__main__':
    unittest.main()
