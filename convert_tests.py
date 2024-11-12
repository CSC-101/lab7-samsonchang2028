from convert import string_to_float
import unittest
class TestCases(unittest.TestCase):
    def test_str_to_float_1(self):
        values = '10'
        results = string_to_float(values)
        expected = 10.0
        self.assertEqual(expected, results)
    def test_str_to_float_2(self):
        values = 'ten'
        results = string_to_float(values)
        expected = None
        self.assertEqual(expected, results)

if __name__ == '__main__':
    unittest.main()