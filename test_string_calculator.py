import unittest
from string_calculator import add

class test_calculator(unittest.TestCase):
    
    def test_empty_string(self):
        result = add("")
        self.assertEqual(result, 0)
        
unittest.main()