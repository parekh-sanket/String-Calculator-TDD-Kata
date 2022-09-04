import unittest
from string_calculator import add

class test_calculator(unittest.TestCase):
    
    def test_empty_string(self):
        result = add("")
        self.assertEqual(result, 0)
    
    def test_comma_in_string(self):
        result = add("1")
        self.assertEqual(result, 1)
        result = add("10,20")
        self.assertEqual(result, 30)
    
    def test_unknown_amount_of_numbers_in_string(self):
        result = add("1,2,3")
        self.assertEqual(result, 6)
        result = add("50,80,60,70")
        self.assertEqual(result, 260)
        
    def test_alphabets_in_string(self):
        result = add("1,2,a,b")
        self.assertEqual(result, 6)
        result = add("10,20,b,z")
        self.assertEqual(result, 58)
    
    def test_negative_in_string(self):
        # add("45,-45") # print negative number in exception
        self.assertRaises(ValueError, add ,"45,-45")
        # add("-49,-45,-100") # print all negative number in exception
        self.assertRaises(ValueError, add ,"-49,-45,-100")

    def test_larger_then_1000_in_string(self):
        result = add("2,10001")
        self.assertEqual(result, 2)
    
    def test_new_line_in_string(self):
        result = add("1\n2,3")
        self.assertEqual(result, 6)
        result = add("1\n2,3")
        self.assertEqual(result, 6)
        
unittest.main()