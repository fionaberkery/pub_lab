
from src.drink import *

class Pub:
    def __init__(self, name):
        self.name = name
        self.till = 0


    def increase_till(self, amount):
        self.till += amount

    def age_challenge(self, age):
        if age >= 18:
            return "What would you like to drink?"
        else:
            return "No"
        

    def serve_a_drink(self, drink):
        # get the units of the drink
        # add these units to drunk level
