from user import *
from wallet import *
from transactions import *

transaction_history = []

Ilyuka = User("Ilyuka", "dragonwar26russ")
Danilko = User("Danilko", "danniuz")
Kekril = User("Kekril", "shortyk")

Ilyuka.create_wallet(Currencies.USD)
Ilyuka.create_wallet(Currencies.RUB)
Ilyuka.create_wallet(Currencies.RUB)

Kekril.create_wallet(Currencies.USD)
Kekril.create_wallet(Currencies.USD)

Ilyuka.wallets[0].top_up(3000)
Ilyuka.wallets[1].top_up(3001)

Danilko.wallets[0].top_up(5000)

Kekril.wallets[0].top_up(50)
Kekril.wallets[1].top_up(350)

transaction_history.append(transfer(Kekril, Ilyuka, Kekril.wallets[1], Ilyuka.wallets[0], 100))
transaction_history.append(transfer(Kekril, Ilyuka, Kekril.wallets[1], Ilyuka.wallets[1], 50))

transaction_history.append(transfer(Kekril, Kekril, Kekril.wallets[1], Kekril.wallets[0], 197))

Kekril.delete_wallet(Kekril.wallets[1].get_wallet_id())

for trans in transaction_history:
    print(trans.__dict__)


