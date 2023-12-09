from bignumber import bignumber

x= int(input())
y= int(input())
a= bignumber(x)
b= bignumber(y)
z=x*y
if a.comp(b.binário()) == True:
    c= bignumber(z)
    print("c é um bignumber")
z=x+y
if a.binário()==b.binário():
    c=bignumber(z)
    if c.b == a.b+1:
        print("comprovado")
    elif c.b == a.b:
        print("comprovado")
