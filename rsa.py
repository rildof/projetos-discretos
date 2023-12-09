#1)
#Procura-se dois
#números primos, p e q, independentes, de tamanho 1024
#bits ou maior;
from buscaprimos import isPrime
import random
import sys
import sympy
verbose = 1
#a)
def get_primes():
    p = pow(2,1024)
    q = pow(2,1025)
    randprime1 = sympy.randprime(p,q)
    randprime2 = sympy.randprime(p,q)
    return randprime1, randprime2

if verbose: print('getting primes')
p,q = get_primes()


#b)
if verbose: print('calculating n=p*q')
n = p*q


#Cálculo de e
e = 2
def phi(n):
    result = 1
    for i in range(2, n):
        if (sympy.gcd(i, n) == 1):
            result += 1
    return result
phi_n = (p-1)*(q-1)
if verbose: print('calculating e')
while(sympy.gcd(e,phi_n) != 1 ):
    e+=1
#Cálculo d
if verbose: print('e=',e)

if verbose: print('calculating d')
d = pow(e,-1, phi_n)

if verbose: print('writing to file')
f = open('public_key','w')
g = open('private_key', 'w')

f.write('('+str(e)+' , '+str(n)+')')
g.write('('+str(d)+' , '+str(n)+')')

#2)
#Implemente a função que aplica a chave (e, n) em um
#“bignumber” m qualquer. Note que essa mesma função é
#utilizada para decifrar criptogramas e para assinar textos

#y=mensagem criptografada
#y cong x(mensagem)^e mod n

def encrypt(x,e,n): return pow(x,e, n)

#4)
#Mostre na prática um exemplo de texto claro sendo
#cifrado utilizando a chave pública (e, n) e a recuperação
#de m a partir do criptograma e a chave privada (d, n)
x = 'texto qualquer'
def txt_to_ascii(txt): return [ord(i) for i in txt]
def ascii_to_txt(ascii): a = [chr(i) for i in ascii]; return ''.join(a)
x = txt_to_ascii(x)

y = [encrypt(i,e,n) for i in x]
print(y)
print('x=',x)
print('y=',y)


#print(ascii_to_txt([i for i in y]))
#3)
#Mostre que qualquer texto claro m pode ser recuperado
#a partir do criptograma y e a chave privada (d, n).
def decrypt(y,d,n): return pow(y,d,n)

#decrypted_x = [decrypt(i,d,n) for i in y]
#print(ascii_to_txt(decrypted_x))

#5)
#Recebe [Texto criptografado(x) , assinatura(ass)]
#usando a chave pública, descriptografa-se a assinatura = pow(ass, e, n)
#Se for igual à mensagem descriptografada, deu bom
ass = [pow(i,d,n) for i in x]
ass_dec = [decrypt(i,e,n) for i in ass]
print(ass_dec)
print()
print(y)
