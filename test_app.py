import unittest
# Import your functions from app.py
from app import get_message 

# Your test code MUST be wrapped in a class inheriting from unittest.TestCase
class TestMyApplication(unittest.TestCase):
    
    # Every test function name MUST start with the prefix "test_"
    def test_application_output(self):
        result = get_message()
        self.assertEqual(result, "Hello from Windows Jenkins!")
#testing
if __name__ == '__main__':
    unittest.main()
