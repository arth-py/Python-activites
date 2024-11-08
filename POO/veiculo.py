class Veiculo:
    def __init__(self,
                 chassi,
                 marca,
                 modelo,
                 ano,
                 placa='Não especificado',
                 cor='Não especificada',
                 dono='Não especificado',
                 quilometragem=0
                 ):
        self.chassi = chassi
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.placa = placa
        self.cor = cor
        self.dono = dono
        self.quilometragem = quilometragem
        return
    
    def muda_cor(self,nova_cor):
        self.cor = nova_cor
        return
    
    def andar(self,km):
        self.quilometragem += km
        return
    
    def mudar_dono(self,nome):
        self.dono = nome
        return

    
    def __str__(self):
        return (
        f'MARCA: {self.marca}\n'
        f'MODELO: {self.modelo}\n'
        f'ANO: {self.ano}\n'
        f'PLACA: {self.placa}\n'
        f'COR: {self.cor}\n'
        f'DONO: {self.dono}\n'
        f'QUILOMETRAGEM: {self.quilometragem}'
        )
        


def main():
    v1 = Veiculo('HE21J', 'Toyota', 'Celta', 2009)
    while True:
        print(f'___________\n')
        print(v1)
        print(f'___________\n')
        
        print('1. Mudar a cor')
        print('2. Andar')
        print('3. Mudar dono')
        print('4. Sair')
        while True:
            try:
                op = input('Escolha uma opção:')
                op = int(op)
                if op in [1,2,3,4]:
                    break
                else:
                    print('Opção inválida. Digite um valor entre 1, 2, 3 ou 4.')
            except ValueError:
                print('Opção inválida. Digite um valor entre 1, 2, 3 ou 4.')


        if op == 1:
            print('Digite a nova cor: ')
            nova_cor = input()
            v1.muda_cor(nova_cor)
        elif op == 2:
            print('Digite quantos quilômetros deseja andar:')
            km = float(input())
            v1.andar(km)
        elif op == 3:
            print('Digite o nome do novo dono:')
            nome = input()
            v1.mudar_dono(nome)
        elif op == 4:
            print('Fim da execução')
            break

if __name__ == '__main__':
    main()