from datetime import *

class CNH:
    def __init__(self,nome,cpf,d_nascimento,categoria,d_validade,d_emissao):
        self.nome = nome
        self.cpf = cpf
        #pq precisa colocar self antes de chamar a função valida?
        self.d_nascimento = self.valida_data(d_nascimento)
        self.categoria = self.valida_categoria(categoria)
        self.d_validade = self.valida_validade(d_validade)
        self.d_emissao = self.valida_emissao(d_emissao)

    def valida_data(self,data):

        # Try except com conversão da string no formato data
        try:
            data = datetime.strptime(data, "%d/%m/%Y").date() # .date() utilizado para remover a parte horária da data
            return data 
        except ValueError:
            # Havendo um erro, a data não é valida e retorna False
            raise ValueError(f'Data de nascimento inválida')
    
    def valida_categoria(self,categoria):
        categorias_validas = ('A','B','C','D','E')
        for c in categoria:
            while c not in categorias_validas:
                print('Categoria inválida')
                categoria = input('Digite novamente a(s) categoria(s):')
        return categoria
    
    def valida_validade(self,d_validade):
        # Try except com conversão da string no formato data
        try:
            self.d_validade= datetime.strptime(d_validade, "%d/%m/%Y").date()
            if self.d_validade > date.today():
                return self.d_validade 
            else:
                d_validade = input('Data Atrasada, digite uma no futuro')
        except ValueError:
            # Havendo um erro, a data não é valida e retorna False
            raise ValueError(f'Data de validade inválida')
    
    def valida_emissao(self,data):
        # Try except com conversão da string no formato data
        try:
            '''CRIAR CONDIÇÃO PARA QUE O ANO DE EMISSÃO TENHA AO MENOS  18 ANOS DA IDADE'''
            data_emissao = datetime.strptime(self.d_emissao, "%d/%m/%Y").date()
            data_nascimento = datetime.strptime(self.d_nascimento, "%d,%m,%Y").date()
            data = datetime.strptime(data, "%d/%m/%Y").date() # .date() utilizado para remover a parte horária da data
            if data_emissao.year - data_nascimento.year < 18:
                raise ValueError(f'Insira uma idade válida.')
            else:
                return data 
        except ValueError as e:
            # Havendo um erro, a data não é valida e retorna False
            raise ValueError(f'{e} não é uma data válida')
        
    def __str__(self):
        return(f'CARTEIRA DE HABILITAÇÃO:\n'
               f'-------------------\n'
               f'NOME: {self.nome}\n'
               f'CPF: {self.cpf}\n'
               f'DATA DE NASCIMENTO: {self.d_nascimento}\n'
               f'CATEGORIA: {self.categoria}\n'
               f'DATA DE VALIDADE: {self.d_validade}\n'
               f'DATA DE EMISSÃO: {self.d_emissao}\n'
               f'-------------------')

def main():
    nome = input('Digite o nome: ')
    cpf = input('Digite o CPF: ')
    nascimento = input('Digite a data de nascimento dd/mm/aa: ')
    categorias = input('Digite as categorias sem espaçamento (ex:AB): ').upper()
    validade = input('Digite o prazo de validade dd/mm/aa: ')
    emissao = input('Digite a data de emissão dd/mm/aa: ')
    c1 = CNH(nome,cpf,nascimento,categorias,validade,emissao)
    '''while True:
        print(c1)
        print(' O que você deseja fazer?')
        print(' 1. Adicionar uma Categoria')
        print(' 2. Alterar a data de validade')
        op = int(input())'''
    print(c1)
if __name__ == '__main__':
    main()