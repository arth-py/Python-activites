'''2. Implemente a classe Bicicleta, colocando limites máximos
e mínimos para os estados: veloc_atual,
altura_cela e calibragem_pneus através de seus respectivos métodos.
Altere os métodos: regular_cela,
calibrar_pneus para permitirem as mudanças caso a bicicleta esteja
parada (veloc_atual=0).'''

class Bicicleta():
    def __init__(self,vel=0,aceleracao=0,altura=0,pressao=0,H_cela=0,pneu=0):
        self.vel = vel
        self.aceleracao = aceleracao
        self.altura = altura
        self.pressao = pressao
        self.H_cela = H_cela
        self.pneu = pneu
        

    def acelerar(self,aceleracao):
        self.aceleracao = aceleracao
        self.vel += self.aceleracao
        self.aceleracao = 0
        return self.vel
    
    def desacelerar(self,aceleracao):
        self.aceleracao = aceleracao
        self.vel -= self.aceleracao
        self.aceleracao = 0
        return self.vel
    
    def regular_cela(self,altura):
        self.altura = altura
        self.H_cela += self.altura
        self.altura = 0
        return self.H_cela

    def calibrar(self,pressao):
        self.pressao = 10*pressao
        self.pneu += self.pressao
        self.pressao = 0
        return self.pneu

def main():
    bike = Bicicleta()
    while True:
        try:
            print(f'\n\n*********BICICLETA*********')
            print(f'_______________________')
            print(f'\n|VELOCIDADE ATUAL: {bike.vel} km/h')
            print(f'|ALTURA DA CELA  : {bike.H_cela}º Nível')
            print(f'|PRESSÃO DO PNEU : {bike.pneu} Pa')
            print(f'_______________________\n')
            print(f'1.Acelerar')
            print(f'2.Desacelerar')
            print(f'3.Regular cela')
            print(f'4.Calibrar pneu')
            print(f'5.Descer da bicicleta')
            
            op = int(input('\nEscolha uma opção: '))
            if op == 1:
                bike.acelerar(float(input('Quanto você deseja acelerar? (Km/h): ')))
            elif op == 2:
                if bike.vel > 0:
                    bike.desacelerar(float(input('Quanto você deseja desacelerar? (Km/h): ')))
                else:
                    print(f'\nERRO: Impossível desacelerar com bicicleta parada')
            elif op == 3:
                if bike.vel == 0:
                    bike.regular_cela(int(input('Qual nível? (1-2-3): ')))
                else:
                    print(f'\nERRO: Impossível regular cela com a bicicleta em movimento')
            elif op == 4:
                if bike.vel == 0:
                    bike.calibrar(int(input('Quantas vezes? (10/vez): ')))
                else:
                    print(f'\nERRO: Impossível calibrar pneu com a bicicleta em movimento')
            elif op == 5:
                if bike.vel > 0:
                    print('\nERRO: Impossível descer com a bicicleta em movimento')
                else:
                    print('\nVocê desceu da bicicleta')
                    break
        except ValueError:
            print(f'Opção inválida!')
            
            
if __name__ == "__main__":
    main()
