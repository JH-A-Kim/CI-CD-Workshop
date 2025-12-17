import unittest
from adder import adder

class TestAdder(unittest.TestCase):
    def test_add_positive_numbers(self):
        self.assertEqual(adder(2, 3), 5)

if __name__ == '__main__':
    unittest.main()