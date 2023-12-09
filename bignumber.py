class bignumber:
    def __init__(self,num):
        self.num = num
        self.b = self.binário()
      

    def binário(self):
        b = 0
        num=self.num
        while True:
            if num >2:
                b+=1
                num//=2
            else:
                b+=1
                self.b=b
                return b   
    
    def comp(self,c):
        if self.b+c <2048:
            return True
        else:
            return False

    def adição(self,soma):
        self.num+=soma
    
    def subtração(self,subtração):
        self.num-=subtração

    def multiplicação(self,multiplicação):
        self.num*=multiplicação

    def divisão(self,divisão):
        self.num/=divisão
        