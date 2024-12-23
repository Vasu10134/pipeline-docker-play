import unittest
from app import greet

class TestApp(unittest.TestCase):
    def test_greet(self):
        self.assertEqual(greet(), None)  # This is just for demonstration

if __name__ == "__main__":
    unittest.main()
