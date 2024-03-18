from enum import Enum


def get_symbol(currency):
    match currency:
        case Currencies.USD: return "$"
        case Currencies.RUB: return "₽"


class Currencies(Enum):
    USD = "USD"
    RUB = "RUB"
