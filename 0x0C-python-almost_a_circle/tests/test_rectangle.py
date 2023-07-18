from unittest import TestCase, main
"""Unit testing the Rectangle class"""

from models import base
from models.rectangle import Rectangle
from models.square import Square

class TestRectangle(TestCase):
    """Rectangle instances unittesting class"""
    def setUp(self):
        self.Rectangle1 = Rectangle(1, 2)
        self.Rectangle2 = Rectangle(3, 4)
    def test_(self):
        Rectangle
        self.Rectangle1.to_json_string()

if __name__ == '__main__':
    main()
