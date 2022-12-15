import random
import math
import time


# method to return prime divisor for n
def pollard_rho(n):
    # no prime divisor for 1
    if (n == 1):
        return n

    # even number means one of the divisors is 2
    if (n % 2 == 0):
        return 2

    # we will pick from the range [2, N)
    x = random.randint(2, n-1)
    y = x

    # the constant in f(x).
    # Algorithm can be re-run with a different c
    # if it throws failure for a composite.
    c = random.randint(1, n-1)

    # Initialize candidate divisor (or result)
    d = 1

    # until the prime factor isn't obtained.
    # If n is prime, return n
    while (d == 1):

        # Tortoise Move: x(i+1) = f(x(i))
        x = ((x * x) % n + c) % n

        # Hare Move: y(i+1) = f(f(y(i)))
        y = ((y * y) % n + c) % n
        y = ((y * y) % n + c) % n

        # check gcd of |x-y| and n
        d = math.gcd(abs(x - y), n)

        # retry if the algorithm fails to find prime factor
        # with chosen x and c
        if (d == n):
            return PollardRho(n)

    return d


# Driver function
if __name__ == "__main__":
    # n = 10967535067
    t_start = time.time()
    n = 51697133118993596900552868527219
    n = 13726304630375965451
    print("One of the divisors for", n, "is ", pollard_rho(n))
    t_end = time.time()
    print("Time taken : ", t_end - t_start)
