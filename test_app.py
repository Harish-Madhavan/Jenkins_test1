import unittest
# Import your functions from app.py
from app import your_function_name 

# Your test code MUST be wrapped in a class inheriting from unittest.TestCase
class TestMyApplication(unittest.TestCase):
    
    # Every test function name MUST start with the prefix "test_"
    def test_application_output(self):
        result = your_function_name()
        self.assertEqual(result, "Expected Output")

if __name__ == '__main__':
    unittest.main()
