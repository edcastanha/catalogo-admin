import unittest

# Test de Category
from category import Category

class TestCategory(unittest.TestCase):
    def test_name_is_required(self):
        with self.assertRaises(TypeError):
            Category()
        

if __name__ == "__main__":
    unittest.main()
    
