import random

def miller(d, n):
    a = 2 + random.randint(1, n - 4)

    x = pow(a, d, n)

    if (x == 1 or x == n - 1):
        return True

    while (d != n - 1):
        x = (x * x) % n
        d *= 2

        if (x == 1):
            return False
        if (x == n - 1):
            return True

    return False

def fermat(n, k):
    for i in range(k):
        a = random.randint(2, n - 2)

        # Fermat's little theorem
        if pow(a, n - 1, n) != 1:
            return False

    return True

def isPrime(n, k):
    if n == 4:
        return False
    elif n == 2 or n == 3:
        return True

    # Find r such that n =
    # 2^d * r + 1 for some r >= 1
    d = n - 1
    while (d % 2 == 0):
        d //= 2

    # Iterate given number of 'k' times
    for i in range(k):
        if not miller(d, n) and not fermat(n, k):
            return False

    return True