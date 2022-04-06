import unittest 
from src.pub  import *
from src.drink import *
from src.customer import *

class TestPub(unittest.TestCase):
    def setUp(self):
        self.pub = Pub("The Droothy Arms")
        self.drink1 = Drink("beer", 3, 2)
        self.drink2 = Drink("wine", 6, 3)
        self.drink3 = Drink("gin", 8, 5)
        self.customer = Customer("Billy", 24, 1000, "beer")
        self.customer2 = Customer("Sarah", 16, 300, "wine")
        

    def test_pub_has_name(self):
        self.assertEqual("The Droothy Arms", self.pub.name)

    def test_pub_has_till(self):
        self.assertEqual(0, self.pub.till)

    def test_sale_of_drink(self):
        self.customer.reduce_wallet(self.drink1.price)
        self.assertEqual(997, self.customer.wallet)
        self.pub.increase_till(self.drink1.price)
        self.assertEqual(3, self.pub.till)

    def test_age_challenge(self):
        self.assertEqual("What would you like to drink?", self.pub.age_challenge(self.customer.age))

    def test_age_challenge2(self):
        self.assertEqual("No", self.pub.age_challenge(self.customer2.age))

    def test_how_drunk_customer_is(self):
        self.assertEqual(0, self.customer.drunkeness)

    def test_serve_drink(self):
        self.pub.serve_a_drink(self.customer.drink_of_choice)
        self.assertEqual(2, self.customer.drunkeness)
