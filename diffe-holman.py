from random import randint
from buscaprimos import isPrime
from math import sqrt


#funções auxiliares
def gcd(a, b):
    if (a == 0):
        return b
    return gcd(b % a, a)
# A simple method to evaluate
# Euler Totient Function
def phi(n):
    result = 1
    for i in range(2, n):
        if (gcd(i, n) == 1):
            result += 1
    return result

def findPrimefactors(s, n):
    # Print the number of 2s that divide n
    while (n % 2 == 0):
        s.add(2)
        n = n // 2

    # n must be odd at this point. So we can
    # skip one element (Note i = i +2)
    for i in range(3, int(sqrt(n)), 2):

        # While i divides n, print i and divide n
        while (n % i == 0):
            s.add(i)
            n = n // i

            # This condition is to handle the case
    # when n is a prime number greater than 2
    if (n > 2):
        s.add(n)




def generate_primes():
    #Passo 1)
    # Implementação da geração de números primos
    # Gere um primo q, em que p=2q+1 também seja primo
    #O primo q tem que ser de pelo menos 1024 bits.


    pass

def primitive_root_amount(p): #Retorna o número de raízes primitivas de um primo p.
    #Passo 2.1)
    #Se o n tem raízes primitivas, phi(phi(n)) é o número de raízes primitivas de n.
    #Porém, se n é um primo, então n possui phi(p-1) raízes primitivas(a incluso)
    return phi(p-1)


def findPrimitive(n):
    #Passo 2.2)
    s = set()

    # Check if n is prime or not
    if (isPrime(n) == False):
        return -1

    # Find value of Euler Totient function
    # of n. Since n is a prime number, the
    # value of Euler Totient function is n-1
    # as there are n-1 relatively prime numbers.
    phi = n - 1

    # Find prime factors of phi and store in a set
    findPrimefactors(s, phi)

    # Check for every number from 2 to phi
    for r in range(2, phi + 1):

        # Iterate through all prime factors of phi.
        # and check if we found a power with value 1
        flag = False
        for it in s:

            # Check if r^((phi)/primefactors)
            # mod n is 1 or not
            if (pow(r, phi // it, n) == 1):
                flag = True
                break

        # If there was no power with value 1.
        if (flag == False):
            return r

            # If no primitive root found
    return -1


def diffie_hellman_key_exchange():
    # Tamanho do número primo
    size = 10  # Tamanho do número primo em bits

    # Geração dos números primos p e q
    q = generate_prime(size)
    p = 2 * q + 1

    # Encontrar uma raiz primitiva de 'p'
    g = calculate_primitive_root(p)

    # Usuário 0 escolhe um número secreto
    secret_0 = randint(2, p - 2)
    public_0 = pow(g, secret_0, p)

    # Usuário 1 escolhe um número secreto
    secret_1 = randint(2, p - 2)
    public_1 = pow(g, secret_1, p)

    # Troca de chaves e cálculo da chave compartilhada
    shared_key_0 = pow(public_1, secret_0, p)
    shared_key_1 = pow(public_0, secret_1, p)

    # Ambos os usuários têm a mesma chave compartilhada
    if shared_key_0 == shared_key_1:
        return shared_key_0
    else:
        return None

# Execução do protocolo Diffie-Hellman
shared_key = diffie_hellman_key_exchange()
if shared_key:
    print("Chave compartilhada:", shared_key)
else:
    print("Erro na troca de chaves.")
