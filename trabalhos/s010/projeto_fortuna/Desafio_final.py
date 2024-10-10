from random import *

def main():
    # Declarando variáveis
    soma= 0
    jogo = True
    print('''
    Tente fazer exatamente 21 pontos!
    ''')
        # Condição para que a repetição ocorra enquanto o usuário disser sim
    while jogo == True:
        # Define um número a partir de 1 a 10        
        numeroRandom= randint(1,10)
        # Soma recebe o valor de soma + numeroRandom       
        soma += numeroRandom
        # Impressão das variáveis       
        print("O número emitido foi ", numeroRandom)
        print("Pontuação atual : ", soma)
        # Condição para que o usuário vença
        if soma == 21:
            print("VOCÊ VENCEU")
        # Condição para que o usuário perca
        if soma > 21:
            print("VOCÊ PERDEU")
            break
        print("Quer somar mais um número? (s/n):")
        resposta=input().lower()
        # Condição para que o usuário responda se quer continuar ou não o jogo
        if resposta == 'n':
            jogo = False
        elif resposta == 's':
            continue
if __name__=='__main__':
    main()
