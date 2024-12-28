from random import *
from datetime import datetime
# Quando ele der inicio o cartao dele deve estar ativo e imprimir  o status e o preço atual
class Cartao:

    def __init__(self,numero,dh_entrada=None,preco=0,status=False,dh_saida=None):
        self.numero = numero
        self.dh_entrada = dh_entrada 
        self.preco = preco
        self.status = status
        self.dh_saida = dh_saida
        
    # Função para Alterar o status do cartão
    def muda_cartao(self):
        self.status = not self.status
    #Função para captar retornar a hora de saída

    def muda_preco(self):
        hora_atual = datetime.strptime(self.dh_entrada, "%H:%M")
        # O atributo da hora da saída recebe o return da função hora saida
        self.dh_saida = datetime.now()
        hora = self.dh_saida.hour - hora_atual.hour 
        minuto = self.dh_saida.minute - hora_atual.minute 
        if hora < 2 or hora == 2 and minuto == 0:
            return 8.00
        elif hora > 2 or hora == 2 and minuto > 14:
            minutos_extras = (hora - 2)*60 + minuto
            preco_total = minutos_extras*0.50
            return 8.00 + preco_total

        

    def __str__(self):
        preco_str = "Nada a pagar" if self.preco == 0 else f"R$ {self.preco:.2f}"
        preco_str = str(preco_str)
        preco_str = preco_str.replace(".",',')
        return (
            f'ID: {self.numero}\n'
            f'Entrada: {self.dh_entrada}\n'
            f'Saída: {self.dh_saida if self.dh_saida else "Ainda no estacionamento"}\n'
            f'Status: {"Ativo" if self.status else "Inativo"}\n'
            f'Preço: {preco_str}'
        )

def main():

    usuario = randrange(10000000,99999999)
    # Criação Objeto
    c1 = Cartao(numero=usuario)
    while True:
        print(f'****BEM VINDO AO SHOPPING RIVERSIDE!****\n'
              f'1. ENTRAR NO ESTACIONAMENTO\n'
              f'2. SAIR DO ESTACIONAMENTO\n')
        try:
            
            op = int(input())
            if op == 1:
                if c1.status:
                    print("Você já está no estacionamento!")
                    print(c1)
                else:
                    '''A variável recebe a data e tempo atual pela classe datetime e método now()'''
                    agora_entrada = datetime.now()
                    # A variável recebe, convertidos para o formato string somente a Hora e o Minuto
                    h_entrada = agora_entrada.strftime("%H:%M")
                    c1.dh_entrada = h_entrada
                    c1.muda_cartao()
                    print('Você entrou no estacionamento!')
                    print(c1)
            
            
            elif op == 2:
                if c1.status:
                    c1.muda_cartao()
                    c1.preco = c1.muda_preco()
                    print(c1)
                    print("FOI UM PRAZER TER VOCÊ CONOSCO! ATÉ A PRÓXIMA ;3")
                    break
                else:
                    print(f"Você não está no estacionamento!\n")
                    
            else:
                print("Opção inválida, escolha 1 ou 2.")
                

        except ValueError:
            raise ValueError('Opção inválida, escolha um valor entre  1 e 2.')

if __name__ =='__main__':
    main()

