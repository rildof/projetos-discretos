from buscaprimos import isPrime
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
        return [pow(i, self.e, self.n) for i in x]

    # 3)
    # Mostre que qualquer texto claro m pode ser recuperado
    # a partir do criptograma y e a chave privada (d, n).
    def decrypt(self, y):
        return [pow(j, self.d, self.n) for j in y]

    def calc_e(self):
        e = 2
        while (sympy.gcd(e, self.phi_n) != 1):
            e += 1
        return e

    def sign(self, x):
        return [pow(i,self.d,self.n) for i in x]

    def verify_sign(self, ass):
        return [pow(i,self.e,self.n) for i in ass]

# 1)
# Procura-se dois
# números primos, p e q, independentes, de tamanho 1024
# bits ou maior;
def get_primes():
    n1 = pow(2, 1024)
    n2 = pow(2, 1025)
    randprime1 = sympy.randprime(n1, n2)
    randprime2 = sympy.randprime(n1, n2)
    return randprime1, randprime2

def phi(n):
    result = 1
    for i in range(2, n):
        if (sympy.gcd(i, n) == 1):
            result += 1
    return result

def txt_to_ascii(txt):
    return [ord(i) for i in txt]
def ascii_to_txt(ascii):
    a = [chr(i) for i in ascii]; return ''.join(a)


if __name__ == "__main__":
    p, q = get_primes()
    rsa = RSAsystem(p, q)

    f = open('public_key','w')
    g = open('private_key', 'w')

    f.write('('+str(rsa.e)+' , '+str(rsa.n)+')')
    g.write('('+str(rsa.d)+' , '+str(rsa.n)+')')

    x = 'Prova foi adiada'
    x = txt_to_ascii(x)

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

