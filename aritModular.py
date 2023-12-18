#Here goes code

def addmod(a, b, n):
    return (a + b) % n


def mulmod(a, b, n):
    return (a * b) % n


def expmod(a, b, n):
    return pow(a, b, n)


def invmod(a, n):
    return pow(a, -1 ,n)

