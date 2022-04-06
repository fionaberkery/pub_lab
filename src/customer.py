class Customer:
    def __init__(self, name, age, wallet, drink_of_choice):
        self.name = name
        self.age = age
        self.wallet = wallet
        self.drink_of_choice = drink_of_choice
        self.drunkeness = 0
        
    def reduce_wallet(self, amount):
        self.wallet -= amount

