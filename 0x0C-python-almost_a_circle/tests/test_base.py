from unittest import TestCase, main
"""Unit testing the Rectangle class"""

from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestBase(TestCase):
    """Square instances unittesting class"""
    def setUp(self):
        """test units setup function"""
        self.S1 = Base(5)
        self.S2 = Base(10)
        self.S3 = Base(6)

    def test_size(self):
        """Testing size property"""
        self.assertEqual(self.S1.id, 5)
        self.assertEqual(self.S2.id, 10)
        self.assertEqual(self.S3.id, 6)
        self.S1.size, self.S2.size, self.S3.size = 20, 40, 60
        self.assertEqual(self.S1.size, 20)
        self.assertEqual(self.S2.size, 40)
        self.assertEqual(self.S3.size, 60)

if __name__ == '__main__':
    main()
