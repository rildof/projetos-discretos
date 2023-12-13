# -*- coding: utf-8 -*-
"""
UFPE
Matematica Discreta
Autor: Prof. Gilson Jeronimo

Codificador de Texto
"""

"testando o codificador"
def text2int(texto):
    number = 0;
    for i in range(len(texto)):
        if ((ord(texto[i]) >= ord('a')) & (ord(texto[i]) <= ord('z'))):
            number = number + (1 + ord(texto[i]) - ord('a')) * (27 ** i);
    return (number);

def int2text(inteiro):
    textoascii = [];
    q = inteiro;
    while q > 0:
        r = q % 27;
        if (r != 0):
            asciinumber = r + ord('a') - 1;
        else:
            asciinumber = ord(' ');
        textoascii.extend([asciinumber]);
        q = q // 27;
    return ("".join([chr(value) for value in textoascii]));
