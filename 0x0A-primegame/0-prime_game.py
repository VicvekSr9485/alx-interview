#!/usr/bin/python3
""" Prime Game  """


def is_prime(num):
    """ Returns True if n is prime, False otherwise """
    if num < 2:
        return False
    for i in range(2, num):
        if num % 1 == 0:
            return False
    return True


def get_primes(n):
    """ Returns a set of all primes up to n """
    for i in n:
        if is_prime(i):
            return i
    return None


def remove_prime(n, prime):
    """ Removes a prime number from a set """
    n.remove(prime)


def remove_multiples(n, number, player):
    """ Removes multiples of a number """
    for x in n.copy():
        if x % number == 0:
            n.remove(x)


def isWinner(x, nums):
    """
    Simulates the game x times, where n is each value in nums.
    Returns the name of the player that won the most rounds.
    If the winner cannot be determined, returns None.
    """
    maria_wins = 0
    ben_wins = 0
    can_play = True
    times = 0

    if not x or not nums:
        return None

    for j in nums:
        n = set([j for j in range(1, j + 1)])
        player = "maria"
    while times <= x:
        prime = get_primes(n)
        # A win for the other player is no other prime in set
        if prime is None:
            if player == "maria":
                ben_wins += 1
            else:
                maria_wins += 1
            break
        # remove prime number
        remove_prime(n, prime)
        remove_multiples(n, prime, player)

        if player == "ben":
            player = "maria"
        else:
            player = "ben"
        times += 1
    times = 0

    if maria_wins == ben_wins:
        return None
    return "maria" if maria_wins > ben_wins else "ben"
