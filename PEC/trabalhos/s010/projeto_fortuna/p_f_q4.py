from random import *
def main():
    tentativas = 0
    score = 0
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
    

    ''')
    while score < 3:
        tentativas += 1
        print('\n',7*'*',"Tentativa",tentativas,7*'*',"\n\nEscolha uma porta (1, 2 ou 3):")
        portaEscolhida=int(input())
        portaCerta= randint(1,3)
        print("A porta escolhida foi a", portaEscolhida)
        print("A porta certa é a", portaCerta)
        if portaEscolhida == portaCerta:
            print("\nParabéns")
            score += 1
        else:
            print("Que peninha...")

        print("Sua pontuação é:", score)

    print("\n** Você conseguiu! Terminou o jogo em",tentativas, "tentativas**\n") 
if __name__=='__main__':
    main()
