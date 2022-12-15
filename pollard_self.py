import random
import math
import time


# function for primality testing
def rabin_miller(p):

    if p < 2:
        return False

    if p != 2 and p % 2 == 0:
        return False

    if p == 2:
        return True

    s = p-1

    while s % 2 == 0:
        s >>= 1

    for i in range(10):
        a = random.randrange(p-1) + 1
        temp = s
        mod = pow(a, temp, p)

        while temp != p-1 and mod != 1 and mod != p-1:
            mod = (mod * mod) % p
            temp = temp * 2

        if mod != p-1 and temp % 2 == 0:
            return False

    return True


# method to return list of prime factors for n
def pollard_rho(n):
    # no prime divisor for 1

    # list to store prime factors of n
    result = []

    if n == 2:
        result += [n]
        return result

    while n % 2 == 0:
        n = math.floor(n / 2)
        result += [2]

    if n == 1:
        return result

    if rabin_miller(n):
        result += [n]
        return result

    # Initializing x and y to be used in f(x) = x^2 + c
    x = random.randint(2, n-1)
    y = x

    # the constant in f(x).
    c = random.randint(1, n-1)

    # Initialize candidate divisor (or result)
    d = 1

    # until the prime factor isn't obtained.
    # If n is prime, return n
    while d == 1:

        # Tortoise Move: x(i+1) = f(x(i))
        x = ((x * x) % n + c) % n

        # Hare Move: y(i+1) = f(f(y(i)))
        y = ((y * y) % n + c) % n
        y = ((y * y) % n + c) % n

        # check gcd of |x-y| and n
        d = math.gcd(abs(x - y), n)

        # retry if the algorithm fails to find prime factor with chosen x and c
        if d == n:
            return pollard_rho(n)

    result += pollard_rho(d)
    new_n = n//d
    result += pollard_rho(new_n)

    return result


# To test whether algorithm produced correct results
def test_algorithm(actual, expected):
    actual.sort()
    expected.sort()
    if actual == expected:
        return True
    return False


# Driver function
if __name__ == "__main__":

    f = open("test_case_partial.txt", 'r')

    while True:
        line_n_input = f.readline()  # read testcase from file
        line_result_expected = f.readline()

        if line_n_input != '':
            n_input = int(line_n_input)
            result_expected = [int(i) for i in line_result_expected.split()]

            # call algorithm method to obtain actual results
            # also calculate time required (elapsed time) for complete calculation
            t_start = time.time()
            result_actual = pollard_rho(n_input)
            t_end = time.time()
            elapsed_time = t_end - t_start

            if test_algorithm(result_actual, result_expected):
                print("\nPollard rho algorithm produced correct results.")
                print("Time taken is {} ms".format(elapsed_time * 1000))
                print("The prime factors of {} are {}".format(n_input, result_actual))
            else:
                print("\nPollard rho algorithm produced incorrect results.")
                print("\nActual prime factors of {} generated running algorithm are {}".format(n_input, result_actual))
                print("\nExpected prime factors of {} are {}".format(n_input, result_expected))
        else:
            break

    print('Exit success')
