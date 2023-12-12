from buscaprimos import isPrimeMillerRabin
from cod_texto import text2int, int2text
import random
import sys
import sympy


class RSAsystem:

    def __init__(self, p, q):
        self.p = p
        self.q = q
        self.n = p*q
        self.phi_n = (p-1)*(q-1)
        self.e = self.calc_e()
        self.d = pow(self.e,-1, self.phi_n)

    # 2)
    # Implemente a função que aplica a chave (e, n) em um
    # “bignumber” m qualquer. Note que essa mesma função é
    # utilizada para decifrar criptogramas e para assinar textos
    # y=mensagem criptografada
    # y cong x(mensagem)^e mod n
    def encrypt(self, x):
        return pow(x, self.e, self.n)

    # 3)
    # Mostre que qualquer texto claro m pode ser recuperado
    # a partir do criptograma y e a chave privada (d, n).
    def decrypt(self, y):
        return pow(y, self.d, self.n)

    def calc_e(self):
        e = 2
        while (sympy.gcd(e, self.phi_n) != 1):
            e += 1
        return e

    def sign(self, x):
        return pow(x,self.d,self.n)

    def verify_sign(self, ass):
        return pow(ass,self.e,self.n)

# 1)
# Procura-se dois
# números primos, p e q, independentes, de tamanho 1024
# bits ou maior;
def generate_random_prime(bits):
    while True:
        num = random.getrandbits(bits)
        num |= (1 << 0)  # Garante que o número seja ímpar e do tamanho correto
        print(num)
        if isPrimeMillerRabin(num, 5):
            return num

def get_primes():
    min_bits = 1024
    max_bits = 2048

    p = generate_random_prime(random.randint(min_bits, max_bits))
    q = generate_random_prime(random.randint(min_bits, max_bits))

    return p, q

if __name__ == "__main__":
    p, q = get_primes()
    rsa = RSAsystem(p, q)

    f = open('public_key','w')
    g = open('private_key', 'w')

    f.write('('+str(rsa.e)+' , '+str(rsa.n)+')')
    g.write('('+str(rsa.d)+' , '+str(rsa.n)+')')

    x = 'texto de teste'
    x = text2int(x)

    y = rsa.encrypt(x)

    print('Texto claro: ',x)
    print('Texto encriptografado: ',y)
    print('------------------------------------------------------------------------------')

    #print(ascii_to_txt([i for i in y]))

    #decrypted_x = [decrypt(i,d,n) for i in y]
    #print(ascii_to_txt(decrypted_x))

    #5)
    #Recebe [Texto criptografado(x) , assinatura(ass)]
    #usando a chave pública, descriptografa-se a assinatura = pow(ass, e, n)
    #Se for igual à mensagem descriptografada, deu bom
    ass = rsa.sign(x)
    ass_dec = rsa.verify_sign(ass)
    print("Texto assinado: ", ass)
    print("Texto assinado descriptografado: ", ass_dec)

