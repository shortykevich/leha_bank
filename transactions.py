from uuid import uuid4

from constants import *
from currencies import Currencies
from wallet import Wallet


def transfer(sender_wallet: Wallet, recipient_wallet: Wallet, amount: float):
    sender = sender_wallet.get_login()
    recipient = recipient_wallet.get_login()
    sender_balance = sender_wallet.get_balance()
    sender_balance -= amount

    commission = 0 if sender == recipient else amount * COMMISSION

    if sender_wallet.currency != recipient_wallet.currency:  # Конвертация
        recipient_delta = convert(amount, sender_wallet.currency, recipient_wallet.currency)
    else:  # Траснфер
        recipient_delta = amount

    if sender_balance < commission:
        raise ValueError("Sender, not enough babki")

    sender_delta = amount + commission

    sender_wallet.decrease_balance(sender_delta)
    recipient_wallet.increase_balance(recipient_delta)

    return Transaction(sender, recipient, sender_wallet, recipient_wallet, amount)


def convert(amount: float, currency_input: Currencies, currency_output: Currencies):
    match (currency_input, currency_output):
        case (Currencies.RUB, Currencies.USD):
            return amount / EXCHANGE_RATE
        case (Currencies.USD, Currencies.RUB):
            return amount * EXCHANGE_RATE


class Transaction:
    _sender = None
    _recipient = None
    _sender_wallet = None
    _recipient_wallet = None

    def __init__(self, sender, recipient, sender_wallet: Wallet, recipient_wallet: Wallet, amount: float):
        self._sender = sender
        self._recipient = recipient
        self._sender_wallet = sender_wallet
        self._recipient_wallet = recipient_wallet
        self._amount = amount
        self._transaction_id = uuid4().hex
