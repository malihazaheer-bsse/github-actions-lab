import unittest

class TestApp(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(2 + 3, 6)

if __name__ == "__main__":
    unittest.main()
