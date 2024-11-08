from random import *

def main():
    print('''
    Porta da Fortuna!
    ========

    Existe um super premio atras de uma destas 3 portas
    Adivinhe qual é a porta certa para ganhar o prêmio!
     ___  ___  ___
    |   ||   ||   |
    |[1]||[2]||[3]|
    |  o||  o||  o|
    |___||___||___|
    
    Escolha uma porta(1,2 ou 3):
    ''')

    portaEscolhida=int(input())
    portaCerta= randint(1,3)
    print("A porta escolhida foi a", portaEscolhida)
    print("A porta certa é a", portaCerta)


    if portaEscolhida == portaCerta:
        print("Parabéns")
    else:
        print("Que peninha")
if __name__=='__main__':
    main()
