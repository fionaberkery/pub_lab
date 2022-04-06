import unittest
from src.drink import *

class TestDrink(unittest.TestCase):
    def setUp(self):
        self.drink1 = Drink("beer", 3, 2)
        self.drink2 = Drink("wine", 6, 3)
        self.drink3 = Drink("gin", 8, 5)

    def test_drink_has_name(self):
        self.assertEqual("beer", self.drink1.name)

    def test_drink_has_name(self):
        self.assertEqual("wine", self.drink2.name)
    
    def test_drink_has_price(self):
        self.assertEqual(3, self.drink1.price)

