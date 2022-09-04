import unittest
from string_calculator import add

class test_calculator(unittest.TestCase):
    
    def test_empty_string(self):
        result = add("")
        self.assertEqual(result, 0)
    
    def test_comma_in_string(self):
        result = add("1")
        self.assertEqual(result, 1)
        result = add("10")
        self.assertEqual(result, 10)
        result = add("1,2")
        self.assertEqual(result, 3)
        result = add("10,20")
        self.assertEqual(result, 30)
        
unittest.main()