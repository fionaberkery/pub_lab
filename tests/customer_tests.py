import unittest
from src.customer import *

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Billy", 24, 1000)

    def test_customer_has_money(self):
        self.assertEqual(1000, self.customer.wallet)

    