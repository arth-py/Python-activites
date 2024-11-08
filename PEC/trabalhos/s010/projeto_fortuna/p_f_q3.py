from random import *

def main():
    jogando = True

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
    while jogando == True:
        print("\nEscolha uma porta (1, 2 ou 3):")
        
        portaEscolhida=int(input())
        portaCerta= randint(1,3)
        print("A porta escolhida foi a", portaEscolhida)
        print("A porta certa é a", portaCerta)
        if portaEscolhida == portaCerta:
            print("Parabéns")
            score += 1
        else:
            print("Que peninha")

        print("Sua pontuação é:", score)
        print("\nVocê quer jogar de novo? (s/n)")
        resposta = input().lower()
        if resposta == 'n':
            jogando = False
    print("Obrigado por jogar.")
    print("Sua pontuação final é de", score)
if __name__=='__main__':
    main()
