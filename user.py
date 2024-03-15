import datetime
from wallet import *

CURRENT_DATE = str(datetime.datetime.now().date())


class User:
    def __init__(self, full_name, login):
        self.full_name = full_name
        self.login = login
        self.creation_date = CURRENT_DATE
        self.wallets = []

    def create_wallet(self, currency: Currencies):
        self.wallets.append(Wallet(currency))

    def delete_wallet(self, wallet_id):
        for wallet in self.wallets:
            if wallet.get_wallet_id() == wallet_id and wallet.get_balance() == 0:
                self.wallets.remove(wallet)
                break
