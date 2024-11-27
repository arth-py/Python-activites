from datetime import datetime

class Cartao:
    assentos = ['01','X','03','04','05','X','07','08','X','X','11','X','13','X','15']

    def __init__(self, nome, voo, codigo, datahora, checkin='Não realizado', assento='Nenhum até o momento'):
        self.nome = nome
        self.voo = voo
        self.codigo = codigo
        self.datahora = self.valida_hora(datahora)
        self.checkin = checkin
        self.assento = assento

    def valida_hora(self,datahora):
        datahora_convertida = datetime.strptime(datahora, "%d/%m/%Y - %H:%M")
        return datahora_convertida
    
    def valida_checkin(self):
        self.checkin = 'Realizado'
        return self.checkin

    def altera_assento(self):
        try:
            print(f'****ASSENTOS****\n'
                f'|{Cartao.assentos[0]}|{Cartao.assentos[1]}|{Cartao.assentos[2]}|{Cartao.assentos[3]}|{Cartao.assentos[4]}|\n'
                f'|{Cartao.assentos[5]}|{Cartao.assentos[6]}|{Cartao.assentos[7]}|{Cartao.assentos[8]}|{Cartao.assentos[9]}|\n'
                f'|{Cartao.assentos[10]}|{Cartao.assentos[11]}|{Cartao.assentos[12]}|{Cartao.assentos[13]}|{Cartao.assentos[14]}|')
            op = int(input('Qual assento você deseja?\nEscolha um numero entre 1-15: '))
            endereco_assento = op-1
            if Cartao.assentos[endereco_assento] == 'X':
                return (f'Assento já ocupado, escolha outro')
            else:
                del Cartao.assentos[endereco_assento]
                Cartao.assentos.insert(endereco_assento, ' X')
        except ValueError:
            raise ValueError('Digite um número válido')
        if op < 1 or op > 15:
            raise ValueError('Opção inválida. Digite um número entre 1 e 15')
    
    def __str__(self):
        return(f'Nome: {self.nome}\n'
              f'Voo: {self.voo}\n'
              f'Codigo: {self.codigo}\n'
              f'Datahora: {self.datahora}\n'
              f'Checkin: {self.checkin}\n'
              f'Assento: {self.assento}\n')
    
def main():
    c1 = Cartao('Pedro','00987','1178','04/03/2005 - 08:30') 
    c2 = Cartao('Laura','00125','4532','17/08/2005 - 21:45') 
    c3 = Cartao('Pedro','03847','5643','15/01/2004 - 17:30') 
    while True:
        print(f'\n*********Seja bem vindo {c1.nome}!*********\n')
        print(f'{c1}')
        print('\n*********Opções*********\n')
        print(f'1. Realizar Check-in\n'
              f'2. Escolher/Trocar Assento')
        try:
            opc = int(input())
        except ValueError:
            raise ValueError('Opção inválida. Escolha um número entre 1 e 2.')
        if opc > 2 or opc < 1:
            raise ValueError('Opção inválida. Escolha um número entre 1 e 2.')
        
        if opc == 1:
            if c1.checkin == 'Realizado':
                print('Check-in já realizado! :)')
            else:
                c1.valida_checkin()

        if opc == 2:
            c1.altera_assento()


if __name__ == '__main__':
    main()