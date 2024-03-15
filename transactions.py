from uuid import uuid4
from user import *
from constants import *
from currencies import *


def transfer(sender, recipient, sender_wallet, recipient_wallet, amount):
    sender_balance = sender_wallet.get_balance()
    recipient_balance = recipient_wallet.get_balance()
    sender_balance -= amount

    commission = 0 if sender.login == recipient.login else amount * COMMISSION

    if sender_wallet.currency != recipient_wallet.currency:  # Конверт
        recipient_balance += convert(amount, sender_wallet.currency, recipient_wallet.currency)
    else:  # Траснфер
        recipient_balance += amount

    sender_wallet.set_balance(sender_balance - commission)
    recipient_wallet.set_balance(recipient_balance)

    return Transaction(sender, recipient, sender_wallet, recipient_wallet, amount)


def convert(amount, currency_input: Currencies, currency_output: Currencies):
    match (currency_input, currency_output):
        case (Currencies.RUB, Currencies.USD):
            return amount * EXCHANGE_RATE
        case (Currencies.USD, Currencies.RUB):
            return amount / EXCHANGE_RATE


class Transaction:

    def __init__(self, sender, recipient, sender_wallet, recipient_wallet, amount):
        self._sender = sender
        self._recipient = recipient
        self._sender_wallet = sender_wallet
        self._recipient_wallet = recipient_wallet
        self._amount = amount
        self._transaction_id = uuid4().hex
