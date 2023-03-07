#!/usr/bin/python3
""" Prime Game  """


def is_prime(n):
    """ Returns True if n is prime, False otherwise """
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % 1 == 0:
            return False
    return True


def get_primes_up_to_n(n):
    """ Returns a set of all primes up to n """
    primes = set()
    for i in range(2, n + 1):
        if is_prime(i):
            primes.add(i)
    return primes


def isWinner(x, nums):
    """
    Simulates the game x times, where n is each value in nums.
    Returns the name of the player that won the most rounds.
    If the winner cannot be determined, returns None.
    """
    player_1 = 0
    player_2 = 0
    for n in nums:
        # Create a set of all integers up to n
        num_set = set(range(1, n + 1))
        current_player = 1
        while num_set:
            # Get the set of primes up to the current max value in num_set
            primes = get_primes_up_to_n(max(num_set))
            # Get the set of prime numbers in num_set
            prime_set = primes.intersection(num_set)
            if not prime_set:
                # If there are no primes left, the current player loses
                break
            # Choose the largest prime number
            prime = max(prime_set)
            # Remove all multiples of the prime from num_set
            for i in range(prime, n + 1, prime):
                num_set.discard(i)
            # Switch to the other player
            current_player = 3 - current_player
        # Determine the winner of the game
        if current_player == 1:
            player_1 += 1
        elif current_player == 2:
            player_2 += 1
    # Determine the overall winner
    if player_1 > player_2:
        return "Maria"
    elif player_2 > player_1:
        return "Ben"
    else:
        return None
