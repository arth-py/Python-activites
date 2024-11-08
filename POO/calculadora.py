'''implementar uma classe que simule uma calculadora simples
(ver a calculadora do windows como referencia)
implementar os métodos:
ligar()
desligar()
reset()
calcular()
'''

class Calculadora:
    
    n1 = 0
    n2 = 0
    op = None
    

    def ligar(self.):
        

    def calcular(self,n1,n2,op):
        self.n1 = n1
        self.n2 = n2
        self.op = op
        
        if self.op == '+':
            return self.n1 + self.n2
        elif self.op == '-':
            return self.n1 - self.n2
        elif self.op == '/':
            if self.numero2 != 0:
                return self.n1 / self.n2
            else:
                return "Erro: Impossível dividir por 0"
        elif self.op == '*':
            return self.n1 * self.n2
        else:
            return "Operação inválida"
        

    def reset(self,n1,n2,op):
        self.n1 = 0
        self.n2 = 0
        self.op = None
        n1 = self.n1
        n2 = self.n2
        op = self.op
        
        return n1,n2,op
        

    



def main():
    my_calculator = Calculadora()
if __name__ == '__main__':
    main()
