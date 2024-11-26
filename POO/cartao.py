from datetime import datetime



class Cartao:
    assentos = ['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15']

    def __init__(self, nome, voo, codigo, datahora, checkin, assento):
        self.nome = nome
        self.voo = voo
        self.codigo = codigo
        self.datahora = self.validahora(datahora)
        self.checkin = checkin
        self.assento = assento

    def valida_hora(self,datahora):
        datahora_convertida = datetime.strptime(datahora, "%d/%m/%Y - %H:%M")
        return datahora_convertida
    
    def valida_checkin(self):
        self.checkin = True
        return self.checkin

    def altera_assento(self):
        try:
            op = int(input('Qual assento você deseja?\n'))
            print(f'****ASSENTOS****\n'
                f'|{assentos[0]}|{assentos[1]}|{assentos[2]}|{assentos[3]}|{assentos[4]}|\n'
                f'|{assentos[5]}|{assentos[6]}|{assentos[7]}|{assentos[8]}|{assentos[9]}|\n'
                f'|{assentos[10]}|{assentos[11]}|{assentos[12]}|{assentos[13]}|{assentos[14]}|')
            assento_escolhido = (assentos.index(op)) - 1
            assentos = assentos.pop(assento_escolhido)
            assentos = assentos.insert(assento_escolhido,'X')
        except ValueError:
            raise ValueError('Digite um número válido')
        if op < 1 or op > 15:
            raise ValueError('Opção inválida. Digite um número entre 1 e 15')
    
    
    
def main():
 

if __name__ == '__main__':
    main()