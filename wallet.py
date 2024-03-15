from transactions import *
from uuid import uuid4


class Wallet:
    def __init__(self, currency: Currencies):
        self.currency = currency
        self._id = uuid4().int
        self._balance = 0

    def top_up(self, amount):
        self._balance += amount

    def get_balance(self):
        return self._balance

    def set_balance(self, new_balance):
        self._balance = new_balance

    def get_wallet_id(self):
        return self._id
