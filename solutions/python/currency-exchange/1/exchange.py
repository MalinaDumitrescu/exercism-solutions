"""Functions for calculating steps in exchanging currency.

Python numbers documentation: https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex

Overview of exchanging currency when travelling: https://www.compareremit.com/money-transfer-tips/guide-to-exchanging-currency-for-overseas-travel/
"""


def exchange_money(budget, exchange_rate):
    """Calculate estimated value after exchange."""
    return budget / exchange_rate


def get_change(budget, exchanging_value):
    """Calculate currency left after an exchange."""
    return budget - exchanging_value


def get_value_of_bills(denomination, number_of_bills):
    """Calculate total value of a specific number of bills."""
    return denomination * number_of_bills


def get_number_of_bills(amount, denomination):
    """Calculate the number of bills of a given denomination."""
    return int(amount // denomination)


def get_leftover_of_bills(amount, denomination):
    """Calculate the leftover amount that cannot be returned in whole bills."""
    return amount % denomination


def exchangeable_value(budget, exchange_rate, spread, denomination):
    """Calculate maximum value of new currency in whole bill denominations."""
    actual_rate = exchange_rate * (1 + spread / 100)
    total_currency = budget / actual_rate
    number_of_bills = total_currency // denomination
    return int(number_of_bills * denomination)
