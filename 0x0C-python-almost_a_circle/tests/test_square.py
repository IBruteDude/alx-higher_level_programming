from unittest import TestCase, main
"""Unit testing the Rectangle class"""

from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestSquare(TestCase):
    """Square instances unittesting class"""
    def setUp(self):
        self.S1 = Square(5)
        self.S2 = Square(10, 0, 0)
        self.S3 = Square(6, 2, 3)

    def test_size(self):
        self.assertEqual(self.S1.size, 5)
        self.assertEqual(self.S2.size, 10)
        self.assertEqual(self.S3.size, 6)
        self.S1, self.S2, self.S3 = 20, 40, 60
        self.assertEqual(self.S1, 20)
        self.assertEqual(self.S2, 40)
        self.assertEqual(self.S3, 60)

if __name__ == '__main__':
    main()
