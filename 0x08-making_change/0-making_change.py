#!/usr/bin/python3
""" Solution to 'Make Change' Interview Problem """


def makeChange(coins, total):
    """ returns fewest number of coins needed to
        meet a given amount total
    """
    # if total is 0 or less, 0 is returned
    if total <= 0:
        return 0

    # next, initialize list(or array) with maximum amount
    # beyond total amount to calculate a new minimum
    # Now using dynamic programming:
    dp = [total + 1] * (total + 1)
    # setting minimum number of coins for amount 0
    dp[0] = 0

    for amount in range(1, total + 1):
        for coin in coins:
            if amount - coin >= 0:
                dp[amount] = min(dp[amount], 1 + dp[amount - coin])
    if dp[total] < total + 1:
        return dp[total]
    return -1
