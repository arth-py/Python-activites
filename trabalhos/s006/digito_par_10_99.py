''' Escreva um programa que leia um número inteiro entre 10 e 99, mostre uma das mensagens, a seguir, conforme o número lido.

Nenhum dígito é ímpar.
Apenas um dígito é ímpar.
Os dois dígitos são ímpares. '''

def impar(x):
    return x % 2 == 0

def digito_dezena(x):
    dezena = x // 10
    return impar(dezena)

def digito_unidade(x):
    unidade = x % 10
    return impar(unidade)
    
def main():
    numero = int(input('Insira um número entre  10 e 99 : '))
    resultado_dezena = digito_dezena(numero)
    resultado_unidade = digito_unidade(numero)
    if resultado_dezena and resultado_unidade:
        print ('Nenhum dígito é ímpar.')
    elif resultado_dezena and not resultado_unidade:
        print ('Apenas um dígito é ímpar.')
    elif not resultado_dezena and resultado_unidade:
        print ('Apenas um dígito é ímpar.')
    else:
        print ('Os dois dígitos são ímpares.')
if __name__ =='__main__':
    main()
                 
