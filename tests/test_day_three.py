import re
import unittest

import AdventOfCode.DayThree.day_three as three

class TestDayThree(unittest.TestCase):
    def test_regex(self):
        self.assertTrue(re.fullmatch(three.get_regex_one(), "mul(1,3)"))

    def test_regex_fail(self):
        self.assertFalse(re.fullmatch(three.get_regex_one(), "mul(1,3"))

    def test_teststring(self):
        test_string = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
        test_result = ["mul(2,4)", "mul(5,5)", "mul(11,8)", "mul(8,5)"]
        self.assertEqual(re.findall(three.get_regex_one(), test_string), test_result)

    def test_mul(self):
        self.assertEqual(three.eval("mul(2,4)"), 8)
    
if __name__ == '__main__':
    unittest.main()
