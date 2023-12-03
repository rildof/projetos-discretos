#Here goes code
import math

# From https://www.geeksforgeeks.org/largest-coprime-set-between-two-integers/
# Function to find the largest
# co-prime set of the integers
def findCoPrime(n, m):
    # Initialize sets
    # with starting integers
    a = [n]
    b = [[n]]

    # Iterate over all the possible
    # values of the integers
    for i in range(n + 1, m + 1):

        # lcm of each list in array
        # 'b' stored in list 'a'
        # so go through list 'a'
        for j in range(len(a)):

            # if there gcd is 1 then
            # element add in that
            # list corresponding to b
            if math.gcd(i, a[j]) == 1:
                # update the new lcm value
                q = (i * a[j]) // math.gcd(i, a[j])
                r = b[j]
                r.append(i)
                b[j] = r
                a[j] = q
        else:
            a.append(i)
            b.append([i])
    maxi = []
    for i in b:
        if len(i) > len(maxi):
            maxi = i
    print(*maxi)
def farey(limit):
    '''Fast computation of Farey sequence as a generator'''
    # n, d is the start fraction n/d (0,1) initially
    # N, D is the stop fraction N/D (1,1) initially
    pend = []
    n = 0
    d = N = D = 1
    while True:
        mediant_d = d + D
        if mediant_d <= limit:
            mediant_n = n + N
            pend.append((mediant_n, mediant_d, N, D))
            N = mediant_n
            D = mediant_d
        else:
            yield n, d
            if pend:
                n, d, N, D = pend.pop()
            else:
                break
def addmod(a, b, n):
    return (a + b) % n


def mulmod(a, b, n):
    return (a * b) % n


def expmod(a, b, n):
    return pow(a, b, n)


def invmod(a, n):
    return pow(a, -1 ,n)

 #print(*farey(100))
#Testando as funções
a = int(1e19)
b = 1
n = int(1e19+1)

print("addmod:", addmod(a, b, n))
print("mulmod:", mulmod(a, b, n))
print("expmod:", expmod(a, b, n))
print("invmod:", invmod(a, n))