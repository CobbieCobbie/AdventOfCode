import unittest
import AdventOfCode.E_DayFive.day_five as five


class TestDayFive(unittest.TestCase):
    def test_main(self):
        self.assertEqual(five.main(), 5)


if __name__ == "__main__":
    unittest.main()