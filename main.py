"""

TODO:
Разобраться с типами ✔
Переписать логику переводов (сейчас отрицательный кошель) ✔
set_balance в пополнить баланс/уменьшить баланс ✔
ID кошельков хранить в хэш мапе ✔
Выбор кошельков для манипуляций ✔
Тесты

"""

from user import User
from wallet import Wallet
from transactions import *

transaction_history = []
users = []


class Engine:
    _active_users_wallets = {}

    def choose_wallet(self, user: User):
        user.print_wallets()
        print("Choose a wallet: ")
        wallet_id = int(input())
        self._active_users_wallets[user.login] = wallet_id

    def ui_transfer(self, sender: User, recipient: User, amount: float):
        sender_wallet_id = self._active_users_wallets[sender.login]
        recipient_wallet_id = self._active_users_wallets[recipient.login]

        sender_wallet = sender.get_wallet(sender_wallet_id)
        recipient_wallet = recipient.get_wallet(recipient_wallet_id)

        new_transaction = transfer(sender_wallet, recipient_wallet, amount)
        transaction_history.append(new_transaction)

        print("\nYour transaction from:\n")
        sender_wallet.print_info()
        print("\nto:\n")
        recipient_wallet.print_info()
        print("\nsuccessfully completed!")

        return new_transaction  # Даня сказал ВДРУГ ПРИГОДИТСЯ. Лично мне ПОЕБАТЬ

    def ui_top_up(self, user: User, amount: float):
        user_wallet_id = self._active_users_wallets[user.login]
        user_wallet = user.get_wallet(user_wallet_id)
        user_wallet.increase_balance(amount)

        print("\nWallet topped up!")
        user_wallet.print_info()


engine = Engine()

Ilyuka = User("Ilyuka", "dragonwar26russ")
Kekril = User("Kekril", "shortyk")

Ilyuka.create_wallet(Currencies.USD)
# Ilyuka.create_wallet(Currencies.RUB)

# Kekril.create_wallet(Currencies.USD)
# Kekril.create_wallet(Currencies.USD)
Kekril.create_wallet(Currencies.RUB)


engine.choose_wallet(Kekril)
engine.choose_wallet(Ilyuka)

engine.ui_top_up(Kekril, 5000)

engine.ui_transfer(Kekril, Ilyuka, 243)