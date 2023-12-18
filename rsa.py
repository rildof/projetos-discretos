from buscaprimos import isPrimeMillerRabin
from cod_texto import text2int, int2text
import random
from aritModular import addmod, mulmod, expmod, invmod
from bignumber import bignumber
import sys

class RSAsystem:

    def __init__(self):
        self.p, self.q = self.get_primes()
        self.p, self.q = bignumber(self.p) , bignumber(self.q)
        self.n = self.p.getNumber() * self.q.getNumber()
        self.phi_n = ( self.p.getNumber() - 1 )*( self.q.getNumber() - 1 )
        self.e = self.calc_e()
        self.d = invmod(self.e, self.phi_n)

    # 2)
    # Implemente a função que aplica a chave (e, n) em um
    # “bignumber” m qualquer. Note que essa mesma função é
    # utilizada para decifrar criptogramas e para assinar textos
    # y=mensagem criptografada
    # y cong x(mensagem)^e mod n
    def encrypt(self, x):
        return expmod(x, self.e, self.n)

    # 3)
    # Mostre que qualquer texto claro m pode ser recuperado
    # a partir do criptograma y e a chave privada (d, n).
    def decrypt(self, y):
        return expmod(y, self.d, self.n)

    def calc_e(self):
        e = 2
        while (mdc(e, self.phi_n) != 1):
            e += 1
        return e

    def sign(self, x):
        return expmod(x,self.d,self.n)

    def verify_sign(self, ass):
        return expmod(ass,self.e,self.n)

    def get_primes(self):
        min_bits = 1024
        max_bits = 2048

        p = generate_random_prime(random.randint(min_bits, max_bits))
        q = generate_random_prime(random.randint(min_bits, max_bits))

        return p, q
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

def mdc(a, b):
    return a if not b else mdc(b, a % b)

if __name__ == "__main__":

    rsa = RSAsystem()

    f = open('public_key','w')
    g = open('private_key', 'w')

    f.write('('+str(rsa.e)+' , '+str(rsa.n)+')' + '\n')
    g.write('('+str(rsa.d)+' , '+str(rsa.n)+')' + '\n')

    x = 'texto de teste'
    x = text2int(x)
    x = bignumber(x)
    y = rsa.encrypt(x.getNumber())

    print('Texto claro: ',int2text(x.getNumber()))
    print('Texto encriptografado: ',int2text(y))
    print('------------------------------------------------------------------------------')

    #print(ascii_to_txt([i for i in y]))

    #decrypted_x = [decrypt(i,d,n) for i in y]
    #print(ascii_to_txt(decrypted_x))

    #5)
    #Recebe [Texto criptografado(x) , assinatura(ass)]
    #usando a chave pública, descriptografa-se a assinatura = pow(ass, e, n)
    #Se for igual à mensagem descriptografada, deu bom
    ass = rsa.sign(x.getNumber())
    ass_dec = rsa.verify_sign(ass)
    print("Texto assinado: ", ass)
    print("Texto assinado descriptografado: ", int2text(ass_dec))

