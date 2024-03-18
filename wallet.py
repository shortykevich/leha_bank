from uuid import uuid4

from currencies import Currencies
from currencies import get_symbol



class Wallet:
    def __init__(self, currency: Currencies, login):
        self.currency = currency
        self._balance = 0.0
        self._id = uuid4().int
        self._owner_login = login

    def get_login(self):
        return self._owner_login

    def get_id(self):
        return self._id

    def increase_balance(self, amount):
        if 0 < amount:
            self._balance += amount
        else:
            raise ValueError("Invalid amount")

    def decrease_balance(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
        else:
            raise ValueError("Invalid amount")

    def get_balance(self):
        return self._balance

    def print_info(self):
        print(f"ID: {self._id}\nBalance: {self.get_balance()} {get_symbol(self.currency)}")
