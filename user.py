from datetime import datetime

from wallet import Wallet
from currencies import Currencies


class User:
    def __init__(self, full_name, login):
        self.full_name = full_name
        self.login = login
        self.creation_date = str(datetime.now().date())
        self.wallets = {}

    def get_wallet(self, wallet_id):
        return self.wallets[wallet_id]

    def create_wallet(self, currency: Currencies):
        wallet = Wallet(currency, self.login)
        self.wallets[wallet.get_id()] = wallet

    def delete_wallet(self, wallet_id):
        if self.wallets[wallet_id].get_balance() == 0.0:
            self.wallets.pop(wallet_id)

    def print_wallets(self):
        for wallet_id, wallet in self.wallets.items():
            wallet.print_info()
