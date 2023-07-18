from unittest import TestCase, main
"""Unit testing the Base class"""

from ...models import Base
from ...models.rectangle import Rectangle
from ...models.square import Square

class TestBase(TestCase):
    def setUp(self):
        self.Rectangle1 = Rectangle(1, 2)
        self.Rectangle2 = Rectangle(3, 4)
    def test_to_json_file(self):
        self.Rectangle1.to_json_string()

if __name__ == '__main__':
    main()
