import random
import math
import time


def brent(n):
    if n % 2 == 0:
        return 2
		
    y, c, m = random.randint(1, n-1), random.randint(1, n-1), random.randint(1, n-1)
    g, r, q = 1, 1, 1

    ys = y
    x = y

    while g == 1:
        x = y
        for i in range(r):
            y = ((y * y) % n + c) % n
        k = 0
        while k < r and g == 1:
            ys = y
            for i in range(min(m, r - k)):
                y = ((y * y) % n + c) % n
                q = q * (abs(x - y)) % n
            g = math.gcd(q, n)
            k = k + m
        r = r * 2

    if g == n:
        while True:
            ys = ((ys * ys) % n + c) % n
            g = math.gcd(abs(x - ys), n)
            if g > 1:
                break
    return g


# Driver function
if __name__ == "__main__":
    # n = 10967535067
    t_start = time.time()
    n = 13726304630375965451
    print("One of the divisors for", n, "is ", brent(n))
    t_end = time.time()
    print("Time taken : ", t_end - t_start)