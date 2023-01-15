#!/usr/bin/python3
""" Minimum Operations module
"""


def minOperations(n: int) -> int:
    """ Returns the minimum number of operations
    """
    if n <= 0:  # If the desired number of H's is impossible to achieve
        return 0
    dp = [0] * (n + 1)  # Create an array to store the minimum number of operations needed for each value of n
    for i in range(2, n + 1):
        dp[i] = i  # Set the initial value of dp[i] to i
        for j in range(2, i):
            if i % j == 0:  # If i is divisible by j
                dp[i] = min(dp[i], dp[j] + 1 + i // j)  # Update dp[i] with the minimum number of operations needed
    return dp[n]  # Return the minimum number of operations needed for n H's
